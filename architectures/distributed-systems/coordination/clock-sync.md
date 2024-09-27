## Clock synchronization

Strongly related to communication between processes is the issue of how processes in distributed systems synchronize. Synchronization is all about doing the right thing at the right time.

In a distributed system, achieving agreement on time is not trivial. When each machine has its own clock, an event that occurred after another event may nevertheless be assigned an earlier time. Having an accurate time is needed in application domains including financial brokerage, security auditing, collaborative sensing, etc.

## Physical clocks

Nearly all computers often have several circuits for keeping track of time, and these devices are known as timers. A computer timer is usually a precisely machined quartz crystal. It can run slightly faster or slower than others, depending on manufacturing differences and the external temperature. The rate at which a clock runs is also called **clock drift**. In contrast, the difference between two clocks at a specific point in time is referred to as **clock skew**.

As quartz clocks drift, they need to be synced periodically with machines that have access to higher accuracy clocks e.g. atomic clocks. NTP can also be used to synchronize clocks.

With a single computer and a single clock, all processes will be internally consistent as they use the same clock. However, as multiple CPUs are introduced, each with its own clock, the situation changes radically. Nonetheless, the basis for keeping global time is a called **Coordinated Universal Time, or UTC**. UTC receivers are commercially available, and many computers are equipped with one.

## Logical clocks

A logical clock measures the passing of time in terms of logical operations, not wall-clock time. The simplest possible logical clock is a counter, which is incremented before an operation is executed. Doing so ensures that each operation has a distinct logical timestamp. If two operations execute on the same process, then necessarily one must come before the other, and their logical timestamps will reflect that.

### Lamport clocks

Knowing the absolute time is often not necessary. What counts is that related events at different processes happen in the correct order. Every process in the system has its own local logical clock implemented with a numerical counter that follows specific rules:

- The counter is initialized with 0
- The process increments its counter before executing an operation
- When the process sends a message, it increments its counter and sends a copy of it in the message
- When the process receives a message, its counter is updated to 1 plus the maximum of its current logical timestamp and the message’s timestamp

### Vector clocks

A vector clock is a logical clock that guarantees that if two operations can be ordered by their logical timestamps, then one must have happened-before the other. A vector clock is implemented with an array of counters, one for each process in the system. And similarly to how Lamport clocks are used, each process has its own local copy of the clock.

The beauty of vector clock timestamps is that they can be partially ordered.

## Clock synchronization algorithms

### Network Time Protocol (NTP)

A common approach in many protocols, is to let clients contact a timeserver. However, message delays will have outdated the reported time.

In the case of NTP, this protocol is set up pairwise between servers. In other words, B will also probe A for its current time.

The challenge is to do so despite the unpredictable latencies introduced by the network. A NTP client estimates the clock skew by correcting the timestamp received by a NTP server with the estimated network latency. Armed with an estimate of the clock skew, the client can adjust its clock, causing it to jump forward or back- ward in time.
