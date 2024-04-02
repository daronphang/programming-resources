## Event broker

A system that is the heart of an event-driven microservice platform, and that receives events, stores them in a queue or partitioned event stream, and provides them for consumption by other processes. Examples include Kafka, Spark, Flink or Beam.

## Features

Event broker systems suitable for large-scale enterprises all generally follow the same model. Multiple, distributed event brokers work together in a cluster to provide a platform for the production and consumption of event streams.

### Scalability

Additional event broker instances can be added to increase the cluster's production, consumption and data storage capacity.

### Durability

Event data is replicated between nodes. This permits a cluster of brokers to both preserve and continue serving data when a broker fails.

### High availability

A cluster of event broker nodes enables clients to connect to other nodes in the case of a broker failure.

### High performance

Multiple broker nodes share the production and consumption load.

## Event storage and serving

Minimal requirements of the underlying storage of the data.
