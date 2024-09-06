## Brokers

A single Kafka server is called a broker that can handle thousands of partitions and millions of messages per second. The broker performs the following:

- Receives messages from producers
- Assigns offsets to messages
- Writes the message to storage on disk
- Responds to fetch requests for partitions and responding with messages that have been published

A Kafka cluster is typically comprised of several brokers. Every broker in a cluster is also a **bootstrap server**, meaning if you can connect to one broker in a cluster, you can connect to every broker.

Kafka brokers are designed to operate as part of a cluster. Within a cluster, one broker will function as the cluster controller (elected automatically from the live members of the cluster). The controller is responsible for administrative operations, assigning partitions to brokers, and monitoring for broker failures.

## Data replication, leader and followers

Replication is accomplished through setting the **topic replication factor**, which specifies the number of copies of data over multiple brokers.

How will a producer know which broker to publish data to for a particular partition? To avoid the inevitable confusion of having both the actual data and its copies present in a cluster, Kafka follows a **leader-follower system**. That way, one broker can be set as the leader of a topic partition and the rest of the brokers as followers for that partition, with only the leader being able to handle those client requests.

**A partition is owned by a single broker in the cluster**, and that broker is called the **leader** of the partition. A replicated partition is assigned to additional brokers called **followers**. Replication provides redundancy, such that one of the followers can take over leadership if there is a broker failure.

All **producers must connect to the leader in order to publish messages**, but consumers may fetch from either the leader or one of the followers.

### Availability over consistency

if all the replicas in the in-sync replicas (ISRs) die at once, Kafka may lose data or choose an unclean leader. An unclean leader is a replica that does not have all the committed messages, but is elected as the leader anyway. This can happen if all the replicas for a partition are down, and **Kafka decides to favor availability over consistency** as the default behavior. Therefore, Kafka’s guarantee about data loss only holds if at least one replica in the ISR is alive.

<img src="../assets/brokers-clusters.png">

## Connecting to the Leader of partition

Kafka is a distributed system. Data is read from and written to the Leader for a given partition, which could be on any of the brokers in a cluster.

When a client (producer/consumer) starts, it will **request metadata about which broker is the leader for a partition**; it can do this from **any broker**. This is also known as the **bootstrap call** (configured via bootstrap.servers).

The metadata returned will include the endpoints available for the Leader broker for that partition, and the client will then use those endpoints to connect to the broker to read/write data as required. The exact broker to send messages to depends on which is the leader for the concrete partition.

The key thing is that when you run a client, the broker you pass to it is just where it’s going to go and get the metadata about brokers in the cluster from. The actual host and IP that it will connect to for reading/writing data is based on the data that the broker passes back in that initial connection; even if it’s just a single node and the broker returned is the same as the one connected to.

If you want to use SSL, need to include SSL in your listener name e.g. LISTENER_EXTERNAL_SSL.

https://rmoff.net/2018/08/02/kafka-listeners-explained/
