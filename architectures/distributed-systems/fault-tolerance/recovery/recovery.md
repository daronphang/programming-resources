## Recovery

A recovery from error is to replace an erroneous state with an error-free state. There are two forms:

- **Backward recovery**: Bringing the system back into a previously correct state (checkpoint)
- **Forward recovery**: Bringing the system to a correct new state from which it can continue to execute

By and large, backward error recovery techniques are widely applied as a general mechanism for recovering from failures in distributed systems. The major benefit of backward error recovery is that it is a generally applicable method independent of any specific system or process.

However, backward error recovery also introduces some problems. First, restoring a system or process to a previous state is generally a relatively costly operation in terms of performance.

Second, because backward error recovery mechanisms are independent of the distributed application for which they are actually used, no guarantees can be given that once recovery has taken place, the same or similar failure will not happen again.

Finally, although backward error recovery requires checkpointing, some states can simply never be rolled back to i.e. irreversible.

## Implementation

Upon recovery, we assume that a process is aware that it has crashed and recovered. A recovery event should be automatically generated, and it should retrieve the relevant state of the process from stable storage (log) before processing of other events is resumed.
