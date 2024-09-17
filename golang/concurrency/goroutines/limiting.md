## Controlling/limiting goroutines

```go
maxGoroutines := 10
guard := make(chan bool, maxGoroutines)
guard <- true
go func() {
  h.handleSenderMsg(ctx, msg)
  <- guard
}()
```
