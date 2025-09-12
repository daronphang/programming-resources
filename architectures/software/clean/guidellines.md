## DTO, domain and database models

In the DTO layer (e.g. Thrift, Protobuf), you should not define domain models directly, but only define DTOs used at this boundary layer. Domain models should remain pure structs in respective language, and often need richer types (time.Time) which otherwise you would be forced to serialize them. Similarly, database models are concerned with how the data is stored.

However, this would mean mapping between DTO to domain, domain to database models is required which can be very verbose and time consuming, but this prioritizes decoupling, maintainability and correctness over convenience.

Nonetheless, this is a guideline and there are pragmatic scenarios where bending the rules is acceptable:

- Early stage projects without strict boundaries, premature abstraction adds friction without benefit
- Domain model carries pure data with no invariants or behavior
- One-to-one mappings with no transformation (identical fields)

Following are some guidelines on model design:

- When designing data schema, model them according to the domain model (business logic), not the database schema nor the DTO schema
- If domain model differs from DTO schema (i.e. fields with native Go types), create them separately in domain model layer
- If how the data is stored in repository differs from domain model, create them separately in repository model layer
- For domain models that has one-to-one mappings with DTO models (no transformation), to reuse respective DTO models across domain

## Function ordering

1. Put exported (capitalized) functions first, followed by unexported (lowercase) helpers
2. Place higher-level orchestration functions before the lower-level utility functions they depend on. This lets readers understand the overall logic first
3. Keep related functions together
