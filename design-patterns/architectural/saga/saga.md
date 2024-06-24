## Saga Pattern

Saga pattern is a failure management pattern that helps establish consistency in distributed applications, and coordinates transactions between microservices to maintain data consistency.

A saga is sequence of transactions that updates each service and publishes a message/event to trigger the next transaction step. If a step fails, the saga executes compensating transactions that counteract the preceding transactions.

Every workflow that architects need to model in software has a certain amount of **semantic coupling**: the inherent coupling that exists in the problem domain.

The semantic coupling of a workflow is mandated by the domain requirements of the solution and must be modeled somehow. However clever an architect is, they cannot reduce the amount of semantic coupling, but their **implementation choices may increase it**.

The major lesson of the last decade of architecture design is to **model the semantics of the workflow as closely as possible with the implementation**.

### Transaction

A transaction is a single unit of logic/work, that may be made up of multiple operations. Within a transaction, an **event** is a state change that occurs to an entity, and a **command** encapsulates all information needed to perform an action or trigger a later event.

### Considerations

- Application needs to maintain data consistency across multiple microservices without tight coupling
- Long-lived transactions should not block others
- Need to rollback an operation if it fails in the sequence

### Drawbacks

- Difficult to debug and complexity increases with the number of microservices

## Implementation

Two approaches are choreography and orchestration.

### Orchestration

<img src="../assets/orchestration.png">

### Choreography

When an error occurs, each service must issue compensating messages to other services. Each error scenario forces domain services to interact with each other, adding communication links that weren’t necessary for the happy path.

<img src="../assets/choreography.png">

## Workflow state management

Most workflows include transient state about the status of the workflow. For orchestrated solutions, the workflow state owner is the orchestrator. For choreography, no obvious owner exists. Nonetheless, there are common options that exist to manage state in choreography.

### Front controller pattern

This pattern places the responsibility for state on the first called service in the chain of responsibility. If that service contains information about the state of the workflow, some of the domain services must have a communication link to query and update the order state.

While this simplifies the workflow, it increases communication overhead.

<img src="../assets/front-controller-pattern.png">

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>

<tr>
<td>Creates a pseudo-orchestrator within choreography</td>
<td>Adds additional workflow state to a domain service</td>
</tr>

<tr>
<td>Makes querying the state of an order trivial</td>
<td>Increases communication overhead</td>
</tr>

<tr>
<td></td>
<td>Detrimental to performance and scale as it increases integration communication chatter</td>
</tr>
</table>

### Stateless choreography

A second way for an architect to manage the transactional state is to keep no transient workflow state at all, relying on querying the individual services to build a real-time snapshot.

However, this greatly increases network overhead in terms of chatter between services to build a stateful snapshot. If the client wants to know the state of their workflow, the architect must build a workflow that **queries the state of each domain service** to determine the most up-to-date status.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>

<tr>
<td>Offers high performance and scale</td>
<td>Workflow state must be built on the fly</td>
</tr>

<tr>
<td>Extremely decoupled</td>
<td>Complexity rises swiftly with complex workflows</td>
</tr>
</table>

### Stamp coupling

A third solution utilizes stamp coupling storing extra workflow state in the message contract sent between services. Each domain service updates its part of the overall state and passes that to the next in the chain of responsibility. Thus, any consumer of that contract can check on the status of the workflow without querying each service.

Nonetheless, this is a partial solution, as it still does not provide a single place for users to query the state of the ongoing workflow.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>

<tr>
<td>Allows domain services to pass workflow state without additional queries to a state owner</td>
<td>Contracts must be larger to accommodate workflow state</td>
</tr>

<tr>
<td>Eliminates the need for a front controller</td>
<td>Doesn't provide just-in-time status queries</td>
</tr>
</table>

## Trade-offs

### State owner and coupling

In the choreographed solution, removing the mediator forces higher levels of communication between services. This might be a perfectly suitable trade-off. For example, if an architect has a workflow that needs higher scale, responsiveness and typically has few error conditions, it might be worth trading the higher scale of choreography with the complexity of error handling.

However, as workflow complexity goes up, the need for an orchestrator rises proportionally. Also, the more semantic complexity contained in a workflow, the more utilitarian an orchestrator is.

## Saga state machines

A state machine is a pattern that describes all of the possible paths that can exist within a distributed architecture. A state machine always starts with a beginning state that launches the transactional saga, then contains transition states and corresponding action that should occur when the transition state happens.

The choice between using compensating updates or state management for distributed transaction workflows depends on the situation as well as trade-off analysis between responsiveness and consistency. Regardless of the technique used to manage errors within a distributed transaction, the state of the distributed transaction should be known and also managed.

## Saga pattern compensation workflows

Not all workflows need to be perfectly reversible and constrained by transactions. Ticketing and inventory-based systems often use this approach. For instance, a website selling products may not have sufficient inventory at the time of purchase due to concurrent transactions.

### Strict

Strict transaction-based approach would require that recent transactions be rolled back i.e. money returned to payment provider, customer alerted that order has been cancelled, etc. However, this could lead to a poor customer experience and a lack of trust between the customer and retailer.

### Compensation

As a form of compensation, the business could order new stock, notify the customer that there has been a delay, and offer a discount code for the next purchase as an apology.

## Atomic transactions and compensating updates

The issue with atomic distributed transactions is that the end user is unnecessary semantically coupled to the business process.

The lack of transaction isolation can induce **side effects** within distributed architectures. If a transaction is reversed, actions performed by other services using data from prior update may have already taken place and cannot be reversed.

Another issue regarding compensating updates is compensation failures. This may result in confusion about what sort of response to send back to the end user.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>

<tr>
<td>All data restored to prior state</td>
<td>No transaction isolation</td>
</tr>

<tr>
<td>Allows retries and restart</td>
<td>Side effects may occur on compensation</td>
</tr>

<tr>
<td></td>
<td>Compensation may fail</td>
</tr>

<tr>
<td></td>
<td>Poor responsiveness for the end user when errors or compensating updates take place</td>
</tr>
</table>
