## Concurrency Defense Principles

### Single Responsibility Principle

SRP states that a given method/class/component should have a single reason to change. Concurrency design is complex enough to be a reason to change in it's own right and hence, deserves to be separated from the rest of the code.

Few things to consider for concurrency-related code:

- Has its own life cycle of development, change and tuning
- Has its own challenges which are different and more difficult than nonconcurrency-related code
- Keep it separate from other code

### Limit the Scope of Data

Two threads modifying a field of a shared object can cause unexpected behavior. One solution is to lock to protect a critical section in the code that uses the shared object.

### Threads Should Be as Independent as Possible

Consider writing your threaded code such that each thread exists in its own world, sharing no data with any other thread. Each thread processes one client request, with all of its required data coming from an unshared source and stored as local variables.

### Keep Synchronized/Lock Sections Small

Sections of code guarded by lock are guaranteed to have only one thread executing through them at any given time. Locks are expensive because they create delays and add overhead.

### Think About Shutdown Early

Graceful shutdown can be hard to get correct. Common problems involve deadlock, with threads waiting for a signal to continue that never comes.

For example, a parent thread spawning child threads and waits for them all to finish before it releases its resources and shutdown. If one of the child thread is deadlocked, the parent will wait forever, and the system never shuts down.

## Terminologies

### Bound Resources

Resources of a fixed size or number used in a concurrent environment i.e. database connections, read/write buffers.

### Mutual Exclusion

Only one thread can access shared data or a shared resource at a time.

### Starvation

One thread or a group of threads is prohibited from proceeding for an excessively long time.

### Deadlock

Two or more threads waiting for each other to finish. Each thread has a resource that the other thread requires and neither can finish until it gets the other resource.

### Livelock

Threads in lockstep, each trying to do work but finding another 'in the way'.

## Execution Models

### Producer-Consumer

Producer threads create work and place it in a buffer or queue. Consumer threads acquire that work from the queue and complete it. The **queue becomes a bound resource**.

Producers must wait for queue to have space and consumers must wait until there is something in the queue.

### Readers-Writers

When you have a shared resource that primarily serves as a source of information for readers, but which is occasionally updated by writers, **throughput is an issue**.

Coordinating readers so they do not read something a writer is updating and vice versa is a tough balancing act. Writers tend to block many readers for a period of time.

The challenge is to balance the needs of both readers and writers to satisfy correct operation, provide reasonable output and avoide starvation.

## Testing

### Get your nonthreaded code working first

Make sure code works outside of its use in threads. Do not try to chase down nonthreading bugs and threading bugs at the same time.

### Treat spurious failures as candidate threading issues

Threaded code causes things to fail that 'simply cannot fail'. Bugs in threaded code might exhibit their symptoms once in a thousand executions. Attempts to repeat the systems can be frustrating. This often leads developers to write off the failure as a hardware glitch or one-off.

### Make your threaded code pluggable

Write the concurrency-supporting code such that it can be run in several configurations i.e. varied number of threads.

### Make your threaded code tunable

Getting the right balance of threads typically requires trial and error. find ways to time the performance of your system under different configurations.

### Run with more threads than processors

Things happen when the system switches between tasks. To encourage task swapping, run with more threads than processors or cores. The more frequently your tasks swap, the more likely you will encounter code that is missing a critical section or causes deadlock.

### Run on different platforms

Run your threaded code on all target platforms early and often.

### Instrument your code to try and force failures

Increase the chances of catching rare and sporadic failure occurrences by adding methods such as sleep(), wait(), etc. that affect the order of execution.
