## Strong vs eventual consistency

Strong consistency and eventual consistency are two different models used to manage data consistency in distributed systems, particularly in database systems and data storage services.

## Strong consistency (SC)

- Guarantees that once a write operation is completed, any subsequent read (across replicas) will reflect that latest write
- Preferred for high data integrity and reliability systems (banking), but introduces latency and scalability challenges

## Eventual consistency (EC)

- Guarantees that if no new updates are made to a given piece of data, eventually all accesses will return the last updated value (after some delay)
- Prioritizes performance and availability but sacrifices data consistency for a period of time e.g. social media feeds
