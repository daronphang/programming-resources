## Multithreaded computation

A multithreaded computation is composed of a set of threads, each of which is a sequential ordering of unit-time instructions. The instructions are connected by dependency edges, which provide a partial ordering on which instructions must execute before which other instructions.

During the course of its execution, **a thread may create/spawn other threads**. Unlike a subroutine call, the spawning thread can operate **concurrently** with the spawned thread. Threads are organized into a spawn tree with root and leaf threads.

## Processes and threads

A process is an executing program. An OS uses processes to separate the applications that are being executed.

A thread is the basic unit to which an OS allocates processor time. Each thread has a scheduling priority and maintains a set of structures the system uses to save the thread context when the thread's execution is paused.

Multiple threads can run in the context of a process. All threads of a process share its virtual address space. A thread can execute any part of the program code, including parts currently being executed by another thread.

A primary thread can create/spawn additional threads to execute code in parallel or concurrently with the primary thread. These threads are often called **worker threads**. Worker threads are threads that perform background tasks on the order of its client i.e. gets activated on clients' requests.
