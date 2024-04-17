## Entities

Object modeling tends to lead us to focus on the attributes of an object, but the fundamental concept of an entity is an abstract continuity threading through a lifecycle and even multiple forms. An object **defined primarily by its identity** (and not by attributes) is called an entity.

Entities have special modeling and design considerations. They have lifecycles that can radically change their form and content, while a thread of continuity must be maintained. Their class definitions, responsibilities, attributes and associations should revolve around who they are, rather than the attributes they carry.

## Value Objects

Tracking the identity of entities is essential, but **attaching identity to other objects can hurt system performance, add analytical work, and muddle the model by making all objects look the same**. An object that represents a descriptive aspect of the domain that has no conceptual identity is called a value object. Value objects are instantiated to represent elements of the design that we care about only for **what they are, not who they are** i.e. colors.

A value object can be an assemblage of other objects, reference entities, and are often passed as parameters in messages between objects. They are frequently transient, created for an operation and then discarded. Value objects are used as **attributes of entities** i.e. an address (value object) which is part of a customer (entity) is made up of street, city, and state.

When you care only about the attributes of an element of the model, classify it as a value object. Making it express the meaning of attributes it conveys and give it related functionality. **Treat the value object as immutable**.

### When to allow mutability

Immutability is a great simplifier in an implementation, making sharing and reference passing safe. If the value of an attribute changes, you use a different value object, rather than modifying the existing one. Nonetheless, there are cases when performance considerations will favor allowing a value object to be mutable:

- If the value is frequently changed
- If object creation or deletion is expensive
- If replacement will disturb clustering
- If there is not much sharing of values

## Services

There are cases where the clearest and most pragmatic design includes operations that do not conceptually belong to an object. Rather than forcing the issue, we can follow the natural contours of the problem space and include services in the model i.e. domain operations that can't find a natural home in an entity or value object.

A service is an operation (activity) offered as an interface that **stands alone** in the model, without encapsulating state as entities and value objects do. Services are a common pattern in technical frameworks, but they can also apply in the domain layer.

A service should still have a defined responsibility, and that responsibility and the interface fulfilling it should be defined in terms of the domain language.

A good service has three characteristics:

- The operation relates to a domain concept that is not a natural part of an entity or value object
- The interface is defined in terms of other elements in the domain model
- The operation is stateless

### Location

Most services belong in the infrastructure layer, but they can also be used and reside in the domain layer. It is important to distinguish services that belong to the domain layer from those of other layers.
