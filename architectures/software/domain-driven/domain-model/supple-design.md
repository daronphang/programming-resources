## Supple design

When software with a complex behavior lacks a good design, it becomes hard to refactor or combine elements. Duplication becomes forced when design elements are monolithic. The project will ultimately be weighted down by its own legacy demands rather than accelerate for development.

Supple design is the complement to deep modeling. Once you’ve dug out implicit concepts and made them explicit, you have the raw material. Through the **iterative cycle** you hammer that material into a useful shape, **cultivating a model that simply and clearly captures the key concerns and shaping a design** that allows a client developer to really put that model to work. Development of the design and code leads to insight that refines model concepts.

The design plays two roles:

- Reveal a deep underlying model that makes its potential clear to clients
- Serve the developer working to change it

For a design to be open to change, it must be easy to understand. The effects of its code must be obvious, so the consequences of a change will be easy to anticipate.

Patterns that tend to lend suppleness to a design include:

- Making composition safe by having assertions and side-effect free functions
- **Intention revealing interfaces** make side-effects explicit, simplify closure of operations and standalone classes
- Cost of change reduced through standalone classes and conceptual contours
- Repeated refactoring eventually leading to suppleness

### Intention revealing interfaces

We want to think about meaningful domain logic. Code that produces the effect of a rule without explicitly stating the rule forces us to think of step-by-step software procedures. If the interface doesn't tell the developer what he needs to know in order to use the object, he has to dig into the internals and **most of the value of encapsulation is lost**.

To obtain the value of explicitly modeling a concept in the form of a class or method, we must give these program elements names that reflect those concepts. The names of classes and methods are great opportunities for improving communication between developers, and for improving the abstraction of the system.

### Side-effect free functions

Side effect refers to any change in the state of the system that will affect future operations. In complex systems, most operations call on other operations. When **deep nesting** is involved, it becomes **very hard to anticipate all the consequences of invoking an operation**.

Nonetheless, you cannot avoid commands in most software systems. The problem can be mitigated in two ways:

- Keep commands and queries strictly segregated in different operations
- Create a new value object which is modified and returned

### Assertions

State post-conditions of operations and invariants of classes and aggregates. If assertions can be coded directly, write unit tests for them.

Clearly stated invariants and pre- and post-conditions allow a developer to understand the consequences of using an operation or object.

### Conceptual contours

When elements of a model or design are embedded in a monolithic construct, their **functionality gets duplicated**. The external interface doesn’t say everything a client might care about. Their meaning is hard to understand, because different concepts are mixed together.

On the other hand, breaking classes and methods down can pointlessly complicate the client, forcing client objects to understanding how tiny pieces fit together.

**Find the conceptually meaningful unit of functionality**, and the design will be both flexible and easily understood.

**Decompose design elements (operations, interfaces, classes, and aggregates) into cohesive units**, taking into consideration your intuition of the important divisions in the domain. Observe the axes of change and stability through successive refactorings and look for the underlying conceptual contours that explain these shearing patterns. Align the model with the consistent aspects of the domain that make it viable in the first place.

### Closure of operations

Where it fits, define an operation whose return type is the same as the type of its argument(s). If the implementer’s has state that is used in the computation, then the implementer is effectively an argument of the operation, so the argument(s) and return value should be of the same type as the implementer. Such an operation is closed under the set of instances of that type. **A closed operation provides a high-level interface without introducing any dependency on other concepts**.

This pattern is most often applied to the operations of a value object. Since the lifecycle of an entity has significance in the domain, you can't just conjure up a new one to answer a question.
