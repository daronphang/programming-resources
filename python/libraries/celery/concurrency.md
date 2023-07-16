## Celery Worker

When you start a celery worker, you start a supervisor process. The celery worker itself does not process any tasks. It spawns child processes/threads and deals with all the book keeping stuff. The child processes (also known as **execution pool**) execute the actual tasks.

https://distributedpython.com/posts/celery-execution-pools-what-is-it-all-about/

## -pool

You can choose between processes or threads, using the --pool argument. Celery supports four execution pool implementations:

- prefork (default)
- solo
- eventlet
- gevent

```console
$ celery worker --app=worker.app --pool=gevent --concurrency=100
```

## --concurrency

Determines the number of processes/threads based on your pool option. For prefork pools, the number of processes should not exceed the number of CPUs.

If not set, Celery defaults to the number of CPUs, whatever the execution pool.

## Prefork

The prefork is based on Python's multiprocessing package. It allows your worker to side-step Python's GIL and fully leverage multiple processors on a given machine.

You want to use prefork pool if your tasks are CPU bound. The number of available cores limits the number of concurrent processes.

## Solo

Solo pool is neither threaded nor process-based. The solo pool runs inside the worker process, and runs inline which means there is no book-keeping overhead. However, it blocks the worker while it executes tasks.

```console
celery worker --app=worker.app --pool=solo
```

## Eventlet and Gevent

Celery supports Eventlet as an alternative execution pool implementation and in some cases, superior to prefork. CPU-bound operations don't generally go well with Eventlet.

The prefork pool can take use of multiple processes, but how many is often limited to a few processes per CPU. With Eventlet, you can spawn hundreds or thousands of green threads. This is one of the applications async I/O that is good at asynchronous HTTP requests.

### Greenlets (Green Threads)

Greenlets give you threads, but without using threads. Threads are managed by the OS kernel which uses a general-purpose scheduler to switch between threads. However, this scheduler is not always efficient.

Greenlets emulate multi-threaded environments without relying on any native OS capabilities. Greenlets are managed in the **application space and not in kernel space**. There is no scheduler pre-emptively swtiching between your threads; instead, greenlets voluntarily/explicitly give up control to one another at specified points in your code.

### Running

Need to pip install gevent or eventlet. Both options are based on the same concept of spawning a greenlet pool. Gevent uses the gevent greenlet pool, while eventlet uses eventlet greenlet pool.

```console
$ ~$ celery worker --app=worker.app --pool=gevent --concurreny=500
```

```console
$ celery -A proj worker -P eventlet -c 1000
```

## Conclusion

You may want to mix of both Eventlet and prefork workers, and route tasks according to compatibility of what works best. There is even evidence to support that **having multiple worker instances running, may perform better than having a single worker** i.e. 3 workers with 10 pool porcesses each.

You need to experiment to find the numbers that work bests for you, as this varies on application, work load, task run times and other factors.
