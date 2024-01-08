## Event Sourcing

In a typical traditional persistence model, we store the “current state” of an aggregate on a relational database table. If we are to track any events that happened around the aggregate, we will basically use transaction log files to store them. However, these transactional logs may not give you the complete picture of a transaction state. There are times when we don't just want to see where we are, we also want to know how we got there.

Event Sourcing is a different way of structuring the business logic and persisting aggregates. It persists an aggregate as a sequence of events in an append-only log and each event represents a state change of the aggregate. It ensures that all changes to application state are stored as a sequence of events. An entity’s current state can be created by **replaying** all the events in order of occurrence.

Instead of storing the current state within the application directly field by field in a table in the database, reloading it when needed, and overwriting it by subsequent changes, a **chronologically ordered list of events is persisted**, which can then be used to reconstruct the current state in memory, if necessary.

Event sourcing is an implementation strategy for the persistence of state, e.g. of aggregates. This strategy **should not be exposed beyond the boundaries of aggregates**. The events from event sourcing should therefore only be used **internally** in the corresponding aggregate or in the context of CQRS to build related read models.

### Events

An event represents a fact that took place in the domain. They are the source of truth; your current state is derived from the events. They are **immutable**, and represent the business facts.

An event usually contains unique metadata such as the timestamp of the event, the unique identifier of the subject, etc. The data within the event will be used in the write model to populate the state and make decisions, as well as populate read models.

### Event Store

Event aggregates are stored as a sequence of events in a database known as an Event Store. In this approach, applications can insert or retrieve aggregate events by their primary key. Examples include RDBMS or native event store such as EventStoreDB, RavenDB, MartenDB.

### Event Publishing

Once events are stored in an event store, these events could be published to an Event Broker for its subscribers to consume them further i.e. Kafka.

### Benefits

- The stored events not only describe the current state, but also how this state has been reached
- It is possible at any time to reconstruct any state from the past by replaying the events only up to a certain point in time
- It is conceivable to use event sourcing to handle incorrect processing of previous events or the arrival of a delayed event

### Drawbacks

- The implementation of event sourcing also entails a certain conceptual and technical complexity
- Events are not supposed to change once persisted, whereas the domain logic often evolves over time
