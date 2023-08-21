## Threading

Threading is one of the most well-known approaches to attaining Python concurrency and parallelism. Threading is a feature provided by OS. Threading's job is to enable applications to be more responsive to user input. Perfect for I/O operations such as web scraping as the processor is sitting idle waiting for data from a remote source. Hence, the processor can download from different data sources in parallel and combine them at the end.

A thread is a separate flow of execution i.e. multiple things happening at once. However, because the implementation of CPython with GIL (Global Interpreter Lock) that limits one Python thread to run at a time, getting multiple tasks to run simultaneously requires a non-standard implementation of Python. Threads written in C have the ability to release GIL and run concurrently.

Tasks that spend much of their time waiting for external events i.e. I/O bound, are good candidates for threading. Threads allow you to perform long-running background tasks without stopping the main thread from continuing to service network packets or GUI events. However, for long-running tasks, should run on different machine (distributing to multiple workers) rather than spinning up sub-processes or threads on the same machine that will degrade performance of application.

### Global Interpreter Lock

GIL prevents two threads from running at the same time in Python i.e. 8 cores changed to 8 threads is the same as using 1 CPU. An added precaution in Python as threads share the same memory space and hence, multiple threads may write to the same memory at the same time.

GIL effectively locks any shared data structures whenever it is being used and releases when job is completed. GIL is necessary as Python isn't thread-safe and Python wasn't designed considering computers have more than 1 CPU.

### Thead Safety Checklist

- Global variables are either read-only or have access properly controlled (using locks)
- Each request gets its own database connection
- Any request that does multiple SQL operations need to consider whether those operations produce "race conditions" i.e. checking if something exists in table and inserting if it doesn't exist is not "thread-safe"

### Highlights

- Context switches are cheap as it has lesser overhead and same program is being executed so there is no swapping pages in and out of memory
- Lighter than processes as threads share same memory space and has more flexible software design
- Allows server to save computation time as it is cheaper to start a thread than to compile and run a program
- Allows to retain values between web requests
- Multiple threads can exist in a single process
- Harder to program as they can interfere with one another
- Increases complexity of program which can make debugging more difficult

## Example

Consider a web browser program Chrome that is launched and a window appears: that is a process. A process is a program that is running with memory and data structures allocated in that memory. When a second tab is opened and another webpage is loading, you can still continue to browse on the first tab: web browser is paying attention to you and loading a page, which is only possible with threads.

### Flask/Apache

For Flask, it uses one thread in development mode, but deployed applications can use multiple threads. For web servers like Apache, it is multi-threaded. Structure involves a listener that listens on port, grab incoming web requests and place them on work queue. Various worker threads then grab requests and perform the work.
