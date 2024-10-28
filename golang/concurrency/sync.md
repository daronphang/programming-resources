## Sync package

The sync package contains the concurrency primitives that are most useful for low-level **memory access synchronization**. It will be up to you to decide when memory access synchronization is appropriate.

## WaitGroup

WaitGroup is a great way to wait for a set of concurrent operations to complete when you either don’t care about the result of the concurrent operation, or you have other means of collecting their results.

```go
var wg sync.WaitGroup

wg.Add(1)
go func() {
    defer wg.Done()
    fmt.Println("1st goroutine sleeping...")
    time.Sleep(1)
}()

wg.Add(1)
go func() {
    defer wg.Done()
    fmt.Println("2nd goroutine sleeping...")
    time.Sleep(2)
}()

wg.Wait()
fmt.Println("All goroutines complete.")
```

## Mutex (mutual exclusion)

Go allows us to run code concurrently using goroutines, which can be used to communicate for synchronization. However, when we don't need communication, and when concurrent processes access the same piece of data, it can lead to race conditions.

Mutexes are data structures provided by the sync package. They can help to place a lock on different sections of data so that only one goroutine can access it at a time. It is a way to guard critical sections of your program.

Nonetheless, although mutex helps to solve data race, it doesn't solve race conditions i.e. the order of operations in the program is still non-deterministic. Also, introducing locks can create maintenance and performance problems i.e. **synchronizing access is expensive**. It is highly recommended to constraint memory access synchronization only to **critical sections**.

```go
func main() {
	n := 0
	var m sync.Mutex

	// now, both goroutines call m.Lock() before accessing `n`
	// and call m.Unlock once they are done
	go func() {
		m.Lock()
		defer m.Unlock()
		nIsEven := isEven(n)
		time.Sleep(5 * time.Millisecond)
		if nIsEven {
			fmt.Println(n, " is even")
			return
		}
		fmt.Println(n, "is odd")
	}()

	go func() {
		m.Lock()
		n++
		m.Unlock()
	}()

	time.Sleep(time.Second)
}
```

## RWMutex

Critical sections are so named because they reflect a bottleneck in your program. It is somewhat expensive to enter and exit a critical section, and so generally people attempt to minimize the time spent in critical sections.

One strategy for doing so is to **reduce the cross-section of the critical section**. There may be memory that needs to be shared between multiple concurrent processes, but perhaps not all of these processes will read and write to this memory. If this is the case, you can take advantage of a different type of mutex: sync.RWMutex.

RWMutex is conceptually the same thing as a Mutex, but it gives you more control over the memory. You can request a lock for reading, in which case you will be granted access unless the lock is being held for writing.

## Cond

Cond is a rendezvous point for goroutines waiting for or announcing the occurrence of an event. An “event” is any arbitrary signal between two or more goroutines that carries no information other than the fact that it has occurred. Very often you’ll want to wait for one of these signals before continuing execution on a goroutine.

### Without Cond

Inefficient and artificially degrading performance. If sleep is too short, you are unnecessarily consuming too much CPU.

```go
for conditionTrue() == false {
    time.Sleep(1*time.Millisecond)
}
```

### With Cond

Allows goroutine to efficiently sleep until it is signaled to wake and check its condition. The call to Wait() doesn't just block, but suspends the current goroutine, allowing other goroutines to run on the OS thread.

```go
c := sync.NewCond(&sync.Mutex{})
c.L.Lock()
for conditionTrue() == false {
    c.Wait()
}
c.L.Unlock()
```

## Once

Counts the number of times Do() is called.

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

## Pool

Pool is a concurrent-safe implementation of the object pool pattern. At a high level, a the pool pattern is a way to create and make available a fixed number, or pool, of things for use. It’s commonly used to constrain the creation of things that are expensive (e.g., database connections) so that only a fixed number of them are ever created, but an indeterminate number of operations can still request access to these things.

Pool is used instead of instantiating objects as you go because Go has a garbage collector, and instantiated objects will be automatically cleaned up once they are not referenced.

Another common situation where a Pool is useful is for warming a cache of pre-allocated objects for operations that must run as quickly as possible. Instead of trying to guard the host machine’s memory by constraining the number of objects created, we’re trying to guard consumers’ time by front-loading the time it takes to get a reference to another object. This is very common when writing high- throughput network servers that attempt to respond to requests as quickly as possible.

### Get, Put

When called, Get will first check whether there are any available instances within the pool to return to the caller. If not, it creates a new one. When finished, callers call Put() to place the instance they were working with back in the pool for use by other processes.

```go
myPool := &sync.Pool{
    New: func() interface{} {
        fmt.Println("Creating new instance.")
        return struct{}{}
    },
}

myPool.Get()
instance := myPool.Get()
myPool.Put(instance)
myPool.Get()
```

### Tips

When working with pool, the following pointers are helpful:

- When instantiating sync.Pool, give it a New member variable that is thread-safe
- When you receive an instance from Get(), make no assumptions regarding the state of the object received
- Make sure to call Put() when you are finished with the object you pulled out of the pool
- Objects in the pool must be roughly uniform in makeup
