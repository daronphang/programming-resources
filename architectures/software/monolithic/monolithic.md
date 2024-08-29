## Monolithic

Approach is considered to be a default/traditional model for creating a software application i.e. built as a single and indivisible unit. Such a solution usually comprises a client-side user interface, a server-side application, and a database.

Monolithic applications have one large code base and lack modularity. Updates will require changes to the entire stack.

### Strengths

- Less cross-cutting concerns such as logging, handling, caching, performance monitoring
- Easier debugging and testing and for running E2E tests
- Simple to deploy and develop

### Drawbacks

- Scaling increases complexity and may be difficult to understand
- Harder to implement changes and overall development process takes much longer
- Continuous deployment is difficult
- Unable to scale components independently
- Difficult to apply a new technology as the entire application has to be rewritten (new technology barrier)

## Why Monolith exists

Under various circumstances, a monolithic application that provides numerous capabilities in one package may still make sense in the following settings:

- Domain and domain boundaries are unknown
- Provided capabilities are tightly coupled, and performance of module interactions takes precedence over flexibility
- Scaling requirements for all related capabilities are known and consistent
- Functionality isn't volatile; change is slow, limited in scope, or both
