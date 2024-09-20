## Go runtime

Of all the things the Go runtime does for you, spawning and managing goroutines is probably the most beneficial to you and your software.

### Fair scheduling

Fair scheduling is a naive strategy that evenly distributes the load between all available processors. In the fair scheduling strategy, for n processors and x tasks, each processor would get x/n tasks. However, there are problems with this approach:

- Tasks that are dependent on each other will likely cause one of the processors to be underutilized
- Can lead to poor cache locality for tasks that require the same data but are scheduled on different processors

### Work stealing

Go handles multiplexing goroutines onto OS threads, and uses an algorithm known as work stealing strategy. Go follows a fork-join model for concurrency. Forks are when goroutines are started, and join points are when two or more goroutines are synchronized through channels or types in the sync package.

The work stealing algorithm follows a few basic rules. Given a thread of execution:

1. Each processor owns its own thread and deque
2. At a fork point, add tasks to the tail of the deque associated with the thread
3. If the thread is idle, **steal work from the head of deque** associated with some other random thread
4. At a join point that cannot be realized yet (i.e., the goroutine it is synchronized with has not completed yet), **pop work off the tail** of the thread’s own deque
5. If the thread’s deque is empty, either stall at a join, or repeat step 3

From the above, a thread of execution both pushes and pops from the tail of its work deque. The work sitting on the tail has a couple of interesting properties:

- It is the work most likely needed to complete the parent's join, resulting in better performance and keeping fewer things in memory
- It is the work most likely to still be in processor's cache, resulting in fewer cache misses

### Stealing continuations

Go’s work-stealing algorithm enqueues and steals continuations. Stealing continuations are considered to be theoretically superior to stealing tasks, and therefore it is best to queue the continuation and not the goroutine. Continuation stealing also works support from the compiler, which Go supports.

### GOMAXPROCS

GOMAXPROCS setting controls how many contexts are available for use by the runtime. The default setting is for there to be **one context per logical CPU** on the host machine. Unlike contexts, there may be more or less OS threads than cores to help Go’s runtime manage things like garbage collection and goroutines.

There is an important guarantee in the runtime that there will always be at least enough OS threads available to handle hosting every context. This allows the runtime to make an important optimization. The runtime also contains a thread pool for threads that aren’t currently being utilized.
