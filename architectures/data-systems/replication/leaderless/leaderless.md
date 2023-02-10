## Leaderless Replication

In some implementations, client directly sends its writes to several replicas, while others make use of a coordinator node to do this on behalf of the client. Unlike a leader database, the coordinator does not enforce a particular ordering of writes.

However, concurrency issues arise for leaderless and multi-leader replication as they allow multiple writes to happen concurrently, and conflicts may occur.

This architecture is used in databases including Amazon Dynamo, Riak, Cassandra and Voldemort.

## Writing

When a client sends a write, it sends to all available replicas. If one replica is offline, it will miss the write. When querying the updated write, the client will read from all replicas and returns the latest value by versioning number.

## Catching-up Mechanisms

### Read Repair

When a client makes a read from several nodes in parallel, it can detect any stale responses and writes the newer value back to that replica. This approach works well for values that are frequently read. However, values that are rarely read may be missing and thus have reduced durability.

### Anti-Entropy Process

Background process that constantly looks for differences in the data between replicas, and copies any missing data from one replica to another.
