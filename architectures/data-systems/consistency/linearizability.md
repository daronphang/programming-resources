## Linearizability

A data storage system depicts linearizability when two conditions are satisfied:

- There is a notion of operations executed in sequential order (aligned with real time)
- All operations on it are atomic

A linearizable system provides atomic/strong consistency i.e. **total order**. Totally ordered communication ensures that messages are delivered in the same order to all participants.

Basic idea is to make a system appear as if there was only one copy of the data. With the above guarantees, even though there may be multiple replicas, the application does not need to worry about them. This approach is appealing as it is easy to understand by making a database behave like a variable in a single-threaded program.

In a linearizable system, after a write has occurred (effect is instantaneous) and one client reads the new value, all subsequent reads must also return the new value, even if the write operation has not yet completed. **Total order of operations is preserved** i.e. all operations are put in a single, totally ordered timeline.

## Linearizability vs serializability

Serializability is an isolation property of transactions, where every transaction may read and write multiple objects. It guarantees that transactions behave the same as if they had executed in some serial order.

Linearizability is a recency guarantee on reads and writes of a register/single object: once a new value has been written or read, all subsequent reads see the value that was written, until it is overwritten again. It does not group operations together into transactions, and hence, does not prevent problems such as write skew.

A database may provide both serializability and linearizability, and this combination is known as **strict serializability**, and are based on 2PL or serial execution. However, SSI is not linearizable.

## Applications

### Unique constraints

Unique constraints in databases require linearizability if it needs to be enforced. Other examples include ensuring bank account balance never goes negative, selling more items than you have in stock in the warehouse, or booking the same seat on flights.

## Implementation

### Single-leader replication

The leader has the primary copy of the data that is used for writes. If you make reads from the leader, that have the potential to be linearizable i.e. **client sends reads and writes exclusively to the leader**. However, not every single-leader database is linearizable, either by design (using SSI) or due to concurrency bugs. Also, read throughput would be limited by a single thread.

### Consensus algorithms

Consensus protocols contain measures to prevent split brain and stale replicas. These algorithms can implement linearizable storage safely, and is used in Zookeeper and etcd.
