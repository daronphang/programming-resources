## Clock synchronization

Strongly related to communication between processes is the issue of how processes in distributed systems synchronize. Synchronization is all about doing the right thing at the right time.

In a distributed system, achieving agreement on time is not trivial. When each machine has its own clock, an event that occurred after another event may nevertheless be assigned an earlier time. Having an accurate time is needed in application domains including financial brokerage, security auditing, collaborative sensing, etc.

## Physical clocks

Nearly all computers often have several circuits for keeping track of time, and these devices are known as timers. A computer timer is usually a precisely machined quartz crystal.

With a single computer and a single clock, all processes will be internally consistent as they use the same clock.

However, as multiple CPUs are introduced, each with its own clock, the situation changes radically. Nonetheless, the basis for keeping global time is a called **Coordinated Universal Time, or UTC**. UTC receivers are commercially available, and many computers are equipped with one.

## Clock synchronization algorithms

### Network Time Protocol (NTP)

A common approach in many protocols, is to let clients contact a timeserver. However, message delays will have outdated the reported time.

In the case of NTP, this protocol is set up pairwise between servers. In other words, B will also probe A for its current time.

## Logical clocks

### Lamport

Knowing the absolute time is often not necessary. What counts is that related events at different processes happen in the correct order.
