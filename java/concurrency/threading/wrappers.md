## Runnable

A Runnable encapsulates a task that runs asynchronously i.e. no parameters and no return value.

```java
public interface Runnable {
    void run();
}
```

## Callables

A Callable is similar to a Runnable, but it returns a value.

```java
public interface Callable<V> {
    V call() throws Exception;
}
```

## Futures

A Future holds the result of an asynchronous computation. The owner of the Future object can obtain the result when it is ready.

**The get() blocks until the computation is finished**. You can cancel the computation with cancel(). If it has not yet started, it is canceled and will never start. If it is currently in progress, it is interrupted if the mayInterrupt parameter is True.

```java
public interface Future<V> {
    V get() throws ...;
    V get(long timeout, TimeUnit unit) throws ...;
    void cancel(boolean myInterrupt);
    boolean isCancelled();
    boolean isDone();
}
```

### FutureTask

The FutureTask wrapper is a convenient mechanism for turning a Callable into both a Future and a Runnable by implementing both interfaces.

```java
Callable<Integer> myComputation = ...;
FutureTask<Integer> task = new FutureTask<Integer>(myComputation);
Thread t = new Thread(task);
ArrayList<Future<Integer>> futures = new ArrayList();
futures.add(t.start());

for (Future<Integer> future : futures) {
    Integer result = future.get();
}
```

## Executors

Constructing a new thread is somewhat expensive as it involves interaction with the OS. If your program creates a **large number of short-lived threads**, you should use a **thread pool** instead.

A thread pool contains a number of idle threads that are ready to run. You provide a Runnable to the pool, and one of the threads call run(). When the run() exits, the thread doesn't die but is returned to the Executor to serve the next request.

Another reason to use a thread pool is to throttle the number of concurrent threads. **Creating a huge number of threads can greatly degrade performance and even crash the VM**.

| Method                           | Description                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------ |
| newCachedThreadPool              | New threads are created as needed; idle threads are kept for 60 seconds        |
| newFixedThreadPool               | The pool contains a fixed set of threads; idle threads are kept indefinitely   |
| newSingleThreadExecutor          | A pool with a single thread that executes the submitted tasks sequentially     |
| newScheduledThreadPool           | A fixed-thread pool for scheduled execution; a replacement for java.util.Timer |
| newSingleThreadScheduledExecutor | A single-thread pool for scheduled execution                                   |

### Thread Pools

The newCachedThreadPool, newFixedThreadPool and newSingleThreadExecutor returns an object of the ThreadPoolExecutor class that implements the ExecutorService interface.

For newFixedThreadPool, if more tasks are submitted than there are idle threads, the unserved tasks are placed on a queue.

**When you are done with a thread pool, call shutdown()**. This method initiates the shutdown sequence for the pool and kills all threads in it. To cancel tasks that have not yet begun, call shutdownNow().

```java
public interface ExecutorService {
    Future<?> submit(Runnable task) // returns null upon completion
    Future<T> submit(Runnable task, T result)
    Future<T> submit(Callable<T> task)
    void shutdown()
    void shutdownNow()
}
```

### Scheduled Execution

The ScheduledExecutorService interface has methods for scheduled or repeated execution of tasks. It is a generalization of java.util.Timer that allows for thread pooling.

You can schedule a Runnable or Callable to run once, after an initial delay. You can also schedule it to run periodically.

```java
public interface ScheduledExecutorService {
    ScheduledFuture<V> schedule(Callable<V> task, long time, TimeUnit unit)
    ScheduledFuture<?> schedule(Runnable task, long time, TimeUnit unit)
    ScheduledFuture<?> scheduleAtFixedRate(Runnable task, long initialDelay, long period, TimeUnit unit)
    ScheduledFuture<?> scheduleWithFixedDelay(Runnable task, long initialDelay, long delay, TimeUnit unit)
}
```

#### Controlling Groups of Tasks

Sometimes, an executor is used for a more tactical reason, to control a group of related tasks i.e. cancelling all tasks in an executor.

#### invokeAny

The invokeAny() submits all objects in a collection of Callable objects and returns the result of a completed task that finished the most quickly.

#### invokeAll

The invokeAll() submits all objects in a collection of Callable objects, blocks until all of them are complete, and returns a list of Future objects that represent solutions to all tasks.

```java
List<Callable<T>> tasks = ...;
List<Future<T>> results = executor.invokeAll(tasks);
for (Future<T> result : results) {
    processFurther(result.get());
}
```

#### ExecutorCompletionService

If you do not want to wait for all tasks to complete, you can obtain the results in the order in which they are available. This can be arranged with the ExecutorCompletionService.

The service manages a blocking queue of Future objects, containing the results of the submitted tasks as they become available.

```java
ExecutorCompletionService<T> service = new ExecutorCompletionService(executor);
for (Callable<T> task : tasks) {
    service.submit(task);
}
for (int i = 0; i < tasks.size(); i++) {
    processFurther(service.take().get();)
}
```

## ForkJoin

The fork-join framework is designed to support recursive computation across multiple processor cores i.e. combinining return values from different threads processing subtasks into one for image/video processing. For instance, if we want to count how many elements of an array fulfill a particular property, we can cut the array in half, compute the results, and add them up.

The framework uses an effective heuristic for balancing the workload among available threads, called **work stealing**. Each worker thread has a deque (double-ended queue) for tasks. A worker thread pushes subtasks onto the head of its own deque. Only one thread accesses the head, so no locking is required. When a worker thread is idle, it 'steals' a task from the tail of another deque.

To put the recursive computation in a form that is usable by the framework, supply a class that extends:

- `RecursiveTask<T>` if it produces a result of type T
- RecursiveAction if it returns null

Override the compute() to generate and invoke subtasks, and to combine their results. To get the current result, use join(). Though get() can also return the result, it is less attractive as it can throw checked exceptions that we are not allowed to throw in compute().

```java
class Counter extends RecursiveTask<Integer> {
    . . .
    protected Integer compute(){
        if (to - from < THRESHOLD) {
            // solve problem directly
        }
        else {
            int mid = (from + to) / 2;
            Counter first = new Counter(values, from, mid, filter);
            Counter second = new Counter(values, mid, to, filter);
            invokeAll(first, second);
            return first.join() + second.join();
        }
    }
}
```

## Completable Futures

The traditional approach for dealing with nonblocking calls is to use event handlers, where the programmer registers a handler for the action that should occur after a task completes.

The CompletableFuture class provides an alternative approach. Unlike event handlers, completable futures can be **composed**. With Completable futures, you just specify what you want to have done and in which order.

When an exception is thrown in a CompletableFuture, it is captured and wrapped in an ExecutionException when get() is called. If get() is not called, use &**handle()**. It is called with both the result (null if none) and the exception (null if none).

```java
public static List<URL> getLinks(String page) {}
public void CompletableFuture<String> readPage(URL url) {}

CompletableFuture<String> contents = readPage(url);
CompletableFuture<List<URL>> links = contents.thenApply(Parser::getLinks);
```

### Adding an Action to CompletableFuture Object

| Method       | Parameter                 | Description                                                        |
| ------------ | ------------------------- | ------------------------------------------------------------------ |
| thenApply    | T -> U                    | Nonblocking, applies a function to the result                      |
| thenCompose  | T -> CompletableFuture<U> | Invokes the function on the result and execute the returned future |
| handle       | (T, Throwable) -> U       | Processes the result or error                                      |
| thenAccept   | T -> void                 | Like thenApply, but with void result                               |
| whenComplete | (T, Throwable) -> void    | Like handle, but with void result                                  |
| thenRun      | Runnable                  | Executes the Runnable with void result                             |

### Combining Multiple Composition Objects

| Method         | Parameter                           | Description                                                         |
| -------------- | ----------------------------------- | ------------------------------------------------------------------- |
| thenCombine    | CompletableFuture<U>, (T,U) -> V    | Executes both in parallel and combine the results                   |
| thenAcceptBoth | CompletableFuture<U>, (T,U) -> void | Like thenCombine, but with void result                              |
| runAfterBoth   | CompletableFuture<?>, Runnable      | Executes the runnable after both complete                           |
| applyToEither  | CompletableFuture<T>, T -> V        | When a result is available on either, pass it to the given function |
| acceptEither   | CompletableFuture<T>, t -> void     | Like applyToEither, but with void result                            |
| runAfterEither | CompletableFuture<?>, Runnable      | Executes the runnable after either completes                        |
| static allOf   | CompletableFuture<?>...             | Complete with void result after all given futures complete          |
| static anyOf   | CompletableFuture<?>...             | Complete with void result after any of the given futures completes  |
