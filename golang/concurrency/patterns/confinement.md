## Confinement

When working with concurrent code, there are a few different options for safe operation:

- Synchronization primitives for sharing memory e.g. sync.Mutex
- Synchronization via communicating e.g. channels
- Immutable data (implicit)
- Data protected by confinement

Confinement is the simple idea of ensuring information is only ever available from one concurrent process. When this is achieved, a concurrent program is implicitly safe and no synchronization is needed. Confinement can also allow for a lighter cognitive load on the developer and smaller critical sections. There are two kinds of confinement possible: adhoc and lexical.

### Adhoc

Adhoc confinement is when you achieve confinement through a convention e.g. codebase you work within, group you work within, etc. However, this is difficult to achieve on projects of any size unless you have tools to perform static analysis on your code every time someone commits some code.

```go
data := make([]int, 4)
loopData := func(handleData chan<- int) {
    defer close(handleData)
    for i := range data {
        handleData <- data[i]
    }
}

handleData := make(chan int)
go loopData(handleData)

for num := range handleData {
    fmt.Println(num)
}
```

### Lexical

Lexical confinement involves using lexical scope to expose only the correct data and concurrency primitives for multiple concurrent processes to use. It makes it impossible to do the wrong thing.

```go
chanOwner := func() <-chan int {
     results := make(chan int, 5)
     go func() {
        defer close(results)
        for i := 0; i <= 5; i++ {
            results <- i
        }
    }()
return results
}

consumer := func(results <-chan int) {
    for result := range results {
        fmt.Printf("Received: %d\n", result)
    }
    fmt.Println("Done receiving!")
}

results := chanOwner()
consumer(results)
```
