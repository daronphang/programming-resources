## Race conditions

Sprinkling sleeps throughout your code can help to debug concurrent programs, but they are not a solution, and introduce inefficiencies. Instead, you should always target logical correctness.

Race conditions are one of the most insidious types of concurrency bugs because they may not show up until years after the code has been placed into production. They are usually precipitated by a change in the environment the code is executing in, or an unprecedented occurrence.

## Deadlocks

A deadlocked program is one in which all concurrent processes are waiting on one another. In this state, the program will never recover without outside intervention.

```go
type value struct {
    mu    sync.Mutex
    value int
}

var wg sync.WaitGroup

printSum := func(v1, v2 *value) {
    defer wg.Done()
    v1.mu.Lock()
    defer v1.mu.Unlock()

    time.Sleep(2*time.Second)

    v2.mu.Lock()
    defer v2.mu.Unlock()
    fmt.Printf("sum=%v\n", v1.value + v2.value)
}
var a, b value
wg.Add(2)
go printSum(&a, &b)
go printSum(&b, &a)
wg.Wait()
```

### Coffman conditions

Coffman conditions outline the conditions that must be present for deadlocks to arise. They are the basis for techniques that help detect, prevent and correct deadlocks:

- **Mutual exclusion**: A concurrent process holds exclusive rights to a resource at any one time
- **Wait for condition**: A concurrent process must simultaneously hold a resource and be waiting for an additional resource
- **No preemption**: A resource held by a concurrent process can only be released by that process
- **Circular wait**: A concurrent process (P1) must be waiting on a chain of other concurrent processes (P2), which are in turn waiting on it (P1)

## Livelocks

Livelocks are programs that are actively performing concurrent operations, but these operations do nothing to move the state of the program forward.

Livelocks can happen when two or more concurrent processes attempt to prevent a deadlock without coordination. Livelocks are a subset of a larger set of problems called starvation.

```go
cadence := sync.NewCond(&sync.Mutex{})
go func() {
    for range time.Tick(1*time.Millisecond) {
        cadence.Broadcast()
    }
}()

takeStep := func() {
    cadence.L.Lock()
    cadence.Wait()
    cadence.L.Unlock()
}

tryDir := func(dirName string, dir *int32, out *bytes.Buffer) bool {
    fmt.Fprintf(out, " %v", dirName)
    atomic.AddInt32(dir, 1)
    takeStep()
    if atomic.LoadInt32(dir) == 1 {
        fmt.Fprint(out, ". Success!")
        return true
    }
    takeStep()
    atomic.AddInt32(dir, -1)
    return false
}

var left, right int32
tryLeft := func(out *bytes.Buffer) bool {
    return tryDir("left", &left, out)
}
tryRight := func(out *bytes.Buffer) bool {
    return tryDir("right", &right, out)
}

walk := func(walking *sync.WaitGroup, name string) {
    var out bytes.Buffer
    defer func() { fmt.Println(out.String()) }()
    defer walking.Done()
    fmt.Fprintf(&out, "%v is trying to scoot:", name)
    for i := 0; i < 5; i++ {
        if tryLeft(&out) || tryRight(&out) {
            return
        }
    }
    fmt.Fprintf(&out, "\n%v tosses her hands up in exasperation!", name)

}
var peopleInHallway sync.WaitGroup
peopleInHallway.Add(2)
go walk(&peopleInHallway, "Alice")
go walk(&peopleInHallway, "Barbara")
peopleInHallway.Wait()

//  Alice is trying to scoot: left right left right left right left right left right
// Alice tosses her hands up in exasperation!
// Barbara is trying to scoot: left right left right left right left right left right
//Barbara tosses her hands up in exasperation!
```

## Starvation

Starvation is any situation where a concurrent process cannot get all the resources it needs to perform work.

Starvation usually implies that there are one or more greedy concurrent process that are unfairly preventing one or more concurrent processes from accomplishing work as efficiently as possible, or maybe at all.

A metric is a useful technique for identifying starvation. One of the ways you can detect and solve starvation is by logging when work is accomplished, and then determining if your rate of work is as high as you expect it.

Starvation can also apply to CPU, memory, file handles, database connections: **any resource that must be shared is a candidate for starvation**.

```go
// greedy worker hols onto the shared lock for the entirety of its work loop
// polite worker attempts to lock when it needs to

var wg sync.WaitGroup
var sharedLock sync.Mutex
const runtime = 1*time.Second

greedyWorker := func() {
    defer wg.Done()
    var count int
    for begin := time.Now(); time.Since(begin) <= runtime; {
        sharedLock.Lock()
        time.Sleep(3*time.Nanosecond)
        sharedLock.Unlock()
        count++
    }
    fmt.Printf("Greedy worker was able to execute %v work loops\n", count)

}
politeWorker := func() {
    defer wg.Done()
    var count int
    for begin := time.Now(); time.Since(begin) <= runtime; {
        sharedLock.Lock()
        time.Sleep(1*time.Nanosecond)
        sharedLock.Unlock()
        sharedLock.Lock()
        time.Sleep(1*time.Nanosecond)
        sharedLock.Unlock()
        sharedLock.Lock()
        time.Sleep(1*time.Nanosecond)
        sharedLock.Unlock()

        count++
    }
    fmt.Printf("Polite worker was able to execute %v work loops\n", count)
}

wg.Add(2)
go greedyWorker()
go politeWorker()
wg.Wait()

// Polite worker was able to execute 289777 work loops
// Greedy worker was able to execute 471287 work loops
```
