## Service-Oriented Architecture

SOA is a method of software development that uses software components called services to create business applications. Each service provides a business capability, and services can also communicate with each other across platforms and languages. Developers use SOA to reuse services in different systems or combine several independent services to perform complex tasks. It defines a way to make software components reusable and interoperable through service interfaces.

A design approach where multiple services (completely separate OS process) collaborate to provide some end set of capabilities. Communication between these services occurs via network calls rather than method calls within a process boundary.

Emerged to combat the challenges of a monolithic application and aims to promote reusability of software i.e. two or more end-user applications.

### Enterprise Service Bus (ESB)

The ESB is a software architectural pattern that supports real-time data exchange between disparate applications i.e. a **centralized** software component performs integrations between applications. Large organizations have multiple applications that perform various functions using diverse data models, protocols, and security restrictions.

ESB performs transformations of data models, handles connectivity and messaging, performs routing, converts communication protocols and potentially manages the composition of multiple requests.

An ESB provides communication and transformation capabilities through a reusable service interface. You can think of an ESB as a centralized service that routes service requests to the appropriate service. It also transforms the request into a format that is acceptable for the service’s underlying platform and programming language.

### Event Bus

Many organizations have moved from ESB to event buses. An event bus is a pipeline that receives events. It connects application components together based on events, which makes it easier for you to build scalable event-driven applications.

Rules associated with the event bus evaluate events as they arrive. Each rule checks whether an event matches the rule's criteria. You associate a rule with a specific event bus, so the rule only applies to events received by that event bus.

A producer publishes an event to the event bus. The event bus filters and evaluates events as they arrive based on pre-configured rules, then pushes the events to consumers. Producer services and consumer services are decoupled, which allows them to be scaled, updated, and deployed independently.

### Benefits

- Faster time to market
- Efficient maintenance
- Greater adaptability
- Interoperability between applications

### Drawbacks

- Limited scalability
- Increasing interdependencies
- Single point of failure

## SOA components

### Service

Services are the basic building blocks of SOA. They can be private—available only to internal users of an organization—or public—accessible over the internet to all. Individually, each service has three main features:

- Service implementation: Code that builds the logic for performing the specific service function, such as user authentication or bill calculation
- Service contract: Defines the nature of the service and its associated terms and conditions
- Service interface: Defines how you can invoke the service to perform activities or exchange data

### Service provider

The service provider creates, maintains, and provides one or more services that others can use.

### Service consumer

The service consumer requests the service provider to run a specific service. It can be an entire system, application, or other service. The service contract specifies the rules that the service provider and consumer must follow when interacting with each other. Service providers and consumers can belong to different departments, organizations, and even industries.

### Service registry

A service registry, or service repository, is a network-accessible directory of available services. It stores service description documents from service providers. The description documents contain information about the service and how to communicate with it. Service consumers can easily discover the services they need by using the service registry.

## SOA vs microservices

The chief differences between the two are the coupling of components and scope of use.

SOA is an integration architectural style and an **enterprise-wide** concept. It enables existing applications to be exposed over loosely coupled interfaces, each corresponding to a business function that enables applications in one part of an extended enterprise to reuse functions in other applications.

Microservices architecture is an **application** architectural style and an application-scoped concept. It enables the internals of a single application to be broken up into small pieces that can be independently changed, scaled and administered. It does not define how applications talk to one another, for that we are back to the enterprise scope of the service interfaces provided by SOA.

SOA is often concerned with interoperability across applications on the enterprise platform and serves as a systemic approach to breaking down the monolith. Microservices employs a similar approach within the various layers of the application itself. **Together, they can form an extremely powerful partnership**.
