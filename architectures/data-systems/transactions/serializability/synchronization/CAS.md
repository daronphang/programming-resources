## CAS (Compare and Swap)

CAS is primarily used by multiple multi-threaded languages for implementing thread-safe operations in multi-threaded or parallel computing environments to prevent race conditions and ensure data consistency.

This operation is used to implement synchronization primitives including semaphores, mutexes, lock-free and wait-free algorithms.

### How it works

CAS compares the content of a memory location with a given value, and if they are the same, modifies the contents of the memory location to a new given value.

This is done as a **single atomic** operation. The atomicity guarantees that the new value is calculated based on up-to-date information; if the value had been updated by another thread in the meantime, the write would fail.

### Pseudo code

```
function cas(p: pointer to int, old: int, new: int) is
    if *p ≠ old
        return false

    *p ← new

    return true
```
