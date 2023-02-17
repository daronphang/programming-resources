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

## Best Practices

### Tell the Truth

A good event definition provides the complete description of everything that has happened during that event. The output event must be treated as the single source of truth and must be recorded as an immutable fact for consumption by downstream consumers.

### Use a Singular Event Definition per Stream

An event stream should contain events representing a single logical event. Not advisable to mix different types of events within an event stream.

### Use Narrowest Data Types

When using the narrowest data types, it lets you rely on code generators and serialization unit tests to check the boundaries of the data. 

Avoid the following:
- Using string to store a numeric value
- Using integer as a boolean
- Using string as an enum

### Keep Events Single-Purpose

One common anti-pattern is adding a type field to an event definition, where different type values indicate specific subfeatures of the event. This complexity affects not only developers who must maintain and populate these events, but also the data's consumers, who need to have a consistent understanding about what data is published and why.

Instead, should decompose the schema into something more manageable where responsibilities are clearly defined.

```
TypeEnum: Book, Movie

ProductEngagement {
    productId: Long,
    productType: TypeEnum,

    // only applies if productType=movie
    // difficult for consumers to maintain
    // not related to productType=books
    watchedPreview: {null, boolean} 
}
```

### Minimize the Size of Events

When you have a design that produces a very large event, make sure the data is directly related. Additional data may have been added to the event 'just in case'. If all the event data is related, need to define the boundaries and context of the microservice.


### Avoid Events as Semaphores or Signals

These events simply indicate something has happened without being the single source of truth for the results. 

For example, a system that outputs an event indicating that work has been completed. To consume this event properly, need to find where the completed work actually resides, leading to inconsistency with multiple sources of truth.