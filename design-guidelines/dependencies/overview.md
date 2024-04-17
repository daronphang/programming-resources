## Why care about dependencies?

A dependency is a risk. For example, if my system requires a Java Runtime Environment (JRE) to be installed and one is not installed, my system will not work.

Dependencies represent risk. Handling that risk has some cost. Through experience, trial and error, or the collective wisdom of a team, you choose to explicitly mitigate that risk, or not.

## Comparison

The Inversion of Control is a fundamental principle used by frameworks to invert the responsibilities of flow control in an application, while Dependency Injection is the pattern used to provide dependencies to an application’s class. For the class and its services to be properly decoupled, the Dependency Inversion Principle should be respected by both the client and the service, always depending on an abstraction.

DI is about how one object acquires a dependency. When a dependency is provided externally, then the system is using DI. IoC is about who initiates the call. If your code initiates a call, it is not IoC, if the container/system/library calls back into code that you provided it, is it IoC.

DIP, on the other hand, is about the level of the abstraction in the messages sent from your code to the thing it is calling. To be sure, using DI or IoC with DIP tends to be more expressive, powerful and domain-aligned, but they are about different dimensions, or forces, in an overall problem. **DI is about wiring, IoC is about direction, and DIP is about shape**.

https://martinfowler.com/articles/dipInTheWild.html#YouMeanDependencyInversionRight

https://martinfowler.com/articles/injection.html
