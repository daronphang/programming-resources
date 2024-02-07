## Leaders and Followers (Master/Slave)

To ensure every write to the database ends up on all replicas, a solution would be to use **leader-based replication**:

1. One of the replicas is designated the leader. All write requests are sent to the leader, which first writes the new data to its local storage.
2. Other replicas are notified of the data change through replication log or change stream. Each follower takes the log from the leader and updates its local copy of the database.

This mode of replication is a built-in feature across many relational and non-relational databases, including MySQL, PostgreSQL, Oracle, SQL Server, MongoDB, Kafka and RabbitMQ.

### Types of Leader-Based Replications

Single-leader or multi-leader.

## Setting Up New Followers

Simply copying data files from one node to another is not sufficient as clients are constantly writing to the database. Implementing locks would go against high availability. Fortunately, it can be setup without downtime as follows:

1. Take a consistent snapshot of the leader's database at some point in time. Most databases have this feature as it is also required for backups.
2. Copy the snapshot to the new follower node.
3. The follower connects to the leader and requests all the data changes that have happened since the snapshot was taken. **This requires that the snapshot is associated with an exact position in the leader's replication log** i.e. log sequence number, binlog coordinates.
4. When the follower has processed the backlog of data changes since snapshot, it has caught up.

## Leader Failure (Failover)

One of the followers need to be promoted to be the new leader, clients need to be reconfigured to send their writes to the new leader, and other followers need to start consuming data changes from the new leader.

As there are many things that can wrong i.e. crashes, power outages, network issues, there is no foolproof way of detecting what has gone wrong. Instead, nodes frequently bounce messages off between each other, and assumed to be dead after a certain timeout.

### Failover Issues

Some operation teams prefer to do failover manually due to the following issues:

- If asynchronous replication is used, the new leader may not have received all the writes from the old leader. Most common solution is to discard un-replicated writes, but may violate clients' durability expectations.
- Two nodes believe that they are the leader (split brain) and is dangerous as there is no process for resolving conflicts.
- Deciding on the right timeout before the leader is declared dead.

## Replication Lag

For asynchronous replications involving distributed databases, if the follower has fallen behind the leader, will lead to inconsistencies as all writes have been reflected in the follower. However, this is just a temporary state, and this effect is known as **eventual consistency**. If the lag is large, the inconsistencies can become a problem for applications.

Hence, need to design systems that provides a stronger guarantee for read-after-write.

### Reading Your Own Writes

To implement read-after-write consistency, can either read data that is editable by the user from the leader i.e. social media profile, and others from followers. Alternative is to track the time of the last update, and make all reads from the leader before a certain duration has passed i.e. one minute.

### Monotonic Reads

Monotonic reads means that if one user makes several reads in a sequence, they will not read older data that has not been updated by followers. This is achieved by making sure each user is reading from the same replica.

### Consistent Prefix Reads

This guarantee says that if a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.

Solution is to ensure that any writes that are casually related to each other are written to the same partition by using algorithms.
