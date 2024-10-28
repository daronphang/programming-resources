## Pipelines

A pipeline is just another tool you can use to form an abstraction in your system. In particular, it is a very powerful tool to use when your program needs to process streams, or batches of data.

A pipeline is nothing more than a series of things that take data in, perform an operation on it, and pass the data back out. We call each of these operations a stage of the pipeline.

By using a pipeline, you separate the concerns of each stage, which provides numerous benefits. You can modify stages independent of one another, you can mix and match how stages are combined independent of modifying the stages, you can process each stage concurrent to upstream or downstream stages, and you can fan-out, or rate-limit portions of your pipeline.

## Channels

Channels are uniquely suited to constructing pipelines in Go because they fulfill all of our basic requirements. They can receive and emit values, they can safely be used concurrently, they can be ranged over, and they are reified by the language.

## Fan-Out, Fan-In

Sometimes, stages in your pipeline can be particularly computationally expensive. When this happens, upstream stages in your pipeline can become blocked while waiting for your expensive stages to complete.

One of the interesting properties of pipelines is the ability they give you to operate on the stream of data using a combination of separate, often re-orderable stages.

Fan-out is a term to describe the process of starting multiple goroutines to handle input from the pipeline, and fan-in is a term to describe the process of combining multiple results into one channel.

You might consider this pattern if both of the following apply:

1. It doesn't rely on values that the stage has calculated before
2. It takes a long time to run

## Or-done channel

Sometimes you will be working with channels from disparate parts of your system, and the code you are working with may be canceled via its done channel.

```go
orDone := func(done, c <-chan interface{}) <-chan interface{} {
    valStream := make(chan interface{})
    go func() {
        defer close(valStream)
        for {
            select {
            case <-done:
                return
            case v, ok := <-c:
                if !ok {
                    return
                }
                select {
                case valStream <-v:
                case <-done:
                }
            }
        }
    }()
    return valStream
}
```

```go
for val := range orDone(done, myChan) {
    // do something with val
}
```

## Bridge channel

In some circumstances, you may find yourself wanting to consume values from a sequence of channels.

```go
<-chan <-chan interface{}
```

As a consumer, the code may not care about the fact that its values come from a sequence of channels. In that case, dealing with a channel of channels can be cumbersome. If we instead define a function that can destructure the channel of channels into a simple channel (bridging channel), this will make it much easier for the consumer to focus on the problem at hand.

```go
bridge := func(
    done <-chan interface{},
    chanStream <-chan <-chan interface{},
) <-chan interface{} {
    valStream := make(chan interface{})
    go func() {
        defer close(valStream)
        for {
            var stream <-chan interface{}
            select {
            case <-done:
                return
            case maybeStream, ok := <-chanStream:
                if !ok {
                    return
                }
                stream = maybeStream
            }

            for val := range orDone(done, stream) {
                select {
                case <-done:
                case valStream <-val:
                }
            }
        }
    }()
    return valStream
}
```

```go
genVals := func() <-chan <-chan interface{} {
    chanStream := make(chan (<-chan interface{}))
    go func(){
        defer close(chanStream)
        for i := 0; i < 10; i++ {
            stream := make(chan interface{}, 1)
            stream <- i
            close(stream)
            chanStream <- stream
        }
    }()
    return chanStream
}

for v := range bridge(nil, genVals()) {
    fmt.Printf("%v ", v)
}
// 0 1 2 3 4 5 6 7 8 9
```

## Queuing

While introducing queuing into your system is very useful, it’s usually one of the last techniques you want to employ when optimizing your program. Adding queuing prematurely can hide synchronization issues such as deadlocks and livelocks.

The utility of introducing a queue isn't that the runtime of one of the stages has been reduced, but rather that the **time it is in a blocking state is reduced**. This allows the stage to continue doing its job.

Queuing can increase the overall performance of the system:

- If batching requests in a stage saves time
- If delays in a stage produce a negative feedback loop into the system

Queuing should be implemented either:

- At the entrance to your pipeline
- In stages where batching will lead to higher efficiency

Queuing can be useful in your system, but because of its complexity, it’s usually one of the last optimizations I would suggest implementing.
