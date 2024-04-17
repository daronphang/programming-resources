## Partitions

Topics are broken up into partitions, meaning a single topic log is broken into multiple logs located on different Kafka brokers. This way, the work of storing messages, writing new messages, and processing existing messages can be split among many nodes in the cluster. This distributed placement of your data is very important for scalability because it allows client applications to both read and write the data from/to many brokers at the same time.

A partition is a single log. Messages are written to it in an append-only fashion and are read in order from beginning to end. Partitions are the way that Kafka provides redundancy and scalability.

Each partition can be hosted on a different server, which means that a single topic can be scaled horizontally across multiple servers to provide performance. Partitions can also be replicated, such that different servers will store a copy of the same partition in case one server fails.

However, adding a new consumer in Kafka forces a **rebalance** across the partitions which seems to be a fairly expensive operation.

### Order

Kafka guarantees that any consumer of a given topic partition will always read that partition’s events in exactly the same order as they were written.
