## Monolithic database

Legacy applications typically use a centralized monolithic database but pose the following challenges:

- Schema changes are difficult
- Creates technology lock-in with vertical scaling as the only way to respond to growth
- Imposes a single point of failure
- Prevents you from building decentralized and independent components required for microservices

## Decentralizing data stores

By choosing to decentralize your data stores, you promote **polyglot persistence** among your microservices, and identify your data storage technology based on the data access patterns.

Each microservice has its own data store and can be independently scaled with low-impact schema changes, and data is gated through the microservice's API. This also typically results in eventual data consistency, but pose potential challenges including data synchronization during transactions, transactional integrity, data duplication, joins and latency.

## Patterns

To enable data persistence among microservices, patterns that help include:

- Database-per-service pattern
- API composition pattern
- CQRS pattern
- Event sourcing pattern
- Saga pattern
- Shared-database-per-service pattern
