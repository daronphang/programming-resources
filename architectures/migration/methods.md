## Migration Methods

To deprecate a service that has accumulated several years of technical debt, there are two choices.

### Component-based migration

Breaking down the whole system into smaller components. Each component is prioritized according to its place in the flow and the team's needs. Each component is rolled out separately. The components are usually a set of functionality that can be reused by different flows.

One rule that can be set is **unification of data model** i.e. all components will work with a single data model.

### Flow-based migration

There may be multiple flows in the service, based on the line of business (LOB). For this method, the migration is done by doing the design and implementation of a given flow in a single iteration i.e. E2E flow.

### Comparison

|      | Component-based                                                                                                                                                          | Flow-based                                                                                                                                                               |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pros | Iteratively delivering business value Constant feedback loop Sharp focus on a single problem Easier prioritization Easier work parallelization A sense of moving forward | Simple engineering design session per flow, where the end design is clear from scratch Single country-based shadowing and rollout Faster due to reduced rollout overhead |
| Cons | Lack of holistic picture of what we will end up with Multiple country-based verification and rollouts                                                                    | Business value will be delivered at the end of the effort The feedback for a design decision will be received multiple months after it was taken Lack of a focus area    |

## Traffic Shadowing

Traffic shadowing means that every upstream event is ingested by both services (production and new), and the service doing shadowing was just comparing its outcome with the result from the production service without causing any side effects.
