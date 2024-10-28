## Cancellation

Sometimes may need to instruct goroutine to stop what it is doing i.e. web server performing computation on behalf of a client that has disconnected.

There is no way for one goroutine to terminate another directly as it would leave all its shared variables in undefined states. Hence, need a reliable mechanism to broadcast an event over a channel so that many goroutines can see it as it occurs and can later see that it has occurred.

After a channel has been closed and drained of all sent values, subsequent receive operations proceed immediately and yield zero values. Can exploit this to create a broadcast mechanism i.e. **don't send a value on the channel, close it**.

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

```go
func main() {
	ch := make(chan int, 0)

	go func() {
		for {
			select {
				case i, ok := <- ch:
				if !ok {
					fmt.Println("channel closed")
					return
				}
				fmt.Printf("received: %v \n", i)
			}
		}
	}()

	for i := range 10 {
		ch <- i
		if i == 3 {
			close(ch)
			break
		}
	}
	time.Sleep(1)
}

// received: 0
// received: 1
// received: 2
// received: 3
// channel closed
```
