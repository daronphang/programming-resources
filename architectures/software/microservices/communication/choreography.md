## Choreography

Choreography is a way to coordinate communication where participants exchange events without a centralized point of control. With choreography, you inform each part of the system of its job, and let it work out the details. An event broker handles messaging in an asynchronous, loosely coupled manner.

Choreography is common in event-driven microservice architectures. All communications are done through the input and output event streams. A producer does not know who the consumers are, nor what business logic or operations they intend to perform. Hence, **the upstream business logic is fully isolated from the downstream consumers.**

Downside is that the explicit view of the business process is only implicitly reflected in your system. This means additional work is needed to ensure that you can monitor and track that the right things have happened. This can be done by building a monitoring system that explictly matches the view of the business process, but then tracks what each of the services does as independent entities. Nonetheless, this approach is more loosely coupled, flexible and amenable to change.

For example, an e-commerce site completing a customer's checkout process can include sending an email to customer, sending order to the warehouse and creating points balance for rewards program. These tasks do not necessarily have to happen in any particular order, and asynchronous flow suits this process.

<img src="../assets/choreography.PNG">

### Benefits

- Good for simple workflows that require few participants and don't need a coordination logic
- Doesn't require additional service implementation and maintenance
- Doesn't introduce a single point of failure as responsibilities are distributed across participants
- Good support for flexibility and reducing service dependencies
- Allows for simple addition of new steps at the end of the workflow

### Drawbacks

- Workflow can become confusing when adding new steps
- Risk of cyclic dependency between participants
- No simple entry point for accessing the BP context as they are distributed across services (lack of localization of business process context)
- Problematic to insert steps into the middle, or change the order of the workflow
- Relationships between services may be difficult to understand outside the context of the workflow
- Workflows can be brittle 
- Difficult to discern the processing progress of a specific event
