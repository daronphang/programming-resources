## Stateful Streaming

Stateful streaming underpins the most important components of an event-driven microservice, as most applications will need to maintain some degree of state for their processing requirements.

## State Stores and Materializing State from an Event Stream

Both materialized state and state stores are required and used extensively in stateful microservices.

Each microservice design must also take into account where the service will store its data: internally such as on the disk, or externally across a network.

### Materialized State

A projection of events from the source event stream (immutable). Enables you to use common business entities in your microservice applications. 

### State Store

Where your service's business state is stored (mutable). Enables you to store business state and intermediate computations. 


