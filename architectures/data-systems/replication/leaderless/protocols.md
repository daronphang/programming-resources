## Protocols

A distinction can be made between active replication, in which an operation is forwarded to all replicas, and consistency protocols based on majority voting.

## Active replication

In active replication, each replica has an associated process that carries out update operations. In contrast to other protocols, updates are generally propagated through the write operation that causes the update i.e. operation is sent to each replica.

One problem with active replication is that operations need to be carried out in the **same order everywhere**. Consequently, what is needed is a totally ordered multicast mechanism. A practical approach to accomplish total ordering is by a **central coordinator**, also called a **sequencer**. One approach is to first forward each operation to the sequencer, which assigns it a unique sequence number and subsequently forwards the operation to all replicas. Operations are carried out in the order of their sequence number.

## Quorum-based

A different approach to supporting replicated writes is to use voting. The basic idea is to require clients to request and acquire the permission of multiple servers before either reading or writing a replicated data item.

### Constraint for strong consistency

The constraint for leaderless replication is as follows:

- w: Number of nodes that confirm the writes with an ACK
- r: Number of nodes queried for the read
- n: Total number of nodes

For strong consistency:

```
w + r > n
```

### Writing

Leaderless Replication eradicates the need of having a leader accepting the writes; instead, it **leverages quorum to ensure strong consistency across multiple nodes** and good tolerance to failures i.e. for write operation to 5 master nodes, it waits for ACK from at least 3 nodes.

Every record in the database has a monotonically increasing version number. Every successful write updates this version number allowing us and the system to identify the latest value of the record upon conflict.

### Reading

Given that there could be a significant delay in the updates to propagate across all N nodes, the Read strategy in Leaderless Replication needs to be robust enough.

Like how the client fanned out the write operation to all the nodes, it also fans out the Read operation to all N nodes. The client waits to get responses from at least N/2 + 1 nodes. Upon receiving the responses from a majority of the nodes, it returns the value having the **largest version number**.
