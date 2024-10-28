## Problems in distributed systems

A wide range of problems can occur in distributed systems, including:

- Single point of failure
- Packets sent over the unreliable network may be lost or arbitrarily delayed
- Node's clock may be significantly out of sync with other nodes (despite best efforts to set up NTP)
- Process may pause for a substantial amount of time at any point in its execution (stop-the-world garbage collector), be declared dead by other nodes, and then come back to life again without realizing it was paused
- Program crashing due to programming error
- Slow processes due to memory leaks or unavailable resources (threads)
- Cascading failures
- Unexpected load

## Fault tolerance

Fault tolerance is the ability of a software system to maintain its functionality and performance **in the presence of faults**. Faults are any deviations from the expected or desired behavior of the system, such as errors, exceptions, or anomalies. A fault-tolerant system can detect, isolate, and correct faults, or at least tolerate them without compromising the system's integrity or availability.

Being fault tolerant is strongly related to what are called **dependable systems**. Dependability is a term that covers a number of useful requirements for distributed systems:

- **Availability**: Property that a system is ready to be used immediately
- **Reliability**: Property that a system can run continuously without failure
- **Safety**: When a system temporarily fails, no catastrophic event happens
- **Maintainability**: How easily a failed system can be repaired

### Metrics

Traditionally, fault-tolerance has been related to the following three metrics:

- **Mean Time to Failure (MTTF)**: The average time until a component fails
- **Mean Time to Repair (MTTR)**: The average time needed to repair a component
- **Mean Time Between Failures (MTBF)**: MTTF + MTTR

### Classifications

- **Transient fault**: Occurs once and then disappears i.e. not repeatable
- **Intermittent fault**: Occurs, vanishes, and then reappears
- **Permanent fault**: Continues to exist until the faulty component is replaced

## Dealing with faults

### Detecting

To tolerance faults, first step is to detect them, but even that is hard. Most systems don't have an accurate mechanism of detecting whether a node has failed, so most distributed algorithms rely on timeouts to determine whether a remote node is still available. However, **timeouts cannot distinguish between network and node failures.**

Once a fault is detected, making a system tolerate is not easy as there is no global variable, shared memory, common knowledge or any kind of shared state between nodes. Major decisions cannot be safely made by a single node, and hence, require protocols that enlist help from other nodes i.e. get a quorum to agree.

### Planning

Partial failures preclude **relying on the successful execution of a remote service**. If such reliability cannot be guaranteed, it is then best to always perform only local executions, leading to the **copy-before-use** principle.

According to this principle, data can be accessed only after they have been transferred to the machine of the process wanting that data. Moreover, modifying a data item should not be done. Instead, it can only be updated to a new version.
