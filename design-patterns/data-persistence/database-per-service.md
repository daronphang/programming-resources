## Database-per-service pattern

By deploying this pattern, you choose the most appropriate data stores (i.e. relational or non-relational) for your application and business requirements. This means that:

- Microservices don't share a data layer
- Changes to a database do not impact other microservices
- Individual data stores cannot be directly accessed by other microservices
- Persistent data is accessed only by APIs

For example, 'Sales' uses Amazon Aurora, 'Customer' uses Amazon DynamoDB, and 'Compliance' uses SQL Server.

## Considerations

- Loose coupling is required between microservices
- Microservices have different compliance or security requirements for their databases
- More granular control of scaling is required
- If pattern is used, need to deploy **API composition pattern** or **CQRS pattern** to implement/aggregate queries that span multiple microservices
- 2PC (two-phase commit) protocol does not support this model

## Drawbacks

- Challenging to implement complex transactions and queries that span multiple microservices or data stores
- Data stores must meet two of the CAP theorem: consistency, availability or partition tolerance
