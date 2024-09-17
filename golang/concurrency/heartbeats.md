## Heartbeats

There are a few different reasons heartbeats are interesting for concurrent code:

- They allow us insights into our system
- They can make testing the system deterministic when it might otherwise not be i.e. not having to rely on a longer timeout

There are two types of heartbeats that can be implemented:

- Heartbeats that occur on a time interval: Useful for concurrent code that might be waiting for something else to happen for it to process a unit of work
- Heartbeats that occur at the beginning of a unit of work: Useful for writing tests

Heartbeats aren’t strictly necessary when writing concurrent code. Nonetheless, for any long-running goroutines, or goroutines that need to be tested, this pattern is recommended.

```go
doWork := func(
    done <-chan interface{},
    pulseInterval time.Duration,
) (<-chan interface{}, <-chan time.Time) {
    heartbeat := make(chan interface{})
    results := make(chan time.Time)
    go func() {
        defer close(heartbeat)
        defer close(results)

        pulse := time.Tick(pulseInterval)
        workGen := time.Tick(2*pulseInterval)

        sendPulse := func() {
            select {
            case heartbeat <-struct{}{}:
            default:
            }
        }
        sendResult := func(r time.Time) {
            for {
                select {
                case <-done:
                    return
                case <-pulse:
                    sendPulse()
                case results <- r:
                return
                }
            }
        }
        for {
            select {
            case <-done:
                return
            case <-pulse:
                sendPulse()
            case r := <-workGen:
                sendResult(r)
            }
        }
    }()
    return heartbeat, results
}


done := make(chan interface{})
time.AfterFunc(10*time.Second, func() { close(done) })

const timeout = 2*time.Second
heartbeat, results := doWork(done, timeout/2)
for {
    select {
    case _, ok := <-heartbeat:
        if !ok {
            return
        }
        fmt.Println("pulse")
    case r, ok := <-results:
        if !ok {
            return
        }
        fmt.Printf("results %v\n", r.Second())
    case <-time.After(timeout):
        return
    }
}
```
