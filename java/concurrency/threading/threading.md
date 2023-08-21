## Threading

```java
public interface Runnable {
    void run();
}

Runnable r = () = > {};
Thread t = new Thread(r);
t.start();
```

### States

To get the current state, call getState().

#### New

Created with the new operator. In this state, the program has not started executing code. A certain bookkeeping needs to be done before a thread can run.

#### Runnable

Once you invoke start(), the thread is in runnable state. However, it is up to the OS to give the thread time to run. A runnable thread may or may not be running at any given time (state is runnable and not running).

Once a thread is running, it doesn't necessarily keep running. It is desirable that running threads occasionally pause so that other threads have a chance to run. **Preemptive scheduling** give each runnable thread a slice of time to perform its task. 

All modern desktop and server OS use preemptive scheduling. However, small devices such as cell phones may use **cooperative scheduling**. In such a device, a thread loses control only when it call yield(), or when it is blocked or waiting.

#### Blocked, Waiting, Timed Waiting

When a thread is blocked or waiting, it is temporarily inactive. It doesn't execute any code and consumes minimal resources. A thread can reach this state:
- When the thread tries to acquire an intrinsic object lock that is currently held by another thread (but not a Lock in the java.util.concurrent library), it enters **blocked** state. Once other threads have relinquished the lock, the thread becomes runnable
- When the thread waits for another thread to notify the scheduler of a condition, it enters **waiting** state. This happens by calling Object.wait() or Thread.join(), or by waiting for a Lock or Condition in the java.util.concurrent library
- When a method has a timeout parameter, the thread enters **timed waiting** state. This state persists either until the timeout expires or the appropriate notification is received

#### Terminated

A thread is terminated for one of the following reasons:
- It dies a natural death because run() exits normally
- It dies abruptly because an uncaught exception terminates run()

## Interrupting Threads

A thread terminates when its run method returns or if an exception occurs, and there is no way to force a thread to terminate. 

However, interrupt() can be used to request termination of a thread. When called on a thread, the interrupted status of the thread is set which is a boolean flag. Each thread should occasionally check whether it has been interrupted.

Nonetheless, there is no requirement that a thread which is interrupted should terminate. Interrupting a thread simply grabs its attention, which can then decide how to react to the interruption.

When interrupt() is called on a thread that blocks on a call such as **sleep() or wait(), the blocking call is terminated by an InterruptedException**. Hence, you should catch this exception and not check on the interrupted status.

```java
while (!Thread.currentThread().isInterrupted() && more work to do) {
    do more work
}
```

### interrupted() vs isInterrupted()

The interrupted() is a static method that checks whether the current thread has been interrupted and clears the status of the thread. The isInterrupted() does not change the status.

## Deprecated stop() and suspend()

The stop() and suspend() methods are deprecated. 