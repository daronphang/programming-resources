## Mutex (mutual exclusion)

Go allows us to run code concurrently using goroutines, which can be used to communicate for synchronization. However, when we don't need communication, and when concurrent processes access the same piece of data, it can lead to race conditions.

Mutexes are data structures provided by the sync package. They can help to place a lock on different sections of data so that only one goroutine can access it at a time.

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
