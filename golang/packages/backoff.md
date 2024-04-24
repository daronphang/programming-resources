## Backoff

```go

func main() {
    b := backoff.NewExponentialBackoff()
    b.RandomizationFactor = 0
    b.InitialInterval = 2 * time.Second
    b.MaxElapsedTime = 10 * time.Second

    if err := backoff.Retry(operation, b); err != nil {
        // handle error
        return nil
    }
}

func operation() error {
    // Cannot pass arguments here.
    return nil
}
```
