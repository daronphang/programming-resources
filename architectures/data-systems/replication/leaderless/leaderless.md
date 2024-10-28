## Leaderless replication (replicated-write)

Leader-centric replication is not fault-tolerant by design because we lose the write operation when the master node is down. Leaderless replication addresses this concern and ensures our system can handle write operations even when a subset of nodes are having an outage. In replicated-write protocols, write operations can be carried out at **multiple replicas instead of only one**, as in the case of primary-based replicas.

However, concurrency issues arise for leaderless and multi-leader replication as they allow multiple writes to happen concurrently, and conflicts may occur.

This architecture is used in databases including Amazon Dynamo, Riak, Cassandra and Voldemort.

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
