## Asynchronous transactions

2PC is a synchronous blocking protocol, and is generally combined with 2PL to provide isolation. However, some transactions may take long to execute, and may not require isolation in the first place.

For instance, to combine a RDS with Elasticsearch for full-text search capability, updates to the RDS would also need to be made in Elasticsearch.

## Log-based transactions

A log is an append-only, totally ordered sequence of messages, in which each message is assigned a unique sequential index. Messages are appended at the end of the log, and consumers read from it in order. Kafka and Azure Event Hubs are two popular implementations of logs.

When a service receives a request, instead of executing it directly in the database, it appends to the message log. Consumers (database, search index) would then consume from the message log, reading entries in the same order as they were appended and updating their state at their own pace.

### Idempotent

The consumer can potentially read the same message multiple times. For example, it could process a message and crash before checkpointing its state. Hence, messages need to be **idempotent**. ne way to do that is to decorate each message with a unique ID and ignore messages with duplicate IDs at read time.
