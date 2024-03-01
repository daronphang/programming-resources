## Consumption of events

Commonly available event brokers use an append-only immutable log, and events are given an auto-incrementing index ID.

Consumers of the data use a reference to the index ID to access data. Events can either be consumed as an event stream or a queue. However, queues are not supported by all event brokers i.e. Kafka.

### Offset

Each consumer is responsible for updating its own pointers to previously read indices (offset) within the event stream. This offset is the measurement of the current event from the beginning of the event stream. Offsets permit multiple consumers to consume and track their progress independently.
