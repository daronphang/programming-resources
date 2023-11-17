## Communicating Sequential Processes (CSP)

When it comes to concurrency, many programming languages adopt the Shared Memory/State Model. However, Go distinguishes itself by implementing CSP. In CSP, a program consists of parallel processes that do not share state; instead, they communicate and synchronize their actions using channels.

## Channels

Channels are the connections between goroutines i.e. a communication mechanism that lets one goroutine send values to another goroutine. A channel has two principal operations, **send** and **receive**. Also supports a third operation, **close**, which sets a flag indicating that no more values will ever be sent on this channel; subsequent attempts to send will panic. Receive operations on a close channel yield the values that have been sent until no more values are left.

### Send, Receive, Close

A channel has two principal operations, "send" and "receive". A send statement transmits a value from one goroutine, through the channel, to another executing a corresponding receive expression. A receive expression whose result is not used is a valid statement.

Channels support a third operation "close" which sets a flag indicating that no more values will ever be sent on this channel; subsequent attempts to send will panic.

```go
ch := make(chan int)    // ch has type 'chan int', unbuffered channel
ch := make(chan int, 0)  // unbuffered channel
ch := make(chan int, 3)  // buffered channel with capacity 3

close(ch)

ch <- x   // a send statement
x = <-ch    // a receive expression in an assignment statement
<-ch    // a receive statement, reuslt is discarded
```

## Unbuffered Channels (Synchronous)

A send operation on an unbuffered channel blocks the sending goroutine until another goroutine executes a corresponding receive on the same channel, at which point the value is transmitted and both goroutines may continue. Conversely, if the receive operation is attempted first, the receiving goroutine is blocked until a send is transmitted.

```go
func main() {
    conn, err := net.Dial("tcp", "localhost:8000")
    if err != nil {
        log.Fatal(err)
    }
    done := make(chan struct{})
    go func() {
        io.Copy(os.Stdout, conn) // NOTE: ignoring errors
        log.Println("done")
        done <- struct{}{} // signal the main goroutine
    }()
    mustCopy(conn, os.Stdin)
    conn.Close()
    <-done // wait for background goroutine to finish
}
```

## Unidirectional Channel Types

To document the intent exclusively and prevent misuse.

```go
// send-only channel of int, allows sends but not receives
func counter(out chan<- int) {
    for x := 0; x < 100; x++ {
        out <- x
    }
    close(out)
}

// receive-only channel of int, allows receives but not sends
func squarer(out chan<- int, in <-chan int) {
    for v := range in {
        out <- v * v
    }
    close(out)
}

func printer(in <-chan int) {
    for v := range in {
        fmt.Println(v)
    }
}

func main() {
    naturals := make(chan int)
    squares := make(chan int)

    go counter(naturals)
    go squarer(squares, naturals)
    printer(squares)
}
```

## Buffered Channels

A buffered channel has a queue of elements. The queue's maximum size is determined when it is created, by the capacity argument to make.

A send operation inserts an element at the back of the queue, and a receive operation removes an element from the front. If the channel is full, the send operation blocks its goroutine until space is made available by another goroutine's receive.

```go
// can send up to 3 values on this channel without goroutine blocking
ch = make(chan string, 3)

ch <- "A"
ch <- "B"
ch <- "C"

fmt.Println(<-ch) // receive "A", frees up one space
```

## Buffered vs Unbuffered

The choice between unbuffered and buffered channels may affect the correctness of a program. Unbuffered channels give stronger synchronization guarantees while in buffered channels, the operations are decoupled.

## Cancellation

Sometimes may need to instruct goroutine to stop what it is doing i.e. web server performing computation on behalf of a client that has disconnected.

There is no way for one goroutine to terminate another directly as it would leave all its shared variables in undefined states. Hence, need a reliable mechanism to broadcast an event over a channel so that many goroutines can see it as it occurs and can later see that it has occurred.

After a channel has been closed and drained of all sent values, subsequent receive operations proceed immediately and yield zero values. Can exploit this to create a broadcast mechanism i.e. don't send a value on the channel, close it.

```go
var done = make(chan struct{})

func cancelled() bool {
    select {
    case <-done:
        return true
    default:
        return false
    }
}

// Cancel traversal when input is detected.
go func() {
    os.Stdin.Read(make([]byte, 1)) // read a single byte
    close(done)
}()

// in goroutine to respond to the cancellation
// must first drain the fileSizes channel
for {
    select {
    case <-done:
        // Drain fileSizes to allow existing goroutines to finish.
        for range fileSizes {
            // Do nothing.
        }
        return
    case size, ok := <-fileSizes:
        // ...
    }
}
```
