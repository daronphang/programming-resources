## Resilience by process groups

The key approach to tolerating a faulty process is to organize several identical processes into a **group**. The key property that all groups have is that when a message is sent to the group itself, all members of the group receive it. In this way, if one process in a group fails, hopefully some other process can take over for it.

Process groups may be dynamic. New groups can be created, and old groups can be destroyed. A process can join a group or leave one during system operation. A process can be a member of several groups at the same time. Consequently, mechanisms are required for managing groups and group membership.

The purpose of introducing groups is to allow a process to deal with collections of other processes as a single abstraction. Thus, a process P can send a message to a group Q of servers without having to know who they are, how many there are, or where they are.

### Group organization

An important distinction between different groups has to do with their internal structure:

- **Flat group**: All processes are equal, there is no distinctive leader and all decisions are made collectively
- **Hierarchical group**: One process is the coordinator and all others are workers

### Membership management

When group communication is present, some method is required for creating and deleting groups, as well as for allowing processes to join and leave groups.

One possible approach is to have a **group server** to which all these requests can be sent. The group server can then maintain a complete database of all the groups and their exact membership. This method is straightforward, efficient, and fairly easy to implement. Unfortunately, it shares a major disadvantage with many (physically) centralized solutions: a single point of failure. If the group server crashes, group management ceases to exist. Probably most or all groups will have to be reconstructed from scratch, possibly terminating whatever work was going on.

Another approach is to manage group membership in a **distributed way**. For example, if reliable multicasting is available, an outsider can send a message to all group members announcing its wish to join the group. To leave a group, a member just sends a goodbye message to everyone. However, when a process crashes, there is no polite announcement. Other members have to discover this experimentally by noticing that the crashed member no longer responds to anything.

An issue with membership management is that leaving and joining have to be **synchronous** with data messages being sent. This means that starting at the instant when a process has joined a group, it must receive all messages sent to that group. Similarly, as soon as a process has left the group, it must not receive any more messages, and other members must not receive messages from it. One way of making sure that a join or leave is integrated into the message stream at the right place is to convert this operation into a **sequence of messages** (message queue) sent to the whole group.

## Failure masking and replication

Process groups are part of the solution for building fault-tolerant systems. In particular, having a group of identical processes allows us to mask one or more faulty processes in that group. In other words, we can replicate processes and organize them into a group to replace a single (vulnerable) process with a (fault tolerant) group.

There are two approaches to replication:

- Primary-based (leader)
- Replicated-write (leaderless)

An important issue with using process groups to tolerate faults is how much replication is needed. For a system to be k-fault tolerant:

- Crash failures: 2k + 1 processes is needed
- Arbitrary failures: 3k + 1 processes is needed

## Consensus in faulty systems with crash failures

In a fault-tolerant process group, each nonfaulty process executes the same commands, in the same order, as every other nonfaulty process. This means that the group members need to reach **consensus** on which command to execute.

### Raft

Raft is a consensus protocol that operates under crash-failure semantics. It was developed in reaction to the inherent intricacies of Paxos.
