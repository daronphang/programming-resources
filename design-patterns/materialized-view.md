## Materialized View pattern

Generate prepopulated views over the data in one or more data stores when the data isn't ideally formatted for required query operations. This can help support efficient querying and data extraction, and improve application performance.

### Context and problem

When storing data, the priority for developers and data administrators is often **focused on how the data is stored, as opposed to how it's read**. The chosen storage format is usually closely related to the format of the data, requirements for managing data size and data integrity, and the kind of store in use. For example, when using NoSQL document store, the data is often represented as a series of aggregates, each containing all of the information for that entity.

However, this can have a **negative effect on queries**. When a query only needs a subset of the data from some entities, such as a summary of orders for several customers without all of the order details, it must **extract all of the data for the relevant entities** in order to obtain the required information.

### Solution

To support efficient querying, a common solution is to generate, in advance, a view that materializes the data in a format suited to the required results set. The Materialized View pattern describes generating prepopulated views of data in environments where:

- Source data isn't in a suitable format for querying
- Generating a suitable query is difficult
- Query performance is poor due to the nature of the data or the data store

These materialized views, which only contain data required by a query, allow applications to quickly obtain the information they need. In addition to joining tables or combining data entities, materialized views can include the current values of calculated columns or data items, the results of combining values or executing transformations on the data items, and values specified as part of the query. A materialized view can even be optimized for just a single query.

A key point is that a materialized view and the data it contains is completely disposable because it can be entirely rebuilt from the source data stores. **A materialized view is never updated directly by an application, and so it's a specialized cache**.

When the source data for the view changes, the view must be updated to include the new information. You can schedule this to happen automatically, or when the system detects a change to the original data. In some cases it might be necessary to regenerate the view manually.
