## Event vs message brokers

An event broker stores a sequence of events. Events are usually appended to a log (queue or topic) in the order in which they arrived at the event broker. Events in the topic or queue are immutable and their order cannot be changed.

Message brokers are used for services or components to communicate with each other. It provides the exchange of information between applications by transmitting messages received from the producer to the consumer in an async manner.

When dealing with a short-lived command or task-oriented processing, or when there is complex message routing involved, we would favor using a **message broker**. When dealing with current or historical events, usually in large volumes of data, which need to be processed in either a single or bulk manner, we would favor an **event broker**.

Event brokers can be used in place of a message broker, but not vice versa. They are designed around providing an ordered log of facts.

There are two specific needs that message brokers are not able to satisfy: consumption of message and message retention.

Nonetheless, message brokers are valid patterns for EDM architectures, but are not sufficient for the full scope of duties such architectures require.

## Kafka vs RabbitMQ

### Consumption of message

RabbitMQ provides queues of messages, and applications that share consumption from a queue will each receive only a subset of the records i.e. multiple queues are required in order for multiple consumers to get the same message. This makes it impossible to correctly communicate state via events, since each consumer is unable to obtain a full copy of events.

Unlike RabbitMQ, Kafka maintains a single ledger of records and manages individual access via indices, so each independent consumer can access all required events i.e. multiple consumers can read the same messages from the same queue.

### Message retention

RabbitMQ deletes events after acknowledgement, whereas Kafka retains them for as long as the organization needs.

The deletion of an event after consumption makes a message broker insufficient for providing indefinitely stored, globally accessible, replayable, single source of truth for all applications.

### Event order

Event order is not maintained when processing from a queue. If a consumer fails to process an event, it will return the event to the queue for processing at a later date.

### Message ordering

RabbitMQ provides few guarantees regarding ordering messages sent to a queue or exchange, especially when multiple consumers are involved from the same queue. The lack of ordering guarantee happens because consumers might return messages to the queue after reading them e.g. processing failure.

For Kafka, they provide a reliable ordering guarantee for message processing. All messages sent to the same topic partition are processed in order.

### Message priority and distribution

Messages can be given priorities in RabbitMQ. It also allow for low latency and complex message distributions i.e. provides clients flexibility for complex routing scenarios and receive specific messages.

With Kafka, all messages have the same priority, so message are always received in the order that they were sent to the topic. Also, event brokers do not allow consumers to filter messages on a topic before polling them.

### Message timing

RabbitMQ provides various capabilities in regards to timing a message sent to a queue: Time-to-Live (TTL) and Delayed/Scheduled messages.

Kafka provides no support for such features. It writes messages to partitions as they arrive, where they are immediately available for consumers to consume.

### Data flow

Messages are sent to exchanges and routed to queues in RabbitMQ. They then sit in the queue until read (and acknowledged), at which point they are deleted.

In Kafka, messages are sent in a continuous stream to the topic, where they are read by the consumers.

### Performance

Kafka is more performant than RabbitMQ, allowing for higher throughput due to their architecture.

### Consumer model (push vs poll)

RabbitMQ has a smart broker/dumb consumer model. All the routing and decisions are made in the broker, then it pushes the messages to the clients (passive). The messages are then removed from the queue after all acknowledgments are received.

Kafka has a dumb broker/smart consumer model. The broker just sends messages to the queues to be read. This is decided by the producer (sending to the correct queue), and the consumer (reading from the correct queue). Consumers take on a more proactive role in reading and tracking information using an offset counter.

### Error handling

Kafka handles message processing errors by delegating the responsibility to the consumer. If a message was processed a few times unsuccessfully (poison pill), the consumer application will need to keep track of the attempts and then produce a message to separate DLQ (dead letter queue) topic, where it can be examined/re-run later on. Hence, the consumer must provide and implement message retry mechanisms at application level.

RabbitMQ keeps track of failures in processing a message. After a message is considered a poison pill, it is routed to a DLQ exchange. Hence, it provides a **guarantee** that a message which was not processed successfully will not get lost.
