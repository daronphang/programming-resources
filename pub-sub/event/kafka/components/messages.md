## Messages (records)

The unit of data within Kafka. The data contained within it does not have a specific format or meaning to Kafka, and may have optional pieces of metadata which are referred to as keys.

## Batches

For efficiency, messages are written in batches. A batch is a collection of messages, all of which are being produced to the same topic and partition. Batches are typically **compressed** to provide more efficient transmission of data.

Individual round trips for each message would result in excessive overhead, but this leads to a **trade-off between latency and throughput**. The larger the batches, the longer it takes an individual message to propagate.
