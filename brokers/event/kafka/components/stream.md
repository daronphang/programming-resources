## Kafka Stream

In Kafka, a stream processor is anything that takes continual streams of data from input topics, performs some processing on this input, and produces continual streams of data to output topics.

You can do simple processing directly using the producer and consumer APIs. However for more complex transformations, Kafka provides Kafka Streams.

For example, a ride-share application might take in input streams of drivers and customers, and output a stream of rides currently taking place.

Kafka Streams provides a client library for building mission-critical real-time applications and microservices, where the input and/or output data is stored in Kafka clusters. You can build applications with Kafka Streams that does non-trivial processing tasks that compute aggregations off of streams or join streams together.

Streams help solve problems such as: handling out-of-order data, reprocessing input as code changes, performing stateful computations, etc.
