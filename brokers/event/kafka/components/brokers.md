## Brokers and Clusters

A single Kafka server is called a broker that can handle thousands of partitions and millions of messages per second. The broker performs the following:

- Receives messages from producers
- Assigns offsets to messages
- Writes the message to storage on disk
- Responds to fetch requests for partitions and responding with messages that have been published

A Kafka cluster is typically comprised of several brokers. Every broker in a cluster is also a bootstrap server, meaning if you can connect to one broker in a cluster, you can connect to every broker.

Kafka brokers are designed to operate as part of a cluster. Within a cluster, one broker will function as the cluster controller (elected automatically from the live members of the cluster). The controller is responsible for administrative operations, assigning partitions to brokers, and monitoring for broker failures.

**A partition is owned by a single broker in the cluster**, and that broker is called the **leader** of the partition. A replicated partition is assigned to additional brokers called **followers**. Replication provides redundancy, such that one of the followers can take over leadership if there is a broker failure.

All producers must connect to the leader in order to publish messages, but consumers may fetch from either the leader or one of the followers.

<img src="../assets/brokers-clusters.png">
