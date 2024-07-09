## Overview

Neither point-to-point request-response microservices nor asynchronous event-driven microservices are strictly better than the other. Both have their place in an organization, and some tasks are far better suited to one over the other. **Hybrid architectures** will certainly be the norm.

## Asynchronous microservices

### Granularity

Services map neatly to bounded contexts and can be easily rewritten when business requirements change.

### Scalability

Individual services can be scaled up and down as needed.

### Technological flexibility

Services use the most appropriate languages and technologies. Allows for easy prototyping using pioneering technology.

### Business requirement flexibility

Ownership of granular microservices is easy to reorganize, and organization can react more quickly to changes in business requirements.

### Loosely coupling

Event-driven microservices are coupled on domain data nad not on a specific implementation API.

### High testability

Microservices tend to have fewer dependencies than large monoliths.

## Synchronous microservices

### Integrations with third-party solutions

Integrations with third-party solutions almost always use a synchronous mechanism and provide a flexible, language-agnostic communication mechanism over HTTP.

### Debugging

Tracing operations across multiple systems can be easier, and allows for high debuggability and visibility into business operations.

### Point-to-point couplings

Synchronous microservices rely on other services to help perform their business tasks, which may in turn, have their own dependent services. This can lead to difficulty in tracing which services are responsible for fulfilling specific parts of the business logic.

### Dependent scaling

The ability to scale up your own service depends on the ability of all dependent services to scale up and is directly related to the degree of communications fanout.

### Service failure handling

If a dependent service is down, decisions must be made about how to handle the exception. Ensuring data consistency becomes increasingly difficult the more services there are in the ecosystem.

### API versioning and dependency management

Multiple API definitions and service versions will often need to exist at the same time. This can add a lot of complexity in orchestrating API changes across multiple services.

### Data access tied to the implementation

Microservices will often still need to access commonly used data from other services. The onus of data access and scalability is put back on the implementation communication structure.

### Distributed monoliths

Services may be composed such that they act as a distributed monolith, with many intertwining calls being made between them. This situation often arises when a team is decomposing a monolith and decides to use synchronous point-to-point calls to mimic the existing boundaries within their monolith.

### Testing

Integration testing can be difficult, as each service requires fully operational dependents, which require their own in turn.
