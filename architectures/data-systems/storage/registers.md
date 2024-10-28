## Shared storage in a distributed system

Shared memory in distributed data systems encapsulate data storage functionality accessible by read and write operations from processes. The memory abstractions are called **registers** as they resemble those provided by multi-processor machines at the hardware level.

Register specifications and algorithms is useful when implementing networked storage systems, distributed file systems, and shared working spaces for collaborative work.

## Registers

Registers store values and can be accessed through two operations: read and write. The processes in the system use registers for communicating with each other and for storing information.

A process interacts with a register abstraction through events. After a process has invoked an operation (i.e. triggering an event), the register abstraction may trigger an event that carries the reply from the operation. Each correct process accesses the registers in a sequential manner, which means that after a process has invoked an operation on a register, the process does not invoke any further operation on that register until the previous operation completes.

### Failures

If we assume that processes might fail, we can no longer require that any process who invokes an operation eventually completes that operation. For example, a process might crash right after invoking an operation and may not have the time to complete this operation.

### Concurrency

When multiple processes access a register in practice, executions are most often not serial. There are three register abstractions handling this:

- **Safe**: A safe register may return an arbitrary value when a write is concurrently ongoing
- **Regular**: Ensures a minimal guarantee in the face of concurrent or failed operations, and may only return the previous value or the newly written value
- **Atomic**: Strongest and provides a strict form of consistency even in the face of concurrency and failures
