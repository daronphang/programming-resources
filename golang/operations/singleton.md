## Singleton pattern

### Not threadsafe

```go
type singleton struct {}
var instance *singleton

func newInstance() *singleton {
    if instance == nil {
        instance = &singleton{}
    }
    return instance
}
```

### Threadsafe

```go
type singleton struct {}
var instance *singleton
var lock = &sync.Mutex{}

func newInstance() *singleton {
    lock.Lock()
    defer lock.Unlock()
    if instance == nil {
        instance = &singleton{}
    }
    return instance
}
```

### Atomic

```go
type singleton struct {}
var instance *singleton
var once sync.Once

func newInstance() *singleton {
    once.Do(func() {
        instance = &singleton{}
    })
    return instance
}
```
