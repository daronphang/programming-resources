## Event Brokers vs Message Brokers

Event brokers can be used in place of a message broker, but not vice versa. They are designed around providing an ordered log of facts.

There are two specific needs that message brokers are not able to satisfy: consumption of message and message retention.

Nonetheless, message brokers are valid patterns for EDM architectures, but are not sufficient for the full scope of duties such architectures require.

### Consumption of Message

A message broker provides queues of messages, and applications that share consumption from a queue will each receive only a subset of the records. This makes it impossible to correctly communicate state via events, since each consumer is unable to obtain a full copy of events.

Unlike the message broker, the event broker maintains a single ledger of records and manages individual access via indices, so each independent consumer can access all required events.

### Message Retention

A message broker deletes events after acknowledgement, whereas an event broker retains them for as long as the organization needs.

The deletion of an event after consumption makes a message broker insufficient for providing indefinitely stored, globally accessible, replayable, single source of truth for all applications.

### Event Order

Event order is not maintained when processing from a queue. If a consumer fails to process an event, it will return the event to the queue for processing at a later date.
