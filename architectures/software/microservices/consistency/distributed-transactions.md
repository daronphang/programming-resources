## Distributed transactions

A distributed transaction is one that spans across two or more microservices. Each microservice is responsible for processing its portion of the transaction, as well as reversing that processing in the case that the transaction is aborted/reverted. **Both the fulfillment and reversal logic must reside within the same microservice i.e. retry policy, error handling, intermittent failure management, etc.**

It is best to avoid implementing distributed transactions whenever possible, as they can add significant risk and complexity to a workflow.

Distributed transactions in an event-driven world are often known as sagas, and can be implemented through either a choreographed or an orchestrator pattern. Both the regular processing and reverting actions should be idempotent, such that any intermittent failures of the participating microservices do not leave the system in an inconsistent state.

## Saga Pattern (Choreographed)

The choreographed saga pattern is suitable for simple distributed transactions. However, monitoring the progress of a choreographed transaction can be difficult, as it requires a full materialization of each participating event stream.

This requires consumer to listen to streams from the first and last service, in the event of a rollback or success without violating the Single Writer Principle.

## Saga Pattern (Orchestrated)

The centralized nature of the orchestrator allows for close monitoring of the progress and state of any given transaction.

Once the transaction has been rolled back, it is up to the orchestrator to decide what to do next to finalize the processing of that event i.e. retry, discard, terminate the application, or output a failure event. The orchestrator is the single producer and publishes the transaction failure to the output stream.

Orchestrated transactions offer better visibility into workflow dependencies, more flexibility for changes, and clearer monitoring options than choreographed transactions.

## Compensation Workflows

Not all workflows need to be perfectly reversible and constrained by transactions. Ticketing and inventory-based systems often use this approach. For instance, a website selling products may not have sufficient inventory at the time of purchase due to concurrent transactions.

### Strict

Strict transaction-based approach would require that recent transactions be rolled back i.e. money returned to payment provider, customer alerted that order has been cancelled, etc. However, this could lead to a poor customer experience and a lack of trust between the customer and retailer.

### Compensation

As a form of compensation, the business could order new stock, notify the customer that there has been a delay, and offer a discount code for the next purchase as an apology.
