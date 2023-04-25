## Replication

Replication is at the heart of Kafka's architecture, and is critical as it ensures availability and durability when individual nodes inevitably fail.

Data is Kafka is organized by topics. Each topic is partitioned, and each partition can have multiple replicas. Those replicas are stored on brokers, and each broker typically stores hundreds or thousands of replicas belonging to different topics and partitions.

### Leader Replica

Each partition has a single replica designated as the leader. All produce requests go through the leader to guarantee consistency. Clients can consume from either the lead replica or its followers.

Another task the leader is responsible for is knowing which of the follower replicas is up-to-date with the leader. Replicas send the leader Fetch requests (same type of requests that consumers send to consume messages). Those Fetch requests contain the offset of the message that the replica wants to receive next. This means that the leader can know if a replica is out-of-sync by looking at the last offset requested by each replica.

### Follower Replica

All replicas for a partition that are not leaders are called followers. Unless configured otherwise, followers don't serve client requests; their main job is to replicate messages from the leader and stay up-to-date with the most recent messages the leader has. If a leader replica crashes, one of the follower replicas will be promoted to become the new leader for the partition.

The ability to read from follower replicas was added as a feature to decrease network traffic costs. To use this feature, consumer configuration should include client.rack identifying the location of the client.

The replication protocol was extended to guarantee that only committed messages will be available when consuming from a follower replica. Hence, we get the same reliability guarantees when consuming from both leader and follower replicas. For replicas to know which messages were committed by the leader, the leader includes the current **high-water mark (latest commit offset)** in the data it sends to the follower.
