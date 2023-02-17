## Context

When developing production-grade systems serving web requests, it is helpful for a function to know more about the environment it is being executed in, aside from the information it needs to work on its own.

For instance, a web server function handling an HTTP request for a client may only require a URL as a parameter, but knowing the client's connection status allows the server to stop processing the request/stop goroutines in the event the client disconnects. **This helps to reduce load and save valuable compute resources on a busy server, and frees them up to handle another client's request**. Examples include timeout, deadline or channel to indicate stop working and return. To enable ubiquitous access to this type of information, Go has included a context package.

### Creating Context

Two ways to create context using Background() or TODO(). Latter can be used by static analysis tools to validate if the context is passed around properly.

```go
package main

import (
	"context"
	"fmt"
)

func doSomething(ctx context.Context) {
	fmt.Println("Doing something!")
}

func main() {
	ctx := context.TODO()
    // ctx, cancel := context.Background()
	doSomething(ctx)
}
```

### Using Data Within Context

Have the ability to access data stored inside a context. By adding data to a context, it can be passed from function to function. Data stored is immutable.

To override a context's value, need to wrap the parent context.

```go
func main() {
	ctx := context.Background()
	ctx = context.WithValue(ctx, "myKey", "myValue")
    fmt.Printf("doSomething: myKey's value is %s\n", ctx.Value("myKey"))
}
```

```go
func doSomething(ctx context.Context) {
	fmt.Printf("doSomething: myKey's value is %s\n", ctx.Value("myKey"))    // myKey

	anotherCtx := context.WithValue(ctx, "myKey", "anotherValue")
	doAnother(anotherCtx)   // wrapped parent context in another

	fmt.Printf("doSomething: myKey's value is %s\n", ctx.Value("myKey"))    // referring to parent context: myKey
}

func doAnother(ctx context.Context) {
	fmt.Printf("doAnother: myKey's value is %s\n", ctx.Value("myKey"))
}
```

### Ending a Context

Provides a signal to any functions using it that the context has ended and should be considered complete i.e. other functions know to stop processing any work related to the context that they may still be working on.

Done() can be checked to see whether a context has ended or not. Method returns a channel that is closed when the context is done i.e. returns nil for every read attempt on the channel.

```go
ctx := context.Background()
resultsCh := make(chan *WorkResult)

for {
	select {
	case <- ctx.Done():
		// The context is over, stop processing results
		return
	case result := <- resultsCh:
		// Process the results received
	}
}
```

### Ending a Context

```go
func doSomething(ctx context.Context) {
	ctx, cancelCtx := context.WithCancel(ctx)

	printCh := make(chan int)
	go doAnother(ctx, printCh)

	for num := 1; num <= 3; num++ {
		printCh <- num
	}
	cancelCtx()
	time.Sleep(100 * time.Millisecond)
	fmt.Printf("doSomething: finished\n")
}

func doAnother(ctx context.Context, printCh <-chan int) {
	for {
		select {
		case <-ctx.Done():
			if err := ctx.Err(); err != nil {
				fmt.Printf("doAnother err: %s\n", err)
			}
			fmt.Printf("doAnother: finished\n")
			return
		case num := <-printCh:
			fmt.Printf("doAnother: %d\n", num)
		}
	}
}

/*
doAnother: 1
doAnother: 2
doAnother: 3
doAnother err: context canceled
doAnother: finished
doSomething: finished
*/

```

### Deadline/Timeout

Set a deadline on a context to automatically end when that deadline passes. For timeout, you provide a time for the context to end.

```go
func doSomething(ctx context.Context) {
	deadline := time.Now().Add(1500 * time.Millisecond)
	ctx, cancelCtx := context.WithDeadline(ctx, deadline)
    // ctx, cancelCtx := context.WithTimeout(ctx, 1500*time.Millisecond)

	defer cancelCtx()   // in case there are return statements

	printCh := make(chan int)
	go doAnother(ctx, printCh)

	for num := 1; num <= 3; num++ {
		select {
		case printCh <- num:
			time.Sleep(1 * time.Second)
		case <-ctx.Done():
			break
		}
	}
	// cancelCtx()
	time.Sleep(100 * time.Millisecond)
	fmt.Printf("doSomething: finished\n")
}

```
