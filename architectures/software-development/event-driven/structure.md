## Event-Driven Communication Structures

An event-streaming data communication structure decouples the production and ownership of data from the access to it. Producers' responsibilities are limited to producing well-defined data into their respective event streams.

### Events are the Basis of Communication

All shareable data is published to a set of event streams, forming a continuous, canonical narrative detailing everything that has happened in the organization. Events are the data, and are not just merely signals indicating data is ready elsewhere. Rather, they act both as a data storage and as a means of asynchronous communication between services.

### Event Streams Provide the Single Source of Truth

Each event in a stream is a statement of fact, and together these statements form the single source of truth. It is critical that the organization adopts the event stream narrative as a single source of truth, as a communication structure is only as good as the veracity of its information.

### Consumers Perform Their Own Modeling and Querying

Data access and modeling requirements are shifted to the consumer, with each consumer obtaining their own copy of events from the source event streams. Consumer remains fully responsible for any mixing of data from multiple event streams, special query functionality, or other business-specific implementation logic.

Both producers and consumers are otherwise relieved of their duty to provide querying mechanisms, data transfer mechanisms, APIs, and cross-team services for the means of communicating data.

## Microservice Single Writer Principle

Each event stream has only one producing microservice i.e. the microservice is the owner of each event produced to that stream. This allows for the authoritative source of truth to always be known for any given event, by permitting the tracing of data lineage through the system.
