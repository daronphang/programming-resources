## API composition pattern

This pattern uses an API composer/aggregator to implement a query by invoking individual microservices that own the data i.e. function composition. It then combines the results by performing an in-memory join.

### Drawbacks

- Might not be suitable for complex queries or large datasets that require in-memory joins
- Overall system becomes less available as you scale up the number of microservices
- Increased database requests create more network traffic
