## Threads

Like a process, a thread executes its own piece of code, independently of other threads. However, no attempt is made to achieve a high degree of concurrency transparency if this would result in performance degradation.

Therefore, a thread system generally maintains only the minimum information to allow a CPU to be shared by several threads. In particular, a **thread context** often consists of nothing more than the processor context, along with some other information for thread management. For example, a thread system may keep track of the fact that a thread is currently blocked on a mutex variable, so as not to select it for execution. For this reason, protecting data against inappropriate access by threads within a single process is left entirely to application developers.

There are a few implications of deploying threads:

- The performance of multi-threaded application often leads to a performance gain compared to single-threaded counterpart
- Development requires additional effort as threads are not automatically protected against each other the way processes are
- It becomes possible to exploit parallelism when executing the program on a multi-processor or multi-core system i.e. each thread is assigned to a different CPU/core
- It can provide a convenient means of allowing blocking system calls without blocking the entire process in which the thread is running i.e. useful for blocking I/O operations
