## Threading

Threading is one of the most well-known approaches to attaining Python concurrency and parallelism. Threading is a feature provided by OS. Threading's job is to enable applications to be more responsive to user input. Perfect for I/O operations such as web scraping as the processor is sitting idle waiting for data from a remote source. Hence, the processor can download from different data sources in parallel and combine them at the end.

A thread is a separate flow of execution i.e. multiple things happening at once. However, because the implementation of CPython with GIL (Global Interpreter Lock) that limits one Python thread to run at a time, getting multiple tasks to run simultaneously requires a non-standard implementation of Python. Threads written in C have the ability to release GIL and run concurrently.

Tasks that spend much of their time waiting for external events i.e. I/O bound, are good candidates for threading. Threads allow you to perform long-running background tasks without stopping the main thread from continuing to service network packets or GUI events. However, for long-running tasks, should run on different machine (distributing to multiple workers) rather than spinning up sub-processes or threads on the same machine that will degrade performance of application.

## Global Interpreter Lock (GIL)

The primary reason for the GIL’s existence is CPython’s memory management (CPython is the interpreter and compiler of Python) and its internal data structures. The GIL ensures that only one thread executes Python bytecode at a time, preventing concurrent access to these data structures, which could result in inconsistent states and memory corruption. Without the GIL, developers would have to manage the complexities of fine-grained locking manually, making Python code more prone to subtle concurrency bugs.

GIL prevents two threads from running at the same time in Python i.e. 8 cores changed to 8 threads is the same as using 1 CPU. An added precaution in Python as threads share the same memory space and hence, multiple threads may write to the same memory at the same time.

GIL effectively locks any shared data structures whenever it is being used and releases when job is completed. GIL is necessary as Python isn't thread-safe and Python wasn't designed considering computers have more than 1 CPU.

However, this is not the only negative effect of the GIL. The GIL introduces overhead from **context switching** that makes multi-threaded programs slower.

Nonetheless, GIL is only taken when **running pure Python code**, and in many cases is completely released and not even checked.

GIL does not prevent the following operations from running in parallel:

- IO operations i.e. sending/receiving network data, reading/writing to file
- Heavy built-in CPU bound operations i.e. hashing, compressing
- Some C extension operations

### Threading and GIL

To acquire the GIL, a thread first checks whether some other thread holds the GIL. Otherwise, it waits until the GIL is released. It waits for a fixed time interval called the **switch interval** (5 ms by default).

If the GIL is not released during that time, it sets two flags:

- eval_breaker: Tells the GIL-holding thread to suspend bytecode execution
- gil_drop_request: Reason for GIL request

The GIL-holding thread sees the flags when it starts the next iteration of the evaluation loop and releases the GIL. It notifies the GIL-awaiting threads, and one of them acquires the GIL. It's up to the OS to decide which thread to wake up, so it may or may not be the thread that set the flags.

## Thead safety checklist

- Global variables are either read-only or have access properly controlled (using locks)
- Each request gets its own database connection
- Any request that does multiple SQL operations need to consider whether those operations produce "race conditions" i.e. checking if something exists in table and inserting if it doesn't exist is not "thread-safe"

## Highlights

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
