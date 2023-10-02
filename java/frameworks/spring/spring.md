## Spring

The Spring framework changed to address modern development concerns, including microservices and reactive programming.

### Dependency Injection

At its core, Spring offers a container (Spring application context) that creates and manages application components (beans). These beans are wired together inside the Spring application context to make a complete application.

The act of wiring beans together is known as dependency injection. Rather than have components create and maintain the lifecycle of other beans that they depend on, a dependency-injected application relies on a separate entity (container) to create and maintain all components and inject those into the beans that need them.

On top of its container, Spring and a full portfolio of libraries offer a web framework, a variety of data persistence options, a security framework, integration with other systems, runtime monitoring, microservice support, a reactive programming model, and many other features necessary for modern application development.

### Automatic Configuration

With component scanning, Spring can automatically discover components from an application's classpath and create them as beans in the Spring application context.

With autowiring, Spring automatically injects the components with the other beans that they depend on.
