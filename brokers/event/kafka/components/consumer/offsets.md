## Tracking consumer position

In Kafka, the broker and consumer must agree on what has been consumed. If there isn’t agreement, issues can occur.

For example, if a broker records a message as consumed immediately after sending it, and the consumer crashes or the request times out, the message doesn’t get processed by the consumer and that message is lost.

Alternatively, the broker can wait for acknowledgement from the consumer before recording the message as consumed. In this example, if the consumer processes the message but fails before it can send an acknowledgement, then the message will be consumed twice.

Kafka solves these tracking issues by utilizing **consumer offsets**.

## Offsets

The only metadata retained on a per-consumer basis is the offset or position of that consumer in a topic. This offset is controlled by the consumer.

A consumer offset is used to track the progress of a consumer group. An offset is a unique identifier, an integer, which marks the last message that a consumer processed in a partition.

The offset is an integer value that continually increases, and is a metadata that Kafka adds to each message as it is produced. The message in a given partition has a unique offset, and the following message has a greater offset.
