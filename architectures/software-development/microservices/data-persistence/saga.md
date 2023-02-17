## Saga Pattern

Saga pattern is a failure management pattern that helps establish consistency in distributed applications, and coordinates transactions between microservices to maintain data consistency.

A saga is sequence of transactions that updates each service and publishes a message/event to trigger the next transaction step. If a step fails, the saga executes compensating transactions that counteract the preceding transactions.

### Transaction

A transaction is a single unit of logic/work, that may be made up of multiple operations. Within a transaction, an **event** is a state change that occurs to an entity, and a **command** encapsulates all information needed to perform an action or trigger a later event.

### Implementation

Two approaches are choreography and orchestration.

### Considerations

- Application needs to maintain data consistency across multiple microservices without tight coupling
- Long-lived transactions should not block others
- Need to rollback an operation if it fails in the sequence

### Drawbacks

- Difficult to debug and complexity increases with the number of microservices
