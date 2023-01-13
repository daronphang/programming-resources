## Partitioning

For very large datasets, or very high query throughput, need to break data up into **partitions/sharding to achieve scalability**. Different partitions can be placed on different nodes in a shared-nothing cluster. Hence, a large dataset can be distributed across many disks, and the query load can be distributed across many processors.

For queries that operate on a single partition, each node can independently execute the queries for its own partition, and query throughput can be scaled by adding more nodes. 

## Partitioning and Replication

Partitioning is usually combined with replication, so that copies of each partition are stored on multiple nodes i.e. each record belongs to one partition, but stored on several nodes for fault tolerance.

A node may store more than one partition. If a leader-follower replication is used, each partition's leader will be assigned to one node, and its followers are assigned to other nodes.

```
Node A
Partition 1 (leader)
Partition 2 (follower)
Partition 3 (follower)

Node B
Partition 1 (follower)
Partition 2 (leader)
Partition 3 (follower)

Node C
Partition 1 (follower)
Partition 2 (follower)
Partition 3 (leader)
```