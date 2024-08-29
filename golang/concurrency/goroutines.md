## Concurrency

Concurrent programming refers to the expression of a program as a composition of several autonomous activities to hide latency of I/O operations and to exploit modern computer's many processors.

GO enables two styles of concurrent programming. First style is goroutines and channels, which support communicating sequential processes (CSP) in which values are passed between independent activities. Second is traditional model of shared memory multithreading.

## Goroutines

Each concurrently executing activity is called goroutine (similar to threading). A sequential program may call one function and then another, but a concurrent program with two or more goroutines, call to both functions at same time. When program starts, its only goroutine is the one that calls main() i.e. main goroutine. New goroutines are created by go statement.

There is no programmatic way for one goroutine to stop another other than by returning from main or exiting the program. However, there are ways to communicate with a goroutine to request that it stop itself.

```go
f()
go f()  // creates new goroutine that calls f(); doesn't wait for f() to finish
```

```go
func main() {
  go spinner(100 * time.Milisecond)
  const n = 45
  fibN := fib(n)
  fmt.Printf("\rFibonacci(%d) = %d\n", n, fibN)
}

func spinner(delay time.Duration) {
  for {
    for _, r := range `-\|/` {
      fmt.Printf("\r%c", r)
      time.Sleep(delay)
    }
  }
}

func fib(x int) int {
  if x < 2 {
    return x
  }
  return fib(x-1) + fib(x-2)
}
```

### Select

Select statement lets a goroutine wait on multiple communication operations i.e. used to choose from multiple send/receive channel operations. It allows a program to try reading from or writing to a number of channels at the same time.

A select blocks until one of its cases can run, then it executes that case. It **chooses one at random if multiple cases are ready** i.e. only one channel operation happens per select statement.

The default case in a select is run if no other case is ready.

```go
select {
case i := <-c:
    // use i
default:
    // receiving from c would block
}

// if have a single channel, range will suffice.
for _ = range ch {
  // do something
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

### Limiting goroutines

```go
maxGoroutines := 10
guard := make(chan bool, maxGoroutines)
guard <- true
go func() {
  h.handleSenderMsg(ctx, msg)
  <- guard
}()
```

## Waiting for goroutines

The application terminates when the main goroutine exits. If you want to wait for goroutines, use sync.WaitGroup.

```go
package main

import (
  "net/http"
  "sync"
)

func main() {
  var wg sync.WaitGroup
  var urls = []string{
    "http://www.golang.org/",
    "http://www.google.com/",
    "http://www.somestupidname.com/",
  }
  for _, url := range urls {
    // Increment the WaitGroup counter.
    wg.Add(1)
    // Launch a goroutine to fetch the URL.
    go func(url string) {
      // Decrement the counter when the goroutine completes.
      defer wg.Done()
      // Fetch the URL.
      http.Get(url)
    }(url)
  }
  // Wait for all HTTP fetches to complete.
  wg.Wait()
}
```

## Stopping goroutines

### Use channels to signal termination

```go
func myProcess(stopChannel chan bool) {
  for {
    select {
    case <-stopChannel:
      fmt.Println("Hey! Shantanu. Thanks for stopping my goroutine :) ")
      return
    default:
      fmt.Println("My Goroutine is running :( ")
      time.Sleep(time.Second)
    }
  }
}
```

### Use context to manage goroutine lifecycle

```go
func myProcess(ctx context.Context) {
  for {
    select {
    case <-ctx.Done():
      fmt.Println("Hey! Shantanu. Thanks for stopping my goroutine :)")
      return
    default:
      fmt.Println("My Goroutine is running :(")
      time.Sleep(time.Second)
    }
  }
}

func main() {
  ctx, cancel := context.WithCancel(context.Background())
  go myProcess(ctx)
  time.Sleep(3 * time.Second)
  cancel()
  time.Sleep(time.Second)
  fmt.Println("Main Goroutine exited")
}
```

### Breaking when all channels are closed

A nil channel is never ready for communication. Each time you run into a closed channel, you can nil that channel ensuring it is never selected again.

```go
for {
  select {
    case x, ok := <- ch:
    if !ok {
      ch = nil
    }
    case x, ok := <- ch2:
    if !ok {
      ch2 = nil
    }
  }
  if ch == nil && ch2 == nil {
    break
  }
}
```

## Goroutine vs Thread

<table>
<tr>
<th>Gorutine</th>
<th>Threads</th>
</tr>

<tr>
<td>Managed by the go runtime</td>
<td>Managed by kernel</td>
</tr>

<tr>
<td>Not hardware dependent</td>
<td>Dependent on OS system</td>
</tr>

<tr>
<td>Have easy communication medium through channel with low latency; does not need explicit managed locks and mutexes for synchronization</td>
<td>Does not have an easy communication medium with high latency</td>
</tr>

<tr>
<td>Does not have a unique ID as it does not have Thread Local Storage</td>
<td>Have their own unique ID</td>
</tr>

<tr>
<td>Cheaper than threads, faster startup time</td>
<td>More expensive than goroutine</td>
</tr>

<tr>
<td>Are cooperatively scheduled</td>
<td>Are preemptively scheduled</td>
</tr>

<tr>
<td>Have growable segmented stacks; allows dynamic stack management to efficiently create goroutines without wasting memory</td>
<td>Does not have growable segmented stacks i.e. fixed-size stacks which can be wasteful for small tasks</td>
</tr>

</table>
