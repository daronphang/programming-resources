## Distributed transactions and consensus

Multiple nodes work together to maintain data consistency and provide fault tolerance. However, nodes can experience failures, network delays, and partitions, which can lead to data inconsistencies.

Consensus algorithms allow a collection of machines to work as a coherent group that can survive the failures of some of its members. Because of this, they play a key role in building reliable large-scale software systems.

### State machines

Consensus algorithms typically arise in the context of **replicated state machines** i.e. identical copies of the same state on different servers. They are used to solve a variety of fault tolerance problems in distributed systems.

Large scale systems that have a single cluster leader such as GFS, HDFS, RAMCloud, typically use a **separate replicated state machine** (Chubby, Zookeeper) to manage leader election and store configuration information that must survive during leader crashes.

Replicated state machines are typically implemented using a replicated log. Since the state machines are deterministic, each server computes the same state and the same sequence of outputs.

Keeping the replicated log consistent is the job of the consensus algorithm. It communicates with the consensus modules on other servers to ensure that every log eventually contains the same requests in the same order, even if some servers fail.

## Features

### Agreement

Consensus algorithms aim to achieve agreement among a group of nodes regarding a single value or a sequence of operations. All nodes in the system should eventually agree on the same decision.

### Mutual exclusion

A group of servers ensuring mutually exclusive access to a critical resource.

### Fault tolerance

Consensus algorithms are designed to handle node failures, communication delays, and network partitions. They ensure that the system can continue to make progress even in the presence of failures.

### Safety

Consensus algorithms ensure safety by guaranteeing that only one value or decision is agreed upon i.e. **never returns an incorrect result under all non-Byzantine conditions including network delays, partitions, packet loss, duplication, and reordering**. Conflicting decisions are prevented to maintain data consistency.

### Liveness

Liveness ensures that the system can make progress and continue to agree on new values or decisions even in the absence of failures, as long as the majority of servers are operational and can communicate with each other.

### Quorum

Many consensus algorithms require a quorum, which is a majority of nodes, to agree on a value before it is accepted or committed.

### Two-phase approach

Most consensus algorithms follow a two-phase approach, where proposals are first prepared and then accepted. This reduces the likelihood of conflicts and ensures safety.

### Leader-based or leaderless

Some consensus algorithms use a leader-based approach, where a designated leader coordinates the consensus process. Others are leaderless, where nodes work collaboratively to achieve consensus.

### Message exchange

Nodes communicate with each other by exchanging messages to propose values, vote, and inform each other about their states.

### Reliable multicasting

A group of servers attempting to receive the same updates in the same order as each other.

### Log replication

Many consensus algorithms include log replication mechanisms to ensure that all nodes have a consistent view of the data.

### Consistency and replication

Consensus algorithms ensure data consistency across replicas by replicating data and ensuring that all replicas agree on the same data.

### Membership changes

Some consensus algorithms support dynamic changes in the membership of the cluster, allowing nodes to join or leave the system gracefully.

## Use cases

### Leader election

In a database with single-leader replication, all nodes need to agree on which node is the leader. The position might become contested if some nodes can't communicate with others due to a network fault, and may result in a **split brain situation** in which two nodes both believe themselves to be the leader. **This would cause data to diverge, leading to inconsistency and data loss.**

### Atomic commit

In a database that supports transactions spanning several nodes/partitions, we have the problem that a transaction may fail but succeed on others. To maintain atomicity, need to get all nodes to agree on the outcome of the transaction: either all abort or commit (if succeeds).
