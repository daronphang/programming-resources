## Concurrency

Concurrent programming refers to the expression of a program as a composition of several autonomous activities to hide latency of I/O operations and to exploit modern computer's many processors.

Before Go, if you wanted to write concurrent code, you would:

- Model your program in threads and synchronize the access to memory between them
- Create a thread pool and multiplexed your operations onto the thread pool if your machine couldn't handle that many threads

GO enables two styles of concurrent programming. First style is goroutines and channels, which support communicating sequential processes (CSP) in which values are passed between independent activities. Second is traditional model of shared memory multithreading.

### Concurrency vs parallelism

The difference between concurrency and parallelism turns out to be a very powerful abstraction when modeling your code, and Go takes full advantage of this.

Concurrency is a property of the code, while parallelism is a property of the running program. A program may appear running in parallel, but they are executing in a sequential manner faster than is distinguishable.

This reveals a few important things:

- We do not write parallel code, **only concurrent code that we hope will be run in parallel**
- It is possible to be ignorant of whether our concurrent code is actually running in parallel, made possible by the layers of abstraction that lie beneath our program's model e.g. OS, runtime, CPU, containers, etc.
- Parallelism is a function of time or context

## Communicating sequential processes (CSP)

CSP is a concurrency model used for managing and coordinating multiple concurrent tasks or processes. CSP is based on the concept of processes that communicate with each other through channels, allowing them to synchronize and exchange data. This model is particularly well-supported in Go through its goroutines and channels.

Go’s philosophy on concurrency can be summed up as follows:

- Aim for simplicity
- Use channels when possible
- Treat goroutines like a free resource i.e. cheap and easy to create

### How this helps you

It is common for languages to end their chain of abstraction at the level of the OS thread and memory access synchronization. Go takes a different route and supplants this with the concept of goroutines and channels.

Goroutines free us from having to think about our problem space in terms of parallelism and instead **allow us to model problems closer to their natural level of concurrency**.

For instance, if we want to build a web server, we would need to consider the following that does not directly concern the problem we are trying to solve:

- Does my language naturally support threads, or do I need to pick a library?
- Where should my thread confinement boundaries be?
- How heavy are threads in the OS?
- Should I create a pool of workers to constrain the number of threads I create? How do I find this optimal number?

A more natural mapping to the problem space is an **enormous benefit**. Go's runtime automatically handles multiplexing concurrent operations onto operating system threads, and manages their scheduling for us. This means that optimizations to the runtime can be made without us having to change how we’ve modeled our problem.

Also, because Go's runtime manages the scheduling of goroutines, it can introspect on things like goroutines blocked waiting for I/O and intelligently reallocate OS threads to goroutines that are not blocked. This **increases the performance** of your code.

## Timeouts

Reasons why we want our concurrent processes to support timeouts:

- System saturation i.e. its ability to process requests is at capacity
- Stale data
- Attempting to prevent deadlocks

## Cancellation

Reasons why our concurrent processes might be canceled:

- Timeouts
- User intervention
- Parent cancellation
- Replicated requests i.e. data is sent to multiple processes in an attempt to get a faster response from one of them
