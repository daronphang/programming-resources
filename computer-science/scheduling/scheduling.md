## Scheduling

For efficient execution of a dynamically growing multithreaded computation on a MIMD-style parallel computer, a scheduling algorithm must simultaneously ensure that:

- **Enough threads are active concurrently to keep the processors busy**
- **Number of concurrently active threads remains within reasonable limits** so that memory requirements are not unduly large

Moreover, the scheduler should also try to maintain related threads on the same processor, if possible, so that communication between them can be minimized. Achieving all these goals simultaneously can be difficult.

Tasks are stored in queues belonging to threads. Once a thread finishes executing a given task, it takes a new one from the queue. However, some threads can have their queues empty.

Two scheduling paradigms are work sharing and work stealing. Their purposes are to redistribute work when performing distributed computations, minimize resource starvation and ensure faireness amongst the parties utilizing the resources.

### Work Sharing

In work sharing, whenever a processor generates new threads, the scheduler attempts to migrate some of them to other processors in hopes of distributing the work to underutilized processors. All threads share the same working queue.

### Work Stealing

In work stealing, underutilized processors take the initiative of stealing threads from other processors. Intuitively, the migration of threads occurs less frequently with work stealing than with work sharing, since when all processors have to work to do, no threads are migrated by a work-stealing scheduler, but threads are always migrated to a work-sharing scheduler.

The advantage of work stealing algorithms is that the overhead of load balancing (finding idle processors) is performed on the idle processor itself, and not by busy processors.
