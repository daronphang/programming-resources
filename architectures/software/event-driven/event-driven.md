## Event-Driven Architecture (EDA)

An event-driven architecture consists of event producers that generate a stream of events (publish), and event consumers that listen for the events (subscribe). EDA is a design paradigm centered around the production, detection, and reaction to events. These events signify a change in state or an occurrence that is of interest to the system.

Events are delivered in near real-time, so consumers can respond immediately to events as they occur. Producers are decoupled from consumers i.e. it doesn't know which consumers are listening. Consumers are also decoupled from each other, and each consumer can see all of the events.

Events are not destroyed upon consumption as in message-passing systems, but instead remain readily available for other consumers to read as they require. The services can consume events from input event streams, apply their business logic, and may emit their own output events.

### When to Use This Architecture

- Multiple subsystems must process the same events
- Real-time processing with minimum time lag
- Complex event processing, such as pattern matching or aggregation over time windows
- High volume and high velocity of data, such as IoT

### Benefits

- Producers and consumers are decoupled
- No point-to-point integrations i.e. easy to add new consumers to the system
- Consumers can respond to events immediately as they arrive (**reactive system**)
- Highly scalable and distributed
- Subsystems have independent views of the event stream
- Employs asynchronous communication, enabling systems to be more responsive and efficient

### Drawbacks

- Some systems such as IoT requires guaranteed delivery
- Each consumer type typically runs in multiple instances and this can create a challenge if events must be processed in order, or if the processing logic is not idempotent

## Models

An event-driven architecture can use a pub/sub or an event stream model.

### Pub/Sub

The messaging infrastructure keeps track of subscriptions. When an event is published, it sends the event to each subscriber. After an event is received, it cannot be replayed, and new subscribers do not see the event.

### Event Streaming

Events are written to a log. Events are strictly ordered (within a partition) and durable. Clients don't subscribe to the stream, instead a client can read from any part of the stream. The client is responsible for advancing its position in the stream i.e. a client can join at any time, and can replay events.
