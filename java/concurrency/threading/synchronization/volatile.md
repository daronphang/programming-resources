## Volatile Fields

With modern processors and compilers, a couple of things may happen that leaves room for error:

- Computers with multiple processors can temporarily hold memory values in registers or local memory caches; threads running in different processors may see different values for the same memory address
- Compilers can reorder instructions for maximum throughput by making the assumption that memory values are only changed when there are explicit instructions in the code; however, a memory value can be changed by another thread

If you use locks to protect code that can be accessed by multiple threads, you won't have these problems. **Compilers are required to respect locks by flushing local caches as necessary and not inappropriately reordering instructions**.

The volatile keyword offers a lock-free mechanism for synchronizing access to an **instance field**. If you use synchronized keyword on a field, it can block other threads from reading it if it is locked.

If you declare a field as volatile, the compiler and VM take into account that the field may be concurrently updated by another thread. The compiler will then insert the appropriate code to ensure that a change to the instance field in one thread is visible from other threads that read the variable.

```java
private volatile boolean done;
public boolean isDone() {
    return done;
}

public void setDone() {
    done = true;
}
```

### Atomicity

Volatile fields **do not provide atomicity** as there is no guarantee that the reading/writing is uninterrupted. Hence, **you should not perform any other operations other than assignment**.

## Final

You can use final keyword to guarantee that other threads will see the same value of the instance field i.e. makes it safe to access a shared field.
