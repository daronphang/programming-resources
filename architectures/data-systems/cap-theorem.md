## CAP Theorem in DBMS

A distributed system with data replication can deliver only two of three desired characteristics: consistency, availability, and partition tolerance.

A distributed system is a network that stores data on more than one node (physical or virtual machines) at the same time. Because all cloud applications are distributed systems, it’s essential to understand the CAP theorem when designing a cloud app so that you can choose a data management system that delivers the characteristics your application needs most.

### Consistency (among replicated copies)

Consistency means that all clients see the same data at the same time, no matter which node they connect to i.e. nodes will have the same copies of a replicated data. For this to happen, whenever data is written to one node, it must be instantly forwarded or replicated to all the other nodes in the system before the write is deemed ‘successful.’

### Availability (of the system for read/write operations)

Availability means that any client making a request for data gets a response, even if one or more nodes are down. All working nodes in the distributed system return a valid response for any request, **without exception**.

Each read or write request for a data item will either be processed successfully or receive a message that the operation cannot be completed. However, the data returned might not be the most recent.

### Partition Tolerance (of nodes due to network fault)

Partition tolerance means that the system can continue operating even if the network connecting the nodes has a fault that results in two or more partitions, where the **nodes in each partition can only communicate with each other**. The system can continue to uphold its consistency guarantees in spite of network partitions. Distributed systems guaranteeing partition tolerance can gracefully recover from partitions once the partition heals.

Partition tolerance is a way of life, and **must be provided**.

## Combinations

As Partition Tolerance is required, one can choose to guarantee consistency or availability:

- High consistency comes at the cost of lower availability
- High availability comes at the cost of lower consistency

### CP

Examples include MongoDB, Redis, HBase.

MongoDB stores data as BSON (Binary JSON) documents. It has a single-master system: each replica set can have only one primary node that receives all write operations.

### AP

Examples include Cassandra, DynamoDB, CosmosDB.

Apache Cassandra doesn't have a master node, and all nodes must be available continuously. However, Cassandra provides eventual consistency by allowing clients to write to any nodes at any time and reconciling inconsistencies as quickly as possible.
