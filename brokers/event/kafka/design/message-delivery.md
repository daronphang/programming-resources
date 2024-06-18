## Message delivery semantics

The semantic guarantee Kafka provides between the broker and producers/consumers refer to how they agree to share messages:

- At most once: Messages are delivered once, and if there is a system failure, messages may be lost and are not redelivered
- at least once: Messages are delivered one or more times
- Exactly once (preferred): Messages are never lost or read twice if some part of the system fails

These semantics offer tradeoffs between latency and message durability. You will need to choose the semantic that makes sense for your application context.

## Producer delivery

### At most once

For the lowest latency, messages can be sent asynchronously in a “fire and forget” way, meaning the producer does not wait for any acknowledgement that messages were received.

### At least once

In this semantic, if a producer expects but fails to receive a response indicating that a message was committed, it will resend the message.

Since version 0.11.0.0, the Kafka producer provides an **idempotent** option for configuring message delivery. The idempotent delivery option guarantees that resending a message will not result in duplicate entries in the log, and that log order is maintained. To achieve this, the broker assigns each producer an ID and deduplicates messages using a sequence number that is sent by the producer with every message.

### Exactly once

Starting with version 0.11.0.0, producers can utilize transactional delivery. This means a producer can request acknowledgment that messages were received and successfully replicated, and if it resends a message, it resends with idempotency, meaning existing messages are overwritten rather than duplicated. This comes with **higher latency, but the most durability**.

## Consumer receipt

### At most once

consumer reads a set of messages, saves its position in the log, and then processes the messages. If the consumer process crashes after saving its position, but before saving the output of its message processing, the consumer that takes over processing would start at the saved position and the messages prior to that position would not be processed.

### At least once

This means a consumer reads a set of messages, processes the messages, and then saves its position. In this case, if the consumer process crashes after processing messages, but before saving its position, the new process that takes over may process some messages a second time.

You can assign messages a **primary key**, so that updates are idempotent, meaning that if the message is received twice, it just overwrites the existing record with the same message data.

### Exactly once

Kafka leverages transactional producer capabilities added in version 0.11.0.0 to achieve exactly once semantics.

The consumer’s position is stored as a message in a topic, so offset data in written to Kafka in the same transaction as when processed data is written to the output topics. If the transaction is aborted, the consumer’s position reverts to its old value and you can specify whether output topics are visible to other consumers using the isolation_level property.
