## Overview

Before diving into the specifics of different technology choices for communication, first decide on how services should collaborate with each other: synchronous and asynchronous.

Both modes of communication can enable two different idiomatic styles of collaboration: request/response and event-based. Nonetheless, you are free to mix-and-match as some technologies would fit more naturally into one style or another.

**Communication structures direct how software is created and managed through the life of an organization**.

## Synchronous

Service calls an API that another service exposes, using a protocol such as HTTP or gRPC. This option is synchronous as the caller waits for a response from the receiver. Hence, client code block their thread, until the response reach from the server.

### Request/Response

Client initiates a request and waits for the response. Aligns well to synchronous communication, but can also work for asynchronous communication. For longer-lived processes, could initiate asynchronous requests and wait for callbacks.

Two technologies that fit well when considering this are RPC and REST.

## Asynchronous

The caller doesn't wait for the operation to complete before returning, and may not even care whether or not the operation completes at all. Can have one or more services to process the message asynchronously. Can be useful for long-running jobs or if you require low latency to ensure UI remains responsive even if the network is laggy.

Most popular protocol is AMQP whereby the client sends the message to message broker systems like Kafka and RabbitMQ queue. Can be implemented in a one-to-one mode (queue) or one-to-many mode (topic).

It is important to distinguish between asynchronous I/O and asynchronous protocol. Asynchronous I/O means the calling thread is not blocked while the I/O completes (for performance reasons) which is an implementation detail. An asynchronous protocol means the sender doesn't wait for a response.

### Event-based (pub-sub)

Instead of a client initiating requests asking for things to be done, it instead says "this thing happened" and expects other parties to know what to do. Business logic is not centralized but instead pushed out more evenly to the various collaborators. Highly decoupled as the client that emits an event doesn't have any way of knowing who or what will react to it (subscribers).

## Implementation styles

When considering between request/response and event-based, need to consider how well they are suited for solving a complex problem of handling processes that span across service boundaries and may be long running.

Two approaches are choreography (event-driven) and orchestration (request/response). In reality, most architects would use the amalgamation of both approaches to create a resilient system.

## Best practices

When building a microservices-based application, should minimize communication between them. **If possible, never depend on synchronous communication (request/response) between multiple microservices**, not even for queries. Your services should be designed such that each is able to execute its main function without relying on others.

The goal of each microservice is to be autonomous and available to the client consumer. **If you think you need to make a call from one microservice to other to provide a response, you have an architecture that won't be resilient when some microservices fail**. The more synchronous dependencies between microservices, the worse the overall response time gets for the client apps.

If your microservice needs to raise an additional action or requires data in another microservice, should do it asynchronously by replicating or propagating the data into the initial service's database by using eventual consistency.

Nonetheless, if one microservices needs to perform a synchronous request to get data from another, should call the microservice's API, and not interact with the database directly.

Ultimately, there is no right or wrong. Choose what is best that meets your needs.
