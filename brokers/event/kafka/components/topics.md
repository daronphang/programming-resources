## Topics

The Kafka cluster organizes and durably stores streams of events in categories called topics, which are Kafka’s most fundamental unit of organization. A topic is a log of events, similar to a folder in a filesystem, where events are the files in that folder. Topics are additionally broken down into a number of partitions.

### Characteristics

- A topic is append only: When a new event message is written to a topic, the message is appended to the end of the log
- Events in the topic are immutable, meaning they cannot be modified after they are written
- A consumer reads a log by looking for an offset and then reading log entries that follow sequentially
- Topics in Kafka are always multi-producer and multi-subscriber: a topic can have zero, one, or many producers that write events to it, as well as zero, one, or many consumers that subscribe to these events

Topics cannot be queried, however, events in a topic can be read as often as needed, and unlike other messaging systems, events are not deleted after they are consumed. Instead, topics can be configured to expire data after it has reached a certain age or when the topic has reached a certain size.

**Kafka’s performance is effectively constant with respect to data size**, so storing data for a long time should have a nominal effect on performance.
