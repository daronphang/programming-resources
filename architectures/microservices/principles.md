## Principles

While it is impossible to cover all of the good practices and design in detail, the following are some key principles to consider when designing your services.

### Model around business concepts

Microservices should be organized around a business capability or domain (DDD), not technical functions. Creating more services does not mean it is following microservice architecture, but still monolithic if services are tightly coupled. This ensures that the service aligns with business goals and can evolve independently. Design them around bounded contexts, which ensures that the service owns its own model, data, and logic.

Interfaces structures around business-bounded contexts are more stable than those structured around technical concepts.

### Loose coupling and high cohesion

Microservices should be loosely coupled, meaning that each service should not have direct dependencies on other services' internal implementations. Use well-defined APIs (e.g., REST, GraphQL) for communication.

Each microservice should have high cohesion, meaning that the services are focused on a specific domain or functionality and contain everything needed to manage that functionality.

### Be mindful of Hyrum's law

Be mindful of Hyrum's law when building APIs: all observable behaviors of your system will be depended on by somebody, e.g. content of error messages, ordering in responses, deprecated features, etc.

### Adopt a culture of automation

Microservices add a lot of complexity, and key part of which comes from the sheer number of moving parts we have to deal with. Embracing a culture of automation is a key way to address this.

Think about creating custom images to speed up deployment, and embracing the creation of fully automated immutable servers to make it easier to reason about your systems.

### Hide internal implementation details

To maximize the ability of one service to evolve independently of any others, it is vital that we hide implementation details e.g. hiding database schema/type, frameworks, libraries, communication protocols, technical error messages, algorithms used, etc. Otherwise, it makes it harder to evolve and maintain over time. Modeling bounded contexts can help, as this helps us focus on those models that should be shared, and those that should be hidden.

Services should hide their databases to avoid falling into one of the most common sorts of coupling that can appear in monolithic architectures and use data pumps for reporting purposes.

```
Exposing database schema to clients:
GET /api/products/{productId}/db/details
```

When possible, pick technology-agnostic APIs to give you freedom to use different technology stacks such as REST.

### Decentralize all things

To maximize the autonomy that microservices make possible, need to be constantly looking for the chance to delegate decision making and control to the teams that own the services themselves.

Ensuring teams own their services is an important step on this journey, making teams responsible for the changes that are made, and having them decide when to release the changes.

Prefer choreography over orchestration and dumb middleware, with smart endpoints to ensure that you keep associated logic and data within service boundaries, and helping keep things cohesive.

### Independently deployable

Should always strive to ensure that our microservices can and are deployed by themselves. It should be the norm that you can make a change to a single service and release it into production, without having to deploy any other services in lock-step.

By adopting a one service-per-host model, you reduce side effects that could cause deploying one service to impact another unrelated service. Consider using blue/green or canary release techniques to separate deployment from release.

### Resilience

Design microservices with resilience in mind. For instance, isolate failures, use timeouts appropriately, implement circuit breakers to limit the fallout of a failing component.

When using network calls, don't treat remote calls like local calls, as this will hide different sorts of failure mode. Make sure timeouts are set appropriately. Understand when and how to use bulkheads and circuit breakers to limit the fallout of a failing component.

### Highly observable

We cannot rely on observing the behavior of a single service instance to see if the system is functioning correctly. Instead, use semantic monitoring and aggregate logs so that when you see a problem, you can drill down to the source.

### Caching

Implement caching when necessary to avoid heavy computation recalculations, eliminate needless round-trips to databases, etc. Keep caching simple and this also increases staleness of data.

### Know when to follow microservices pattern

When deploying new and untested features, whereby consumer benefits are still uncertain: it is reasonable to start with monolithic architecture. At this early stage, the need for ongoing maintenance or additional features is not yet clear. However, as the platform matures and stabilizes, it is important to plan for a transition to microservices, ensuring greater scalability, modularity, and long-term maintainability.
