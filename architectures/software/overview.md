## Software architecture

Everything in software architecture is a trade-off. To understand this, developers must understand terminology concerning components, modularity, coupling, and connascence.

When designing a system, don't try to find the best design; instead, strive for the **least worst** combination of trade-offs.

### Characteristics

The architecture characteristics define the success criteria of a system, which is generally orthogonal to the functionality of the system. They include:

- Availability
- Reliability
- Scalability
- Testability
- Security
- Agility
- Fault tolerance
- Elasticity
- Recoverability
- Performance
- Deployability
- Learnability

A common anti-pattern in architecture entails trying to design a generic architecture that supports all characteristics. Each architecture characteristic complicates the overall system design, and supporting too many will lead to greater complexity.

## Importance of data

Data is the most important asset in a company. Businesses want to extract value from the data that they have and are finding new ways to deploy data in decision making i.e. data driven decisions.

One important distinction is the separation between operational and analytical data.

### Operational data

Data used for the operation of the business, including sales, transactional data, inventory, etc. This type of data is defined as Online Transactional Processing (OLTP), which typically involves CRUD operations.

### Analytical data

Data used by data scientists and other business analysts for predictions, trending and other business intelligence. This data is typically not transactional and often not relational i.e. graph database.

## Translation of domain concerns

| Domain Concern           | Architecture Characteristics                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| Mergers and acquisitions | Interoperability, scalability, adaptability, extensibility                                |
| Time to market           | Agility, testability, deployability                                                       |
| User satisfaction        | Performance, availability, fault tolerance, testability, deployability, agility, security |
| Competitive advantage    | Agility, testability, deployability, scalability, availability, fault tolerance           |
| Time and budget          | Simplicity, feasibility                                                                   |

## Architecture decisions

Architecture decisions define the rules for how a system should be constructed i.e. business and service layers within a layered architecture can access the database, restricting the presentation layer from making direct database calls. They **form the constraints of the system and direct the development teams on what is and isn't allowed**.

If a particular architecture decision cannot be implemented in one part of the system due to some condition or other constraint, that decision/rule can be broken through something called a **variance**. Most organizations have variance models that are used by an architecture review board (ARB) or chief architect. Those models formalize the process for seeking a variance to a particular standard or decision.

## Design principles

A design principle differs from an architecture decision in that a design principle is a **guideline** rather than a hard-and-fast rule. For instance, a design principle can be for development teams to leverage asynchronous messaging between services to increase performance.

## Architecture quantum

An architecture quantum is an independently deployable artifact with high functional cohesion, high static coupling, and synchronous dynamic coupling. A common example of an architecture quantum is a well-formed microservice within a workflow.

In other words, the architecture quantum defines a DDD bounded context in the scope of architecture characteristics e.g. performance, scale, elasticity, reliability, etc.

It is obvious how static coupling can affect the quantum; for dynamic coupling, depending on the type of call that was made, you might **temporarily** couple two services together e.g. synchronous.
