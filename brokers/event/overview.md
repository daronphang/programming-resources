## Event Broker

A system that is the heart of an event-driven microservice platform, and that receives events, stores them in a queue or partitioned event stream, and provides them for consumption by other processes.

### Partitioning

Event streams can be partitioned into individual substreams. This partitioning mechanism allows for multiple instances of a consumer to process each substream in parallel, allowing for greater throughput.

### Strict Ordering

Data in an event stream partition is strictly ordered. Commonly, event brokers enable an immutable, append-only log of facts that preserves the state of event ordering.

### Immutability

All event data is completely immutable once published. You can only modify previous data by publishing a new event with the updated data.

### Indexing

Events are assigned an index when written to the event stream. This is used by consumers to manage data consumption, as they can specify which offset to begin reading from.

Consumer lag is the difference between the consumer's current index and the tail index. It can be used to scale up the number of consumers when it is high, and scale down when low.

### Infinite Retention

Event streams must be able to retain events for an infinite period of time.

### Replayability

Event streams must be replayable, such that any consumer can read whatever data it requires.
