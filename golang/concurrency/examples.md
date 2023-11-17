## Unbuffered

```go
package main

import (
  "fmt"
  "time"
)

func access(ch chan int) {
  time.Sleep(time.Second)
  fmt.Println("start accessing channel\n")

  for i := range ch {
    fmt.Println(i)
    time.Sleep(time.Second)
  }
}

func main() {
  ch := make(chan int)
  defer close(ch)

  go access(ch)

  for i := 0; i < 9; i++ {
    ch <- i
    fmt.Println("Filled")
  }

  time.Sleep(3 * time.Second)
}

// start accessing channel
// 0
// Filled
// 1
// Filled
```

## Buffered

```go
package main

import (
  "fmt"
  "log"
  "math/rand"
  "sync"
  "time"
)

func main() {
  ch := make(chan order, 3) // buffered with max of 3 in queue

  wg := &sync.WaitGroup{}
  wg.Add(2)

  go func() {
    defer wg.Done()
    worker("Candier", ch)
  }()

  go func() {
    defer wg.Done()
    worker("Stringer", ch)
  }()

  for i := 0; i < 10; i++ {
    waitForOrders()
    o := order(i)
    log.Printf("Partier: I %v, I will pass it to the channel\n", o)
    ch <- o
  }

  log.Println("No more orders, closing the channel to signify workers to stop")
  close(ch)

  log.Println("Wait for workers to gracefully stop")
  wg.Wait()

  log.Println("All done")
}

func waitForOrders() {
  processingTime := time.Duration(rand.Intn(2)) * time.Second
  time.Sleep(processingTime)
}

func worker(name string, ch <-chan order) {
  for o := range ch {
    log.Printf("%s: I got %v, I will process it\n", name, o)
    processOrder(o)
    log.Printf("%s: I completed %v, I'm ready to take a new order\n", name, o)
  }
  log.Printf("%s: I'm done\n", name)
}

func processOrder(_ order) {
  processingTime := time.Duration(2+rand.Intn(2)) * time.Second
  time.Sleep(processingTime)
}

type order int

func (o order) String() string {
  return fmt.Sprintf("order-%02d", o)
}
```

## Looping in Parallel

Problems that consist of subproblems that are completely independent of each other are described as "embarassingly parallel". These problems are the easiest kind to implement concurrently and enjoy performance that scales linearly with the amount of parallelism.

There is no direct way to wait until a goroutine has finished, but we can change the inner goroutine to report its completion to the outer goroutine by sending an event on a shared channel.

```go
// makeThumbnails makes thumbnails of the specified files
// takes a set of full-size images and produces thumbnail-size images
// order doesn't matter

func makeThumbnails(filenames []string) {
    for _, f := range filenames {
        if _, err := thumbnail.ImageFile(f); err != nil {
            log.Println(err)
        }
    }
}

func makeThumbnails2(filenames []string) {
    ch := make(chan struct{})

    for _, f := range filenames {
        // value of f is passed as an explicit argument
        // this is to avoid reading the same value in inner goroutines
        go func(f string) {
            thumbnail.ImageFile(f) // NOTE: ignoring errors
            ch <- struct{}{}
        }(f)
    }

    // waits for goroutines to complete
    // since we know there are len(filenames) inner goroutines,
    // the outer goroutine need only to count that many events before it returns
    for range filenames {
        <-ch
    }
}

// uses a buffered channel to return the names of generated image files
// or an error if any step failed
func makeThumbnails5(filenames []string) (thumbfiles []string, err error) {
    type item struct {
        thumbfile string
        err
        error
    }

    ch := make(chan item, len(filenames))

    for _, f := range filenames {
        go func(f string) {
            var it item
            it.thumbfile, it.err = thumbnail.ImageFile(f)
            ch <- it
        }(f)
    }
    for range filenames {
        it := <-ch
        if it.err != nil {
            return nil, it.err
        }
        thumbfiles = append(thumbfiles, it.thumbfile)
    }
    return thumbfiles, nil
}
```
