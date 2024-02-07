## Keys and Partitions

Keys serve two goals:

- Additional information that gets stored with the message
- Typically used to decide which one of the topic partitions the message will be written to

All messages with the same key will go to the same partition. If the key is null, the default partitioner will be used, and the record will be sent to one of the available partitions of the topic at random using a round-robin algorithm to balance the messages among the partitions.

If a key exists and the default partitioner is used, Kafka will hash the key and use the result to map the message to the same partition. All partitions in the topic are used to calculate the mapping, including available and unavailable partitions.
