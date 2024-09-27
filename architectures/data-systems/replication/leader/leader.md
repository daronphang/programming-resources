## Leader replication (primary-based)

In the case of sequential consistency, it turns out that primary-based protocols prevail. In these protocols, each data item x in the data store has an associated primary, which is responsible for coordinating write operations on x.

This mode of replication is a built-in feature across many relational and non-relational databases, including MySQL, PostgreSQL, Oracle, SQL Server, MongoDB, Kafka and RabbitMQ.

### How it works

1. One of the replicas is designated the leader. All write requests are sent to the leader, which first writes the new data to its local storage
2. Other replicas are notified of the data change through replication log or change stream. Each follower takes the log from the leader and updates its local copy of the database

### Types

There are two types: single-leader and multi-leader.

## Setting up new followers

Simply copying data files from one node to another is not sufficient as clients are constantly writing to the database. Implementing locks would go against high availability. Fortunately, it can be setup without downtime as follows:

1. Take a consistent snapshot of the leader's database at some point in time. Most databases have this feature as it is also required for backups
2. Copy the snapshot to the new follower node
3. The follower connects to the leader and requests all the data changes that have happened since the snapshot was taken. **This requires that the snapshot is associated with an exact position in the leader's replication log** i.e. log sequence number, binlog coordinates
4. When the follower has processed the backlog of data changes since snapshot, it has caught up
