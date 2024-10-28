## Functional decomposition

Functional decomposition is the process of taking an application and breaking it down into individual parts i.e. separate services with well-defined responsibility.

### Microservices

One way to split a monolith into a set of independently deployable services is using microservices architecture.

### API gateway

API gateway can be used to manage how clients communicate with the application. For example, A client might need to perform multiple requests to different services to fetch all the information it needs to complete a specific operation.

### CQRS

The API’s gateway ability to compose internal APIs is quite limited, and querying data distributed across services can be very inefficient if the composition requires large in-memory joins. Accessing data can also be inefficient for reasons that have nothing to do with using a microservice architecture:

- Data store used might not be suited for specific types of queries
- Data store might not scale to handle the number of reads

In these cases, decoupling the read path from the write path can yield substantial benefits. An approach is using CQRS pattern.

The two paths can use different data models and data stores that fit their specific use cases i.e. read path using NoSQL, and write using SQL.

To keep the read and write data models synchronized, the write path pushes updates to the read path whenever the data changes. External clients could still use the write path for simple queries, but complex queries are routed to the read path.

### Messaging

When an application is decomposed into services, the number of network calls increases, and with it, the probability that a request’s destination is momentarily unavailable. Messaging is a form of asynchronous communication/transaction.
