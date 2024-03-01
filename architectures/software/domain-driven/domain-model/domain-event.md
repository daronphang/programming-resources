## Domain event

As we move towards a fully encapsulated domain model, we may start to encounter a very critical word in our conversations with the domain experts: When. This keyword should be a signal to us that there is a potential event in our system.

**Use domain events to explicitly implement side effects across multiple aggregates**. Optionally, for better scalability and less impact in database locks, use **eventual consistency** between aggregates within the same domain.

An event is something that has happened in the past. A domain event is, something that happened in the domain that you want other parts of the same domain (in-process) to be aware of i.e. DTO (data transfer object). A domain event captures the memory of something interesting which affects the domain. The notified parts usually react somehow to the events.

An important benefit of domain events is that side effects can be expressed explicitly with DomainEvent and DomainEventHandler. Without events, the code that is triggered by an event will be tightly coupled to the rule.

It's important to ensure that, just like a database transaction, either all the operations related to a domain event finish successfully or none of them do. Also, domain events should be **immutable**, as they are events in the past.

For synchronous messaging across disconnected aggregates, domain events are a great way to **ensure aggregate root consistency across the entire model**.

### Domain event vs messaging-style events

Both are similar but with one important difference. With message brokers, a message is sent asynchronously and communicated across processes and machines. This is useful for integrating multiple Bounded Contexts, microservices, or even different applications.

However, with domain events, you want to raise an event from the domain operation you're currently running, but you want any side effects to occur within the same domain.

### Domain event vs integration event

Both are the same thing, but their implementations are different. Domain events can be asynchronous or synchronous. However, integration events should always be asynchronous.

The purpose of integration events is to propagate committed transactions and updates to additional subsystems, whether they are other microservices, Bounded Contexts or even external applications. Hence, they should occur only if the entity is successfully persisted, otherwise it's as if the entire operation never happened.

### Domain event dispatcher

One approach is a real messaging system or even an event bus, possibly based on a service bus as opposed to in-memory events. However, for the first case, real messaging would be overkill for processing domain events, since you just need to process those events within the same process (that is, within the same domain and application layer).

To tackle this complexity, it is generally acceptable and much easier to handle domain events **within the same process and transaction scope** that they were published from. For handling processes that do require asynchronous behavior and aggregates in different sub-domains or microservices, integration events can be published using a Message Broker/Event Bus.

### Transaction involving multiple aggregates

There are two approaches:

1. Single transaction across aggregates
2. Eventual consistency across aggregates

Eric Evans advocates the rule that one transaction per aggregate and hence, argue for eventual consistency. Any rule that spans Aggregates will not be expected to be up-to-date at all times. Through event processing, batch processing, or other update mechanisms, other dependencies can be resolved within some specific time.

This rationale is based on embracing fine-grained transactions instead of transactions spanning many aggregates or entities. The idea is that in the second case, the number of database locks will be substantial in large-scale applications with high scalability needs.

### Example

```java
public Payment RecordPayment(
    decimal paymentAmount,
    IBalanceCalculator balanceCalculator
) {
    var payment = new Payment(paymentAmount, this);
    _payments.Add(payment);

    Balance = balanceCalculator.Calculate(this);
    // Static dependency.
    // Domain event is dispatched immediately.
    // Makes testing difficult because of side effects.
    if (Balance == 0) DomainEvents.Raise(new FeePaidOff(this));
    return payment;
}

public class FeePaidOff : IDomainEvent {
    public FeePaidOff(Fee fee) {
        Fee = fee;
    }

    public Fee Fee { get; private set; }
}

public class FeePaidOffHandler : IHandler<FeePaidOff> {
    private readonly ICustomerRepository _customerRepository;
    public FeePaidOffHandler(ICustomerRepository customerRepository) {
        _customerRepository = customerRepository;
    }

    public void Handle(FeePaidOff args) {
        var fee = args.Fee;
        var customer = _customerRepository.GetCustomerChargedForFee(fee);
        customer.UpdateAtRiskStatus();
    }
}

public class Customer {
    public bool IsAtRisk { get; private set; }

    public void UpdateAtRiskStatus() {
        var totalWithOutstandingBalance = Fees.Count(fee => fee.HasOutstandingBalance());
        IsAtRisk = totalWithOutstandingBalance > 3;
    }
}
```

## Domain events as a preferred way to trigger side effects across multiple aggregates within the same domain

If executing a command related to one aggregate instance requires additional domain rules to be run on one or more additional aggregates, you should design and implement those side effects to be triggered by domain events.

Alternatively, you can have the aggregate root subscribed for events raised by members of its aggregates (child entities).

For instance of salesOrder, each OrderItem child entity can raise an event when the item price is higher than a specific amount, or when the product item amount is too high. The aggregate root can then receive those events and perform a global calculation or aggregation.

It's important to understand that this event-based communication is not implemented directly within the aggregates; you need to implement **domain event handlers**.

Handling the **domain events is an application concern**. The domain model layer should only focus on the domain logic: things that a domain expert would understand, not application infrastructure like handlers and side-effect persistence actions using repositories. Therefore, the application layer level is where you should have domain event handlers triggering actions when a domain event is raised.

If you use domain events, you can create a fine-grained and decoupled implementation by segregating responsibilities using this approach:

1. Send a command e.g. CreateOrder
2. Receive the command in a command handler
   - Execute a single aggregate's transaction
   - Raise domain events for side effects
3. Handle domain events (within the current process) that will execute an open number of side effects in multiple aggregates or application actions
   - Verify or create buyer and payment method
   - Send email to buyer

## A better domain events pattern

The need for domain events comes from a desire to inject services into domain models. What we really want is to create an encapsulated domain model, but decouple ourselves from potential side effects and isolate those explicitly.

Typically, the side effects of a domain event should occur within the same logical transaction, but not necessarily in the same scope of raising the domain event. Hence, we need to be aware of **static, opaque dependencies**.

Instead of dispatching to a domain event handler immediately, we could record the domain events (e.g. saving to a collection), and before committing the transaction, to dispatch those domain events. Dispatching can be done synchronously or asynchronously.

### Example

```java
public Payment RecordPayment(
    decimal paymentAmount,
    IBalanceCalculator balanceCalculator
) {
    var payment = new Payment(paymentAmount, this);
    _payments.Add(payment);
    Balance = balanceCalculator.Calculate(this);
    if (Balance == 0) Events.Add(new FeePaidOff(this));
    return payment;
}

// Dispatching domain events before committing transaction.
public override int SaveChanges() {
    var domainEventEntities = ChangeTracker.Entries<IEntity>()
        .Select(po => po.Entity)
        .Where(po => po.Events.Any())
        .ToArray();

    foreach (var entity in domainEventEntities) {
        var events = entity.Events.ToArray();
        entity.Events.Clear();
        foreach (var domainEvent in events) {
            _dispatcher.Dispatch(domainEvent);
        }
    }
    return base.SaveChanges();
}
```

```java
[Test]
public void Should_notify_when_the_balance_is_paid_off() {
    Fee paidOffFee = null;
    var customer = new Customer();
    var fee = customer.ChargeFee(100m);
    fee.RecordPayment(100m, new BalanceCalculator());
    var paidOffEvent = fee.Events.OfType<FeePaidOff>().SingleOrDefault();

    paidOffEvent.ShouldNotBeNull();
    paidOffEvent.Fee.ShouldEqual(fee);
}
```
