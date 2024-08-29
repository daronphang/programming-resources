## Systems of record and derived data

On a high level, systems that store and process data can be grouped into two broad categories.

### Systems of record

Holds the authoritative version of your data i.e. source of truth. Each fact is represented exactly once (representation is typically **normalized**). If there is any discrepancy between another system and the system of record, the value in the latter is the correct one.

### Derived data systems

Data from this system is the result of taking some existing data from another system and transforming or processing it in some way i.e. cache or duplicate. De-normalized values, indexes, and materialized views also fall into this category.

Although data is redundant, it is often essential for getting good performance on read queries. It is commonly **de-normalized**.

## Type of systems

### Services (online systems)

A service waits for a request or instruction from a client to arrive. When one is received, the service tries to handle it ASAP and sends a response back. Response time and availability are very important.

### Batch processing systems (offline systems)

Takes a large amount of input data, runs a job to process it, and produces some output data. Batch jobs are often scheduled to run periodically. An important building block for building scalable, reliable and maintainable applications.

### Stream processing systems (near real-time systems)

A stream processor consumes inputs and produces outputs (rather than responding to requests). A stream job operates on events shortly after they happen, whereas a batch job operates on a fixed set of input data. This allows stream processing systems to have lower latency than batch processing systems.
