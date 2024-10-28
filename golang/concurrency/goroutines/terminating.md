## Terminating goroutines

The goroutine has a few paths to termination:

- When it has completed its work
- When it cannot continue its work due to an unrecoverable error
- When it is told to stop working

There is no programmatic way for one goroutine to stop another other than by returning from main or exiting the program. However, there are ways to communicate with a goroutine to request that it stop itself.

### Program termination

If the main function (or the main goroutine) ends and the program exits, any remaining goroutines are terminated abruptly. The Go runtime will stop all goroutines when the main function completes and the program is about to exit. This is because the entire process ends, so all goroutines are stopped.

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
