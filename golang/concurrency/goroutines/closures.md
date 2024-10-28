## Closures

Goroutines execute within the same address space they were created in.

### Looping

As goroutines being scheduled may run at any point in time in the future, it is undetermined what values will be used from within the goroutine. There is also a high probability the loop will exit before the goroutines begin.

```go
// goroutines accessing the value that is transferred to a heap holding
// a reference to the last value
var wg sync.WaitGroup
for _, salutation := range []string{"hello", "greetings", "good day"} {
    wg.Add(1)
    go func() {
        defer wg.Done()
        fmt.Println(salutation)
    }()
}
wg.Wait()

// good day
// good day
// good day
```

Instead, the proper way to write a loop is to pass a copy of the variable into the closure so that by the time the goroutine runs, it will be operating on the data from its iteration of the loop.

```go
var wg sync.WaitGroup
for _, salutation := range []string{"hello", "greetings", "good day"} {
    wg.Add(1)
    go func(salutation string) {
        defer wg.Done()
        fmt.Println(salutation)
    }(salutation)
}
wg.Wait()
```
