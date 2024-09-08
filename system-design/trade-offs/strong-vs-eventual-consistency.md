## Strong vs eventual consistency

Strong consistency and eventual consistency are two different models used to manage data consistency in distributed systems, particularly in database systems and data storage services.

## Strong consistency (SC)

SC model guarantees that once a write operation is completed, any subsequent read will reflect that write.

SC is preferred for high data integrity and reliability systems, but introduces latency and scalability challenges i.e. banking.

## Eventual consistency (EC)

In an EC model, system guarantees that if no new updates are made to a given piece of data, eventually all accesses will return the last updated value.

EC prioritizes performance and availability but sacrifices data consistency for a period of time i.e. social media feeds.
