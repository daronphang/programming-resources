## Duplicate Events

### Producer fails to receive acknowledgement from broker

In this scenario, producer still has copies of the evnets to produce in its memory. These events, if published again, may have the same timestamps and event data, but will be assigned new offsets.

### Producer crashes after writing

In this scenario, the producer will have successfully written its events, but will not update its consumer offsets yet. This means that when the producer comes back up, it will repeat the work that it had previously done, creating logically identical copies of the events but with new timestamps. 

## Effectively Once Processing with Transactions

Effectively once processing ensures that any updates made to the single source of truth are consistently applied, regardless of any failure to the producer, consumer or event broker. 

### Idempotent Writes

Idempotent writes are commonly supported among event broker implementations such as Apache Kafka and Apache Pulsar. They allow for an event to be written only once to an event stream.

### Transactions

Full transactional support is offered only by Apache Kafka. This allows a producer to publish its events to multiple event streams in a single, atomic transaction. Transactions are extremely powerful and give Kafka a significant advantage over its competitors. This feature offloads the responsibility of duplication prevention from the consumer.