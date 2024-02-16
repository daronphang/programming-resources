## Lifecycle of Domain Object

For complicated objects that have longer lives (some are not spent in active memory), managing these 'persistent' objects presents challenges that can easily derail an attempt at model-driven design.

The problems fall into two categories:

- Maintaining integrity throughout the lifecycle
- Preventing the model from getting swamped by the complexity of managing the lifecycle

Three patterns will address these issues: aggregates, factories and repositories.

## Patterns

Modeling aggregates and adding factories and repositories to the design gives us the ability to manipulate the model objects systematically and in meaningful units throughout their lifecycle:

- Aggregates mark off the scope within which invariants have to be maintained at every stage of the lifecycle
- Factories and repositories operate on aggregates, encapsulating the complexity of specific lifecycle transitions

## Aggregates

An aggregate is a cluster of associated objects that we **treat as a unit for the purpose of data changes**. Examples include:

- In an e-commerce system: an order, line items, and customer
- In a banking system: an account, account transactions, and customer
- In a healthcare system: a patient, his medical history, and his prescriptions

Each aggregate has:

- Root: Single specific entity contained in the aggregate (only member that outside objects are allowed to hold references to)
- Boundary: Defines what is inside the aggregate (hidden from outside)

Aggregates tighten up the model itself by defining clear ownership and boundaries, avoiding a chaotic tangled web of objects. This is crucial to maintaining integrity in all phases of the lifecycle.

Aggregates are the basic element of transfer of data storage which always need to be consistent - you request to load or save whole aggregates inside a transaction. **Transactions should not cross aggregate boundaries**.

## Factories

When creation of an object, or an entire aggregate becomes complicated or reveals too much of the internal structure, factories provide encapsulation.

Much of the power of objects rests in the intricate configuration of their internals and their associations. An object that expresses some model concept should be distilled to the point that nothing remains that does not relate to its meaning or support its role in those interactions. Problems arise from giving a complex object responsibility for its own creation.

A **client taking on object creation becomes unnecessarily complicated** and blurs its responsibility. It breaches the encapsulation of the domain objects and aggregates being created. If the client is expected to assemble the domain objects it needs, it must know something about the internal structure of the object.

Complex object creation is a **responsibility of the domain layer** that does not belong to the objects that express the model. It has no meaning in the domain, but is a **necessity of the implementation**.

A factory encapsulates the knowledge needed to create a complex object or aggregate. It provides an interface that reflects the goals of the client and an abstract view of the created object. Hence, **shift the responsibility for creating instances of complex objects and aggregates to a separate object**.

Factories are used to create and reconstitute complex objects and aggregates, keeping their internal structure encapsulated i.e. a factory encapsulates the lifecycle transitions of creation and reconstitution.

### Designing the interface

When designing the interface, keep in mind these pointers:

- Each operation must be atomic
- Factory will be coupled to its arguments
- Factory is responsible for ensuring all invariants are met for the object or aggregate it creates

## Repositories

Repositories address the middle and end of the lifecycle, providing the means of finding and retrieving persistent objects while encapsulating the immense infrastructure involved.

The goal of domain-driven design is to create software by focusing on a model of the domain rather than the technology. A client needs a practical means of acquiring references to preexisting domain objects. However, if clients use the database directly, developers are tempted to bypass model features like aggregates, directly taking and manipulating what they need.

Most objects should not be accessed by a global search. Yet, a subset of persistent objects must be globally accessible through a search based on object attributes. Such access is needed for the roots of aggregates that are not convenient to reach by traversal i.e. entities or value objects with complex internal structure. Free database queries can actually breach the encapsulation of domain objects and aggregates. Exposure of technical infrastructure and database access mechanisms complicates the client and obscures the model-driven design.

A repository represents all objects of a certain type as a conceptual set. It acts like a collection, except with **more elaborate querying capability**. Objects of the appropriate type are added and removed, and the machinery behind the repository inserts them or deletes them from the database. This definition gathers a cohesive set of responsibilities for providing access to the roots of aggregates from early-lifecycle through the end.

Clients request objects from the repository using query methods that select objects based on criteria specified by the client, typically specifying the value of certain attributes. The repository retrieves the requested object, encapsulating the machinery of database queries and metadata mapping.

Hence, **keep the client focused on the model, delegating all object storage and access to the repositories**. For each type of object that needs global access:

- Create an object that can provide the illusion of an in-memory collection of all objects of that type
- Set up access through a well-known global interface
- Provide methods to add and remove objects, which will encapsulate the actual insertion or removal of data in the data store
- Provide methods that select objects based on some criteria, and return fully instantiated objects or collections of objects whose attribute values meet the criteria, thereby encapsulating the actual storage and query technology

The easiest repository to build has hard-coded queries with specific parameters. However, for projects with a lot of querying, more supportive infrastructure such as a **repository framework** can be built to allow more flexible queries.

### Advantages

- Simple concept for obtaining persistent objects and managing their lifecycle
- Decouples application and domain design from persistence technology, multiple database strategies, or even multiple data sources
- Communicates design decisions about object access
- Easy substitution of dummy implementation, for use in testing, using in-memory collection

### Designing objects for relational databases

The database is more intimately related to the object model than most other components as it is storing the persistent form of the data tha makes up the objects themselves.

When the database is being viewed as an object store, **don't let the data model and object model diverge far**, regardless of the powers of mapping tools. Sacrifice some richness of object relationships to keep close to the relational model. Compromise some formal relational standards if it helps to simplify object mapping i.e. normalization.

Processes outside the object system **should not access an object store**. They could violate the invariants enforced by the objects. Also, their access will lock in the data model which could make it difficult to refactor objects.
