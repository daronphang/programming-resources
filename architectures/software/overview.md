## Software Architecture

Everything in software architecture is a trade-off. To understand this, developers must understand terminology concerning components, modularity, coupling, and connascence.

## Architecture Characteristics

The architecture characteristics define the success criteria of a system, which is generally orthogonal to the functionality of the system. They include:

- Availability
- Reliability
- Scalability
- Testability
- Security
- Agility
- Fault Tolerance
- Elasticity
- Recoverability
- Performance
- Deployability
- Learnability

A common anti-pattern in architecture entails trying to design a generic architecture that supports all characteristics. Each architecture characteristic complicates the overall system design, and supporting too many will lead to greater complexity.

### Translation of Domain Concerns

| Domain Concern           | Architecture Characteristics                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| Mergers and acquisitions | Interoperability, scalability, adaptability, extensibility                                |
| Time to market           | Agility, testability, deployability                                                       |
| User satisfaction        | Performance, availability, fault tolerance, testability, deployability, agility, security |
| Competitive advantage    | Agility, testability, deployability, scalability, availability, fault tolerance           |
| Time and budget          | Simplicity, feasibility                                                                   |

## Architecture Decisions

Architecture decisions define the rules for how a system should be constructed i.e. business and service layers within a layered architecture can access the database, restricting the presentation layer from making direct database calls. They **form the constraints of the sstem and direct the development teams on what is and isn't allowed**.

If a particular architecture decision cannot be implemented in one part of the system due to some condition or other constraint, that decision/rule can be broken through something called a **variance**. Most organizations have variance models that are used by an architecture review board (ARB) or chief architect. Those models formalize the process for seeking a variance to a particular standard or decision.

## Design Principles

A design principle differs from an architecture decision in that a design principle is a **guideline** rather than a hard-and-fast rule. For instance, a design principle can be for development teams to leverage asynchronous messaging between services to increase performance.

## Fitness Functions

Fitness function was initially stated in Evolutionary computing and Genetic Algorithm to guide simulations towards optimal design solutions. Evolutionary computing is all about **guided incremental changes**, in which engineers access the current state and measure how close it is to the desired state.

Fitness function is an object function used to assess how close the output comes to achieving the aim. In other words, it takes a candidate solution to a problem as input and produces as output how 'fit' the solution is with respect to the problem.

Fitness function is any mechanism that provides an objective integrity assessment of some architecture characteristic or combination of architecture characteristics. They are not some new framework for architects to download, but rather a new perspective on many existing tools.

Regardless of the application architecture (monolith, microservices), fitness function-driven development can introduce continuous feedback for architectural conformance and inform the development process as it happens, rather than after the fact.

For example, when using a genetic algorithm to optimize wing design, the fitness function assesses wind resistance, weight, airflow, and other characteristics desirable to good wing design.
