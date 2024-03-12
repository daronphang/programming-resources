## Modularity

Modularity describes a **logical grouping of related code**, which could be a group of classes in an OOP language, or functions in a structured/functional language. Most languages provide mechanisms for modularity i.e. package in Java, namespace in .NET, etc.

Key concepts to measuring modularity are cohesion, coupling and connascence (multiple components agreeing on the meaning of particular values).

### Cohesion

Cohesion refers to what extent the parts of a module should be contained within the same module. It is a measure of how related the parts are to one another. Ideally, a cohesive module is one where all the parts should be packaged together, and attempting to divide a cohesive module would only result in increased coupling and decreased readability.

### Coupling

There are two types of coupling:

- Static: Represents how static dependencies resolve within the architecture via contracts
- Dynamic: Represents how quanta communicate at runtime, either synchronously or asynchronously

An easy way to think about the difference is that static coupling describes how services are wired together, whereas dynamic coupling describes how services call one another at runtime.

For example, in a microservices architecture, a service must contain dependent components such as a database, representing static coupling i.e. the service isn’t operational without the necessary data. That service may call other services during the course of a workflow, which represents dynamic coupling. Neither service requires the other to be present to function, except for this runtime workflow. Thus, **static coupling analyzes operational dependencies, and dynamic coupling analyzes communication dependencies**.

#### Analysis

Graph theory can be used to analyze coupling in codebases, as the method calls and returns form a call graph. Moreover, a **reliability analysis** can be performed to determine if something changes, what dependency might break.

Two types of coupling can be measured:

- Afferent coupling: Measures the number of incoming connections to a code artifact
- Efferent coupling: Measures the outgoing connections to other code artifacts

### Connascence

Two components are connascent if a change in one would require the other to be modified in order to maintain the overall correctness of the system.

#### Static

Static connascence refers to source-code-level coupling (as opposed to execution-time coupling). Different types include:

- Connascence of Name: Multiple components must agree on the name of entity
- Connascence of Type: Multiple components must agree on the type of entity
- Connascence of Meaning: Multiple components must agree on the meaning of particular values
- Connascence of Position: Multiple components must agree on the order of values
- Connascence of Algorithm: Multiple components must agree on a particular algorithm

#### Dynamic

Dynamic connascence analyzes calls at runtime. The different types include:

- Connascence of Execution: Order of execution of multiple components is important
- Connascence of Timing: Timing of execution of multiple components is important
- Connascence of Values: Occurs when several values relate on one another and must change together
- Connascence of Identity: Occurs when multiple components must reference the same entity
