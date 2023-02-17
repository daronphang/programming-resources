## Concepts

### Domain

The problem space that a business occupies and provides solutions to. This encompasses everything that the business must contend with, including rules, processes, ideas, business-specific terminology, and anything related to its problem space. The domain exists regardless of the existence of the business.

### Subdomain

Each subdomain focuses on a specific subset of responsibilities and typically reflects some of the business's organizational structure i.e. Warehouse, Sales, Engineering, etc.

### Domain and Subdomain Model

An abstraction of the actual domain useful for business purposes. The pieces and properties of the domain that are most important to the business are used to generate the model. Models often need to be refined as the domain changes and as business priorities shift.

### Bounded Context

The logical boundaries, including the inputs, outputs, events, requirements, processes, and data models that are relevant to the subdomain. While ideally a bounded context and a subdomain will be in complete alignment, legacy systems, technical debt, and third-party integrations often create exceptions.

Bounded contexts should be highly cohesive. The internal operations of the context should be intensive and closely related, with the vast majority of communication occurring internally rather than cross-boundary.

**Connections between bounded contexts should be loosely coupled**, as changes made within one bounded context should minimize or eliminate the impact on neighbouring contexts.

It is common for business requirements of a product to change during its lifetime, but it is rare for a company to need to change the underlying implementation of any given product without accompanying business changes. Hence, bounded contexts should be built around business requirements and not technological requirements.

<img src="./assets/bounded-contexts.png">

Modelling around business requirements is preferred, but there are tradeoffs. Code may be replicated a number of times, and many services may use similar data access patterns. Product developers may try to reduce repetition by sharing data sources with other products or by coupling on boundaries. However, the subsequent tight coupling may be far more costly in the long run than repeating logic and storing similar data.
