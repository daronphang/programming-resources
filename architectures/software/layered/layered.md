## Layered Architecture (n-tiered)

Domain-driven design isolates the domain with layered architecture. The essential principle is that an element of a layer has dependencies only on other elements in the same layer or on elements of the layers beneath it. Communication upward must be through some indirect mechanism. Most successful architectures have four conceptual layers.

This style is the de facto standard for most applications, primarily because of its simplicity, familiarity, and low cost. However, it also falls into several architectural anti-patterns, including 'architecture by implication' and 'accidental architecture' anti-patterns.

Layers, modules and microservices solve different problems. Microservices are formed around separate functionalities. A layered architecture refers more generally to how one might design the **internal components of an application**. Though a layered architecture style is inherently monolithic, **any microservice application that uses layers should be deployed as a single monolithic unit**.

### Presentation Layer (User Interface)

Responsible for showing information to the user and interpreting user's commands.

### Application Layer

Defines the jobs the software is supposed to do and directs the expressive domain objects to work out problems. The tasks this layer is responsible for are meaningful to the business or necessary for interaction with the application layers of other systems.

This layer is kept thin and does not contain business rules or knowledge, but only coordinates tasks and delegates work to collaborations of domain objects in the next layer down.

### Domain (Model) Layer

Responsible for representing concepts of the business, information about the business situation, and business rules. State that reflects the business situation is controlled and used here.

### Infrastructure Layer

Provide generic technical capabilities that support the higher layers o.e. persistence for the domain, drawing widgets for UI, message sending for the application, etc.

The infrastructure layer may also support the pattern of interactions between the four layers through an architectural framework.
