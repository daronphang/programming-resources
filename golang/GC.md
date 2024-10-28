## Garbage collector

Go automatically manages the allocation of variables and includes the garbage collector that automatically recycles memory as needed weaknesses. Identify parts of memory that are no longer needed.

### Memory management

Memory is allocated more efficiently based on the lexical scope in which it’s created:

- Variables are placed on the memory stack
- If the compiler can't determine the exact lifespan of a variable, it is placed in the heap, where memory is dynamically allocated

### Objectives

The primary role of the garbage collector is to identify and reclaim memory specifically from these dynamic allocations:

- Automatically free up memory from unreachable objects, preventing memory leaks
- Minimize memory management errors, such as use-after-free and dangling pointers
- Operate concurrently with the program, reducing pause times
- Abstract away the complexities of manual memory management for developers
- Ensure efficient memory management with minimal overhead

### Resources

The GC has to balance between using the computer’s processor (CPU) and its storage (memory).

The memory used includes the currently active memory, any new memory added before the marking step, and space for some extra details (metadata).

The CPU use has two parts: one fixed part for running the GC and another part that changes based on how much memory is active.

### Parameters

To balance the trade-off between the two main variables, you can adjust the cyclic frequency of the GC and set a threshold for when the GC should start working:

- **GOGC**: Determines the target heap size after each GC cycle
- **GOMEMLIMIT**: Runtime memory limit

When the heap becomes too large, it can lead to an increase in GC cycles, resulting in high CPU usage and a potential program stall. By doubling GOGC, you will double the heap memory overhead and roughly halve the CPU cost of the GC.

```
Target heap memory = Live heap + (Live heap + GC roots) × GOGC/100
```
