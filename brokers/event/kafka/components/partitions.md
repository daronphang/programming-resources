## Partitions

A partition is a single log. Messages are written to it in an append-only fashion and are read in order from beginning to end. Partitions are the way that Kafka provides redundancy and scalability.

Kafka partitions speed up the processing of large amounts of data in parallel by distributing message processing across many nodes in your Kafka cluster.

Instead of writing all of your data from a topic to one partition (and thus one broker), you are able to split your topics into different partitions and distribute those partitions to brokers i.e. meaning a single topic log is broken into multiple logs located on different Kafka brokers.

In this way, the work of storing messages, writing new messages, and processing existing messages can be split among many nodes in the cluster. This distributed placement of your data is very important for scalability because it allows client applications to both read and write the data from/to many brokers at the same time. In other words, **a topic partition is the unit of parallelism in Kafka**.

Each partition can be hosted on a different server, which means that a single topic can be scaled horizontally across multiple servers to provide performance. Partitions can also be replicated, such that different servers will store a copy of the same partition in case one server fails. The number of partitions can also be significantly higher than the number of brokers.

Unlike other messaging systems, producers are responsible for deciding which partition messages are written to. However, adding a new consumer in Kafka forces a **rebalance** across the partitions which seems to be a fairly expensive operation.

### Performance

The more Kafka partitions you have:

- Data throughput is higher: Parallel executions of publishing and processing messages by publisher, broker and consumer
- More consumers in consumer groups
- More open file handles you have on brokers: Kafka opens two files for each segment of a partition which are the log and index
- More RAM consumed by clients: Clients create buffers per partition

### Limits

- Maximum of 4000 partitions per broker (distributed over many topics)
- Maximum of 200,000 partitions per cluster
- Good guideline is 12 partitions

### Ordering

Kafka guarantees the order of the events **within the same topic partition**. However, by default, it does not guarantee the order of events across all partitions.

For example, to improve performance, we can divide the topic into two different partitions and read from them on the consumer side. In that case, a consumer reads the events in the same order they arrived at the same partition. In contrast, if Kafka delivers two events to different partitions, we can’t guarantee that the consumer reads the events in the same order they were produced.

## Partitioning strategies

### Semantic partitioning

To improve the ordering of events, we can **set an event key** to the event object. With that, **events with the same key are assigned to the same partition**, which is ordered. Thus, events with the same key arrive at the consumer side in the same order they were produced.

### Random partitioning

Random partitioning results in the evenest spread of load for consumers, and thus makes scaling the consumers easier. It is particularly suited for stateless or “embarrassingly parallel” services. Records will get added to a batch and pushed to a random topic partition.

## How Kafka determines which partition to send data to

### DefaultPartitioner

The strategy is as follows:

- If a partition is specified in the record, use it
- If no partition is specified but a key is present, choose a partition based on a hash of the key

```
Partition number = Hash(Key) % Number of partitions
```

- If no partition or key is present, buffer the message until it is full or when linger.ms timeouts, and send to the sticky partition

### UniformStickyPartitioner

This partitioner **does not make use of record key**. The strategy is as follows:

- If a partition is specified in the record, use it
- Otherwise choose the sticky partition (similar to above)

## Why repartition?

In most cases, users will set up their applications that consume from a Kafka topic to have a number of consumers that is a divisor of the number of partitions so that one consumer won’t be overloaded relative to other consumers.

However, data can still be distributed unevenly to different partitions if there is a hotkey or poor partitioning strategy, and repartitioning may be necessary in these cases. This would result in a **data skew** where one or more consumers will be overloaded with a disproportionate amount of data to process.

Another reason ou may want to repartition your Kafka data is to align your data according to its context i.e. changing the partition key.

## Changing partitions in a topic

While it is possible to change the number of partitions, however, doing so requires careful consideration as it may affect data distribution and consumer behavior.

### Removing

Kafka does not support decreasing the number of partitions as it would result in data loss.

## Adding

When you increase the number of partitions, the existing messages will remain in the same partitions as before, and only new messages will be considered for new partitions.

Be aware that adding partitions doesn’t change the partitioning of existing data so this may disturb consumers if they rely on that partition. That is if data is partitioned by hash(key) % number_of_partitions then this partitioning will potentially be shuffled by adding partitions but Kafka will not attempt to automatically redistribute data in any way. One strategy to avoid this is to over-partition by a factor.

## Multiple topics vs partitions

- Separation of concerns: You should create distinct topics for distinct entities e.g. users, orders
- Host storage capabilities: A partition must fit in the storage of the host machine, while a topic can be distributed across Kafka cluster
- Retention policy: Message retention works at partition level
