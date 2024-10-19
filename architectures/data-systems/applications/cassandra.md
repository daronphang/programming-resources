## Cassandra

Cassandra is a distributed storage system for managing very large amounts of structured data spread out across many commodity servers (possibly spread across different data centers), while providing highly available service with no single point of failure.

Cassandra does not support a full relational data model. Instead, it provides clients with a simple data model that supports dynamic control over data layout and format.

### Data model

A table in Cassandra is a distributed multi dimensional map indexed by a key. The value is an object which is highly structured. Every operation under a single row key is atomic per replica no matter how many columns are being read or written into. Columns are grouped together into sets called column families.

## System architecture

A read/write request for a key gets routed to any node in the Cassandra cluster. The node then determines the replicas for this particular key.

For writes, the system routes the requests to the replicas and waits for a **quorum of replicas** to acknowledge the completion of the writes.

For reads, based on the consistency guarantees required by the client, the system either routes the requests to the closest replica or routes the requests to all replicas and waits for a quorum of responses.

### Partitioning

Cassandra has the ability to scale incrementally, and this requires the ability to dynamically partition the data over a set of nodes. This is performed using **consistent hashing**, but uses an order preserving hash function to do so.

The basic consistent hashing algorithm presents some challenges:

- The random position assignment of each node on the ring leads to non-uniform data and load distribution
- The basic algorithm is oblivious to the heterogeneity in the performance of nodes

There exist two ways to address this issue:

- Nodes are assigned to multiple positions in the ring (vnodes) i.e. similar to Dynamo
- Analyze load information on the ring and have lightly loaded nodes move on the ring to alleviate heavily loaded nodes (Cassandra opted for this)

### Replication

Cassandra uses replication to achieve high availability and durability.

Each key is assigned to a coordinator node i.e. the first node hashed on the ring. The coordinator node is in charge of the replication of data that fall within its range.

Cassandra system at Facebook elects a leader amongst its nodes using a system called Zookeeper. All nodes on joining the cluster contact the leader who tells them for what ranges they are replicas for and leader makes a concerted effort to maintain the invariant that no node is responsible for more than N-1 ranges in the ring. The metadata about the ranges a node is responsible is cached locally at each node and in a fault-tolerant manner inside Zookeeper.

### Membership

Cluster membership is based on **Scuttlebutt**, a very efficient anti-entropy Gossip based mechanism. The salient feature of Scuttlebutt is that it has very efficient CPU utilization and very efficient utilization of the gossip channel.

### Bootstrapping

When a node starts for the first time, it chooses a random token for its position in the ring. For fault tolerance, the mapping is persisted to disk locally and also in Zookeeper. The token information is then gossiped around the cluster.

### Scaling

When a new node is added into the system, it gets assigned a token such that it can alleviate a heavily loaded node. This results in the new node splitting a range that some other node was previously responsible for.

### Local persistence

The Cassandra system relies on the local file system for data persistence.

Typical write operation involves a write into a commit log for durability and recoverability and an update into an in-memory data structure. The write into the in-memory data structure is performed only after a successful write into the commit log. A **dedicated disk** is provided on each machine for the commit log to maximize disk throughput.

A typical read operation first queries the in-memory data structure before looking into the files on disk. The files are looked at in the order of newest to oldest. When a disk lookup occurs we could be looking up a key in multiple files on disk. In order to prevent lookups into files that do not contain the key, a **bloom filter**, summarizing the keys in the file, is also stored in each data file and also kept in memory.
