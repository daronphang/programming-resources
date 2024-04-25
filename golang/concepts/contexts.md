## Context

When developing production-grade systems serving web requests, it is helpful for a function to know more about the environment it is being executed in, aside from the information it needs to work on its own.

For instance, a web server function handling an HTTP request for a client may only require a URL as a parameter, but knowing the client's connection status allows the server to stop processing the request/stop goroutines in the event the client disconnects. **This helps to reduce load and save valuable compute resources on a busy server, and frees them up to handle another client's request**. Examples include timeout, deadline or channel to indicate stop working and return. To enable ubiquitous access to this type of information, Go has included a context package.

Context in Go refers to the circumstances that form the setting for an event. In other words,the context package can be used to make the functions/goroutines to act according to certain events in the system.

### Why need context?

- Listen to cancellation: When the system is shutting down, it should cancel all background processes and tasks for graceful shutdown of services
- Notifying timeouts and deadline: If a service times out, we need to cancel our goroutines and not waste compute resources
- Passing miscellaneous key values: Context can be used to pass values from middleware

### Creating context

Two ways to create context:

- context.Background(): Does nothing, an abstract
- context.TODO(): Code should use context.TODO() when it is unclear which context to use or it is not yet available (because the surrounding function has not yet been extended to accept a Context parameter); for the purpose of code refactoring and code analysis

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

### Using data within context

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

### Ending a context

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

### Deadline or timeout

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

## Example

```go
func main() {
	// creating parent context
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	// this is for graceful shutdown
	exit := make(chan os.Signal, 1)
	signal.Notify(exit, os.Interrupt, syscall.SIGTERM)

	for {
		select {
		case <-exit:
			cancel()
			fmt.Println("shutting down gracefully.")
		case <-ctx.Done():
			// listens for parent context cancellation
			fmt.Println("parent context is cancelled.")
			os.Exit(0)
		default:
			// calls our service check every one second.
			time.Sleep(1 * time.Second)
			if serviceHealthCheck(ctx, "https://google.com") {
				fmt.Println("Service OK")
			} else {
				fmt.Println("Service Fail")
			}
		}
	}
}

// serviceHealthCheck is a very dumb healthcheck which
// takes an url and return true if able to get the url
// in the specified context timout duration else false.
func serviceHealthCheck(ctx context.Context, url string) bool {
	status := make(chan bool, 1)

	// create a new context with parent ctx and provide timeout duration
	// you can also use context.WithDeadline as follows.
	//ctx, cancel := context.WithDeadline(ctx, time.Now().Add(700*time.Millisecond))
	ctx, cancel := context.WithTimeout(ctx, 700*time.Millisecond)

	defer cancel()

	// dummy implementation of service health check
	go func(url string) {
		client := http.Client{}
		if _, err := client.Get(url); err != nil {
			status <- false
		}
		status <- true
	}(url)

	select {
	case s := <-status:
		return s
	case <-ctx.Done():
		fmt.Println("request timeout")
		return false
	}
}
```
