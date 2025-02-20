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

## Multiple subscribers

```go
func main() {
	ch := make(chan int, 100)
	for i := range 100 {
		ch <- i
	}

	go test("goroutine1", ch)
	go test("goroutine2", ch)
	time.Sleep(3 * time.Second)
}

func test(name string, ch chan int) {
	for v := range ch {
		fmt.Println("%v: %v", name, v)
	}
}
```
