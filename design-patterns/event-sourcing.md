## Event Sourcing

Event Sourcing is an alternative way to persist data. In contrast with state-oriented persistance, Event Sourcing stores each state mutation as a separate record called an **event**.

This can simplify tasks in complex domains, by avoiding the need to synchronize the data model and the business domain, while improving performance, scalability, and responsiveness. It can also provide consistency for transactional data, and maintain full audit trails and history that can enable compensating actions.

<img src="../assets/event-sourcing.png">

### State-oriented persistence

Since the 1980s, relational databases started to dominate the world of data persistence. However, with the rise of OOP, developers started to struggle to persist objects in relational databases. Such a struggle was known as **"object-relational impedance mismatch"**. Alternative families of databases appeared over the decades to address the mismatch issues, but all that is stored in the database is the **current state** of the system.

Users perform actions called **commands** that trigger updates to data objects, which are then persisted in a database. All DBMSes support four basic operations for persistence: CRUD. System objects usually are persisted as database records i.e. rows in tables or documents. When an object changes, and the change needs to be persisted, the database record gets replaced by a new record.

### Historical record

Often keeping only the current state of an entity is not enough. When such a requirement is present, developers often choose to save a particular update history in a separate table or in transaction log files.

However, these transactional logs may not give you the complete picture of a transaction state. There are times when we don't just want to see where we are, we also want to know how we got there.

Moreover, there is no guarantee that the business won't require keeping the record on other state changes. Hence, all the history before the change that would keep such a record will be lost.

Change history of entities can allow access to previous states, but ignores the meaning of those changes, so that any manipulation of the information is procedural, and often pushed out of the domain layer.

### Events

When a command from a user is received, the event-sourced system will translate it into an event. The event can be used to update any state held in memory, but only the event is stored in the database i.e. WithdrawMoney translated into MoneyWithdrawn.

An event represents a fact that took place in the domain. They are the source of truth; your current state is derived from the events. They are **immutable** (can only be created or read), and represent the business facts.

An event usually contains unique metadata such as the timestamp of the event, the unique identifier of the subject, etc. The data within the event will be used in the write model to populate the state and make decisions, as well as populate read models.

### Explicit mutations as domain events

A domain event is a fully-fledged part of the domain model, a representation of something that happened in the domain.

When we model state changes as domain events, we can make those changes explicit and use the domain language (Ubiquitous Language) to describe the change i.e. order payment received, discount applied, line item removed, etc.

### Entities as event streams

Event Sourcing is the persistence mechanism where each state transition for a given entity is represented as a domain event that gets persisted to an event database (event store). When the entity state mutates, a new event is produced and saved. When we need to restore the entity state, we read all the events for that entity and apply each event to change the state, reaching the correct final state of the entity when all available events are read and applied.

Event Sourcing is a different way of structuring the business logic and persisting aggregates. It persists an aggregate as a sequence of events in an **append-only** log and each event represents a state change of the aggregate. It ensures that all changes to application state are stored as a sequence of events. An entity’s current state can be created by **replaying** all the events in order of occurrence i.e. chronologically ordered list of events.

Event sourcing is an implementation strategy for the persistence of state i.e. of aggregates. This strategy **should not be exposed beyond the boundaries of aggregates**. The events from event sourcing should therefore only be used **internally** in the corresponding aggregate or in the context of CQRS to build related read models.

### Event Store

Event aggregates are stored as a sequence of events in a database known as an Event Store i.e. EventStoreDB, RavenDB, MartenDB.

When you use a relational or document database, you retrieve a single record with the entity id, representing the current entity state. In contrast, when you retrieve an entity from an event database, you get multiple records, and each record is an event.

When we read all events from a single entity stream, we can reconstruct the current state by calling When() for all the events, in sequence.

### Optimizing

In systems with larger volumes of data, you can use RDBMS functionality for implementing Query (CQRS) by storing the current view of the event-sourced data i.e. **projections**.

Alternatively, you can persist the projections or snapshots in-memory, if the number of events is small.

### Event Publishing

Once events are stored in an event store, these events could be published to an Event Broker for its subscribers to consume them further i.e. Kafka.

### Benefits

- The stored events not only describe the current state, but also how this state has been reached
- Inherent atomic operation
- It is possible at any time to reconstruct any state from the past by replaying the events only up to a certain point in time
- It is conceivable to use event sourcing to handle incorrect processing of previous events or the arrival of a delayed event

### Drawbacks

- The implementation of event sourcing also entails a certain conceptual and technical complexity
- Events are not supposed to change once persisted, whereas the domain logic often evolves over time

## Command handling flow

```c#
// Event properties are primitive types or shared complex types.
// These attributes MUST be serializable.
public abstract class Entity {
    List<object> changes;

    public void Apply(object event) {
        When(event);
        changes.Add(event);
    }

    // Each event will mutate the state in-process.
    // This is required for consequent events
    // i.e. ItemAdded and TotalUpdated
    protected abstract void When(object event);
}


public class ItemAdded {
    public string OrderId;
    public Shared.OrderItem Item;
    public double Total;
}

public class Order extends Entity {
    OrderId id;
    OrderItem[] items;
    Money totalAmount;

    public AddItem(OrderItem newItem) {
        if (!CanAddItem(item))
            throw new DomainException("Unable to add the item");

        // Not Event Sourcing if direct mutation of
        // entity state is performed.
        // items.Add(newItem);
        // totalAmount = totalAmount.Add(newItem.LineTotal);

        // An event is produced instead.
        var newTotal = totalAmount.Add(newItem.LineTotal).AsDouble;
        Apply(
            new ItemAdded {
                OrderId = id,
                Item = Map(newItem),
                Total = newTotal
            }
        );
    }

    // For the code that mutates the entity state based on events,
    // it should not have any advanced logic or calculations.
    protected void When(object event) {
        switch (event) {
            case ItemAdded e:
                items.Add(OrderItem.FromEvent(e.Item));
                totalAmount = e.Total;
                break;
            case ItemRemoved e:
                break;
        }
    }
}
```

```c#
public class EntityStore {
    EventDatabase db;
    Serializer serializer;

    public void Save<T>(T entity) where T : Entity {
        var changes = entity.changes;
        if (changes.IsEmpty()) return; // nothing to do

        var dbEvents = new List<DbEvent>();
        foreach (var event in changes) {
            var serializedEvent = serializer.Serialize(event);
            dbEvents.Add(
                data: new DbEvent(serializedEvent),
                type: entity.GetTypeName();
            );
        }
        var streamName = EntityStreamName.For(entity);
        db.AppendEvents(streamName, dbEvents);
    }

    public T Load<T>(string id) where T : Entity {
        var streamName = EntityStreamName.For(entity);
        var dbEvents = db.ReadEvents(streamName);
        if (dbEvents.IsEmpty()) return default(T); // no events

        var entity = new T();
        foreach (var event in dbEvents) {
            entity.When(event);
        }
        return entity;
    }
}
```
