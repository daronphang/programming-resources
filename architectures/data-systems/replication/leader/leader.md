## Leaders and followers (master/slave)

To ensure every write to the database ends up on all replicas, a solution would be to use **leader-based replication**:

1. One of the replicas is designated the leader. All write requests are sent to the leader, which first writes the new data to its local storage
2. Other replicas are notified of the data change through replication log or change stream. Each follower takes the log from the leader and updates its local copy of the database

This mode of replication is a built-in feature across many relational and non-relational databases, including MySQL, PostgreSQL, Oracle, SQL Server, MongoDB, Kafka and RabbitMQ.

## Types of leader-based replications

Single-leader or multi-leader.

## Setting up new followers

Simply copying data files from one node to another is not sufficient as clients are constantly writing to the database. Implementing locks would go against high availability. Fortunately, it can be setup without downtime as follows:

1. Take a consistent snapshot of the leader's database at some point in time. Most databases have this feature as it is also required for backups
2. Copy the snapshot to the new follower node
3. The follower connects to the leader and requests all the data changes that have happened since the snapshot was taken. **This requires that the snapshot is associated with an exact position in the leader's replication log** i.e. log sequence number, binlog coordinates
4. When the follower has processed the backlog of data changes since snapshot, it has caught up

## Leader failure (failover)

One of the followers need to be promoted to be the new leader, clients need to be reconfigured to send their writes to the new leader, and other followers need to start consuming data changes from the new leader.

As there are many things that can wrong i.e. crashes, power outages, network issues, there is no foolproof way of detecting what has gone wrong. Instead, nodes frequently bounce messages off between each other, and assumed to be dead after a certain timeout.

### Failover issues

Some operation teams prefer to do failover manually due to the following issues:

- If asynchronous replication is used, the new leader may not have received all the writes from the old leader. Most common solution is to discard un-replicated writes, but may violate clients' durability expectations
- Two nodes believe that they are the leader (split brain) and is dangerous as there is no process for resolving conflicts
- Deciding on the right timeout before the leader is declared dead
