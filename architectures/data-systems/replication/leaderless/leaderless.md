## Leaderless replication

Leader-centric replication is not fault-tolerant by design because we lose the write operation when the Master node is down. Leaderless replication addresses this concern and ensures our system can handle Write operations even when a subset of nodes are having an outage.

In some implementations, client directly sends its writes to several replicas, while others make use of a coordinator node to do this on behalf of the client. Unlike a leader database, the coordinator does not enforce a particular ordering of writes.

However, concurrency issues arise for leaderless and multi-leader replication as they allow multiple writes to happen concurrently, and conflicts may occur.

This architecture is used in databases including Amazon Dynamo, Riak, Cassandra and Voldemort.

### Constraint for strong consistency

The constraint for leaderless replication is as follows:

- w: Number of nodes that confirm the writes with an ACK
- r: Number of nodes queried for the read
- n: Total number of nodes

For strong consistency:

```
w + r > n
```

## Writing

Leaderless Replication eradicates the need of having a leader accepting the writes; instead, it **leverages quorum to ensure strong consistency across multiple nodes** and good tolerance to failures i.e. for write operation to 5 master nodes, it waits for ACK from at least 3 nodes.

Every record in the database has a monotonically increasing version number. Every successful write updates this version number allowing us and the system to identify the latest value of the record upon conflict.

### Gossip

The nodes gossip internally to propagate the writes to other nodes.

## Reading

Given that there could be a significant delay in the updates to propagate across all N nodes, the Read strategy in Leaderless Replication needs to be robust enough.

Like how the client fanned out the write operation to all the nodes, it also fans out the Read operation to all N nodes. The client waits to get responses from at least N/2 + 1 nodes. Upon receiving the responses from a majority of the nodes, it returns the value having the **largest version number**.

## Catching-up mechanisms

### Read repair

When a client makes a read from several nodes in parallel, it can detect any stale responses and writes the newer value back to that replica. This approach works well for values that are frequently read. However, values that are rarely read may be missing and thus have reduced durability.

### Anti-entropy process

Background process that constantly looks for differences in the data between replicas, and copies any missing data from one replica to another.

## Approaches

### Client-driven fan-out

Client sends reads and writes to all replicated data nodes and decides the correctness depending on the quorum configuration.

### Node coordinator

Client makes a request to any node, and that node starts to act as the coordinator for that transaction. This node coordinator will then take care of the fan-out to other nodes and complete the transaction. Upon completion, it returns the response to the client.
