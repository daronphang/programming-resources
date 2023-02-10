## Events

### Unkeyed Event

Unkeyed events are used to describe an event as a singular statement of fact. There is no key involved in this event.

```
Key   Value
N/A   "Hello World" sent by person A
```

### Entity Event

An entity is a unique thing with a unique ID. The entity event describes the properties and state of an entity. The value field contains all the necessary information related to the unique entity.

```
Key         Value
ABC123      Person A
```

### Keyed Event

A keyed event contains a key but does not represent an entity. Keyed events are usually used for partitioning the stream of events to guarantee data locality within a single partition of an event stream.

```
Key         Value
ABC123      "Hello World" sent to Person A
ABC123      "Hello World" sent to Person B
```

## Event Data Definitions and Schemas

Event data serves as the means of long term and implementation agnostic data storage, as well as communciation mechanism between services. Hence, it is important that **both producers and consumers of events have a common understanding of the meaning of data**. The consumer must be able to interpret without consulting the producer.
