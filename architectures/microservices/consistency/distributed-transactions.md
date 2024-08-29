## Distributed transactions

A distributed transaction is one that spans across two or more microservices. Each microservice is responsible for processing its portion of the transaction, as well as reversing that processing in the case that the transaction is aborted/reverted. **Both the fulfillment and reversal logic must reside within the same microservice i.e. retry policy, error handling, intermittent failure management, etc.**

It is best to avoid implementing distributed transactions whenever possible, as they can add significant risk and complexity to a workflow.

## Eventual consistency

Distributed architectures rely heavily on eventual consistency as a trade-off for better operational architecture characteristics such as performance, scalability, elasticity, fault tolerance, and availability.

## Background synchronization pattern

The background synchronization pattern uses a separate external service or process to periodically check data sources and keep them in sync with one another. The length of time for data sources to become eventually consistent can vary depending on whether the process is implemented as a batch job or periodically.

One of the challenges of this pattern is that the background process used to keep all the data in sync must know what data has changed. This can be done through an event stream, a database trigger, or reading data from source tables and aligning target tables with source data.

However, the biggest disadvantage is that it **couples all of the data sources together**, breaking every bounded context between the data and services. The process must have write access to all tables owned by the corresponding services, meaning the tables effectively have shared ownership with the background process.

Also, particular operations may have business rules, and this logic must be replicated in the background process.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>

<tr>
<td>Services are decoupled</td>
<td>Data source coupling</td>
</tr>

<tr>
<td>Good responsiveness</td>
<td>Complex implementation</td>
</tr>

<tr>
<td></td>
<td>Breaks bounded contexts</td>
</tr>

<tr>
<td></td>
<td>Business logic may be duplicated</td>
</tr>

<tr>
<td></td>
<td>Slow eventual consistency</td>
</tr>
</table>

## Orchestrated request-based pattern

A common approach for managing distributed transactions is to make sure all of the data sources are synchronized during the course of the business request.

Distributed transactions in an event-driven world are often known as sagas, and can be implemented through either a choreographed or an orchestrator pattern. Both the regular processing and reverting actions should be idempotent, such that any intermittent failures of the participating microservices do not leave the system in an inconsistent state.

### Saga pattern (orchestrated)

The centralized nature of the orchestrator allows for close monitoring of the progress and state of any given transaction.

Once the transaction has been rolled back, it is up to the orchestrator to decide what to do next to finalize the processing of that event i.e. retry, discard, terminate the application, or output a failure event. The orchestrator is the single producer and publishes the transaction failure to the output stream.

Orchestrated transactions offer better visibility into workflow dependencies, more flexibility for changes, and clearer monitoring options than choreographed transactions.

## Event-based pattern

With this pattern, events are used in conjunction with an asynchronous pub/sub messaging model to post events or command messages.

The eventual consistency time for this pattern is usually short because of the parallel and decoupled nature of asynchronous message processing.

### Saga pattern (choreographed)

The choreographed saga pattern is suitable for simple distributed transactions. However, monitoring the progress of a choreographed transaction can be difficult, as it requires a full materialization of each participating event stream.

This requires consumer to listen to streams from the first and last service, in the event of a rollback or success without violating the Single Writer Principle.
