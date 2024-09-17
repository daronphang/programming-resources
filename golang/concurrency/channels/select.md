## Select

Select statement lets a goroutine wait on multiple communication operations i.e. used to choose from multiple send/receive channel operations. It allows a program to try reading from or writing to a number of channels at the same time. Select statement is the glue that binds channels together.

A select blocks until one of its cases can run, then it executes that case. It **chooses one at random if multiple cases are ready** i.e. only one channel operation happens per select statement.

The default case in a select is executed if no other case is ready.

```go
select {
case i := <-c:
    // use i
default:
    // receiving from c would block
}
```

```go
package main

import (
    "fmt"
    "time"
)

func server1(ch chan string) {
    time.Sleep(6 * time.Second)
    ch <- "from server1"
}
func server2(ch chan string) {
    time.Sleep(3 * time.Second)
    ch <- "from server2"

}
func main() {
    output1 := make(chan string)
    output2 := make(chan string)
    go server1(output1)
    go server2(output2)
    select {
    case s1 := <-output1:
        fmt.Println(s1)
    case s2 := <-output2:
        fmt.Println(s2)
    }
}
```

```go
package main

import "fmt"

func fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}
}

func main() {
	c := make(chan int)
	quit := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			fmt.Println(<-c)
		}
		quit <- 0
	}()
	fibonacci(c, quit)
}

/*
0
1
1
2
3
5
8
13
21
34
quit
*/
```

### Deadlock

Select statement will block forever since no other goroutine is writing to the channel. Program will panic at runtime.

```go
package main

func main() {
    ch := make(chan string)
    select {
    case <-ch:
    }
}
```

### for-select loop

There are a couple of scenarios this pattern can be used:

- Sending iteration variables out on a channel
- Looping infinitely waiting to be stopped

```go
for _, s := range []string{"a", "b", "c"} {
    select {
    case <-done:
        return
    case stringStream <- s:
    }
}
```

```go
for {
    select {
    case <- done:
        return
    default:
        // Do non-preemptable work
    }
}
```

## or-channel

At times you may find yourself wanting to combine one or more done channels into a single done channel that closes if any of its component channels close. You can create a one-liner by combining channels together through recursion and goroutines.

```go
var or func(channels ...<-chan interface{}) <-chan interface{}
or = func(channels ...<-chan interface{}) <-chan interface{} {
    switch len(channels) {
    case 0:
        return nil
    case 1:
        return channels[0]
    }

    orDone := make(chan interface{})

    // When any of the channels are closed, goroutine will close orDone channel
    // When goroutines up the tree exit, goroutines down the tree also exit
    go func() {
        defer close(orDone)
        switch len(channels) {
        case 2:
            select {
            case <- channels[0]:
            case <- channels[1]:
            }
        default:
            select {
            case <- channels[0]:
            case <- channels[1]:
            case <- channels[2]:
            case <- or(append(channels[3:], orDone)...):
            }
        }
    }()
    return orDone
}
```

```go
sig := func(after time.Duration) <-chan interface{}{
    c := make(chan interface{})
    go func() {
        defer close(c)
        time.Sleep(after)
    }()
    return c
}

start := time.Now()
<-or(
    sig(2*time.Hour),
    sig(5*time.Minute),
    sig(1*time.Second),
    sig(1*time.Hour),
    sig(1*time.Minute),
)
fmt.Printf("done after %v", time.Since(start))
// done after 1.000216772s
```
