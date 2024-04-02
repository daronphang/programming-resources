## Events and event streaming

Event streaming is the practice of capturing events in real-time from sources including databases, sensors, mobile devices, cloud services, and software applications.

An event streaming platform captures events in order and these streams of events are stored durably for processing, manipulation, and responding to in real time or to be retrieved later. In addition, event streams can be routed to different destination technologies as needed. Event streaming ensures a continuous flow and interpretation of data so that the right information is at the right place, at the right time.

## Features

### Partitioning

Event streams can be partitioned into individual sub-streams. This partitioning mechanism allows for multiple instances of a consumer to process each sub-stream in parallel, allowing for greater throughput.

### Strict ordering

Data in an event stream partition is strictly ordered. Commonly, event brokers enable an immutable, append-only log of facts that preserves the state of event ordering.

### Immutability

All event data is completely immutable once published. You can only modify previous data by publishing a new event with the updated data.

### Indexing

Events are assigned an index when written to the event stream. This is used by consumers to manage data consumption, as they can specify which offset to begin reading from.

Consumer lag is the difference between the consumer's current index and the tail index. It can be used to scale up the number of consumers when it is high, and scale down when low.

### Infinite retention

Event streams must be able to retain events for an infinite period of time.

### Replayability

Event streams must be replayable, such that any consumer can read whatever data it requires.
