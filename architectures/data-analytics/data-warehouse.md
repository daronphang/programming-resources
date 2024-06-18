## Data warehouse pattern

Architects made an attempt to provide queriable analytical data with the **Data Warehouse pattern**. The basic problem they tried to address goes to the core of the separation of operational and analytical data: the formats and schemas of one don’t necessarily fit (or even allow the use of) the other. For example, many analytical problems require aggregations and calculations, which are expensive operations on relational databases, especially those already operating under heavy transactional load.

## Characteristics

### Data extracted from many sources

As the operational data resided in individual databases, it isn't practical to query across all various databases to build reports. Hence, the data is extracted into the warehouse solely for analytical purpose.

### Transformed to single schema

Often, operational schemas don’t match the ones needed for reporting. Thus, most data warehouses utilized a Star Schema to implement dimensional modelling, transforming data from operational systems in differing formats into the warehouse schema. To facilitate speed and simplicity, warehouse designers de-normalize the data to facilitate performance and simpler queries.

### Loaded into warehouse

As the operational data resides in individual systems, the warehouse must build mechanisms to regularly extract the data, transform it, and place it in the warehouse. Designers either used built-in relational database mechanisms like replication or specialized tools to build translators from the original schema to the warehouse schema.

## Drawbacks

### Integration brittleness

The requirement built into this pattern to transform the data during the injection phase creates crippling brittleness in systems. **A database schema for a particular problem domain is highly coupled to the semantics of that problem**; changes to the domain require schema changes, which in turn require data import logic changes.

### Extreme partitioning of domain knowledge

Building complex business workflows requires domain knowledge. Building complex reports and business intelligence also requires domain knowledge, coupled with specialized analytics techniques. Architects, developers, DBAs, and data scientists must all coordinate on data changes and evolution, forcing tight coupling between vastly different parts of the ecosystem.

### Complexity

Building an alternate schema to allow advanced analytics adds complexity to the system, along with the ongoing mechanisms required to ingest and transform data. A data warehouse is a separate project outside the normal operational systems for an organization, so must be maintained as a wholly separate ecosystem, yet highly coupled to the domains embedded inside the operational systems. All these factors contribute to complexity.

### Limited functionality for intended purpose

Ultimately, most data warehouses failed because they didn’t deliver business value commensurate to the effort required to create and maintain the warehouse.

## Star schema

The Star Schema pattern was popular with data marts and warehouses. It separates the data semantics into facts, which hold the organization’s quantifiable data, and dimensions; hence they are also known as dimensional models, which include descriptive attributes of the fact data.

Most significantly, the Star Schema is purposely de-normalized to facilitate simpler queries, simplified business logic (fewer complex joins), faster queries and aggregations, complex analytics such as data cubes, and the ability to form multi-dimensional queries. Most Star Schemas become incredibly complex.
