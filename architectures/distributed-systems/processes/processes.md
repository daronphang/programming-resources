## Processes

Processes play a crucial role in distributed systems.

To execute a program, an OS creates a number of **virtual processors**, each one for running a different program. To keep track of these virtual processors, the OS has a **process table**, containing entries to store CPU register values, memory maps, open files, accounting information, privileges, etc. Jointly, these entries form a **process context**.

A process is often defined as a program in execution i.e. a program that is currently being executed on one of the OS’ virtual processors. An important advantage is that the OS takes great care to ensure that independent processes **cannot maliciously or inadvertently affect** the correctness of each other’s behavior i.e. **each process works in its own data space**. Multiple processes may be concurrently sharing the same CPU and other hardware resources is made transparent. Usually, the OS requires hardware support to enforce this separation.

This concurrency transparency comes at a price:

- Each time a process is created, the OS must create a complete independent address space
- Switching the CPU between two processes may require some effort
- The OS will also have to modify registers of the **Memory Management Unit (MMU)** and invalidate address translation caches, such as in the **Translation Lookaside Buffer (TLB)**
- If the OS supports more processes than it can simultaneously hold in main memory, it may have to swap processes between main memory and disk before the actual switch can take place
