## Event Data Definitions and Schemas

Event data serves as the means of long term and implementation agnostic data storage, as well as communication mechanism between services. Hence, it is important that **both producers and consumers of events have a common understanding of the meaning of data**. The consumer must be able to interpret without consulting the producer.

## Data Contracts

Best way to enforce data contracts and provide consistency between producer and consumer is to define a schema explicitly. Implicit data contracts are brittle and susceptible to uncontrolled damage.

It may be tempting to build a common library that interprets any given event for all services, but this creates problems with multiple language formats, event evolutions, and independent release cycles. Duplicating efforts across services to ensure a consistent view of implicitly defined data is nontrivial and best avoided completely.

## Schema Changes

Leave the old entities under the old schema in their original event stream. Produce the new and updated entities using the new schema to a new stream. Don't mix different event types in an event stream, especially event types that are evolutionarily incompatible.

Recommended to use explicit schema format that supports controlled schema evolution, such as Apache Avro or Protobuf. JSON is not recommended as it does not provide full-compatibility schema evolution.
