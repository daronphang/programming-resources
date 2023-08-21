## Priorities

Every thread has a priority. By default, it inherits the priority of the thread that constructed it. You can increase or decrease with setPriority().

When the thread scheduler has a chance to pick a new thread, it prefers thread with higher priority. However, thread priorities are **highly system dependent** i.e. Java thread priorities are mapped to the priority levels of the host platform. Windows has seven priority levels, while Linux does not have thread priorities i.e. all threads have the same priority.

```
1   MIN_PRIORITY
5   NORM_PRIORITY
10  MAX_PRIORITY
```

## Daemon

You can turn a thread into a daemon. A daemon is a thread that has no other roles except to provide a service i.e. timer threads, cleanup threads. When only daemon threads remain, the VM exits i.e. daemon threads shutdown when the program exits.

**Daemon threads should never access a persistent resource such as a file or database** since it can terminate at any time.

```java
t.setDaemon(true);
```

## Handlers for Uncaught Exceptions

The run() of a thread cannot throw any checked exceptions, but it can be terminated by an unchecked exception. However, there is no catch clause to which the exception can be propagated. Instead, just before the thread dies, the exception is passed to a handler for uncaught exceptions. 

The handler must belong to a class that implements the Thread.UncaughtExceptionHandler interface which has a single method.

You can install a handler (default is null) into any thread with:
- setUncaughtExceptionHandler()
- setDefaultUncaughtExceptionHandler()

```java
public interface UncaughtExceptionHandler {
    void uncaughtException(Thread t, Throwable e)
}
```