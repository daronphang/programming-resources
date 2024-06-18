## Cadence

Cadence is a distributed, scalable, durable, and highly available **workflow orchestration** engine to execute asynchronous long-running business logic in a scalable and resilient way. It is a fault-tolerant stateful programming model that obscures most of the complexities of building scalable distributed applications.

Cadence fault-oblivious stateful code platform preserves a complete multithreaded application state including thread stacks with local variables across hardware and software failures. It greatly simplifies the coding of complex stateful distributed applications. This allows you to write code using the full power of a programming language while Cadence takes care of durability, availability, and scalability of the application.

The Cadence backend service is stateless and relies on a persistent store. Cassandra, MySQL and Postgres storages are supported.

## Use Cases

### Microservice orchestration and saga

It is common that some business processes are implemented as multiple microservice calls. And the implementation must guarantee that all of the calls must eventually succeed even with the occurrence of prolonged downstream service failures. In some cases, instead of trying to complete the process by retrying for a long time, compensation rollback logic should be executed.

Cadence is a perfect fit for such scenarios. It guarantees that workflow code eventually completes, has built-in support for unlimited exponential activity retries and simplifies coding of the compensation logic. It also gives full visibility into the state of each workflow, in contrast to an orchestration based on queues where getting a current status of each individual request is practically impossible.
