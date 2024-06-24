## Partitioning/sharding

For very large datasets, or very high query throughput, need to break data up into **partitions/sharding to achieve scalability**. Different partitions can be placed on different nodes in a shared-nothing cluster. Hence, a large dataset can be distributed across many disks, and the query load can be distributed across many processors.

Each shard contains a subset of the data and is responsible for handling a portion of the data workload. Sharding is done to improve data distribution, scalability, and performance.

Sharding is entirely transparent to the application which is able to connect to any node in the cluster and have queries automatically access the correct shards. Instead of relying on automatic coordination, applications determine where data is located and route queries accordingly.

For queries that operate on a single partition, each node can independently execute the queries for its own partition, and query throughput can be scaled by adding more nodes.

### How sharding works

1. Data is partitioned based on specific criteria e.g. user ID
2. Each partition (shard) resides on a dedicated server
3. Applications determine the correct shard for a given query
4. Data within a shard can be replicated for high availability

## Benefits

### Simpler architecture

Sharding eliminates the complexities of inter-node communication and automatic data distribution, resulting in a simpler system to understand and manage.

### Independent scaling

Individual shards can be scaled independently, offering more granular control over resource allocation.

### Clear data ownership

Each shard has a well-defined responsibility for a specific subset of data, eliminating the ambiguity of ownership that can arise in clusters.

### Simplified algorithm

The logic for data placement is significantly simpler than complex cluster management algorithms, reducing the likelihood of catastrophic failures.

## Drawbacks

### No database-level joins

Since data is spread across multiple shards, performing joins across different shards becomes challenging. This is because the data has to be compiled from multiple servers, which can add significant overhead and negatively impact performance.

However, there are ways to mitigate this issue. Utilizing caching and fast networks can help to speed up the process and ensure that page load times remain fast. Additionally, de-normalizing the database by merging related data into a single table can also be a viable solution, as it allows for the execution of previously complex join queries on a single table.

### Referential integrity

Maintaining data integrity, such as using foreign keys, can be a challenge when using a sharded database. Most relational database management systems don’t support foreign keys across different servers, making it difficult to enforce referential integrity.

Applications that rely on this feature may need to implement it in their code and run regular SQL jobs to keep the data consistent. This can add extra complexity and maintenance to the application.

### No database-level transactions

Transactions spanning multiple shards are not possible, requiring application-level logic to maintain data consistency and integrity.

### Increased application complexity

Applications must handle shard routing and manage data consistency across shards, adding complexity to the development process.

### Schema changes are more involved

Modifying database schemas requires applying changes to all individual shards.

### Reporting complexity

Generating reports that span multiple shards requires retrieving data from each shard and aggregating the results manually.

### Rebalancing

As data grows or shrinks, shards may need to be rebalanced, which can be a complex and resource-intensive process.

## Hot shard

A “hot shard” refers to a specific shard or partition within a distributed data storage system or database that is experiencing a disproportionately high level of data traffic or activity compared to other shards or partitions i.e. a bottleneck. This imbalance can lead to performance degradation for the entire system.

Causes include:

- Uneven data distribution
- Popular data that are frequently accessed
- Inefficient queries

## Partitioning and replication

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
