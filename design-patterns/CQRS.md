## Command Query Responsibility Segregation (CQRS)

CQRS is the notion that you can use a different model to update information than the model you use to read information. CQRS uses command handlers to simplify the query process and hide complex, multisystem changes.

However, for most systems, CQRS adds **risky complexity**.

### Limitations of CRUD

The mainstream approach people use for interacting with an information system is to treat it as a CRUD datastore. Our interactions are all about storing and retrieving these records.

While reading and writing to the same database is acceptable for small applications, distributed applications operating at web-scale require a segmented approach. As our needs become more sophisticated we steadily move away from that model.

### Command and Query models

The change that CQRS introduces is to split that conceptual model into separate models for update and display, which it refers to as Command and Query respectively.

The rationale is that for many problems, particularly in more complicated domains, having the same conceptual model for commands and queries leads to a more complex model that does neither well. Nevertheless, there is usually enough overlap between the command and query sides that **sharing a model is easier**.

The two models might not be separate object models, it could be that the same objects have different interfaces for their command side and their query side, rather like views in relational databases. However, in most cases, they are clearly separate models.

### Benefits

- Complex domains can be tackled with CQRS
- Separating write activities from read activities allows you to use the best database technology for the task at hand i.e. SQL db for writing and non-SQL db for reading
- Read activity tends to be more frequent than write, hence you can reduce response latency by placing read data sources in strategic geolocations for better performance
- Separating write from read activity leads to more efficient scaling of storage capacity based on real-world usage (independent scaling)

### Drawbacks

- Supporting the CQRS pattern requires expertise in a variety of database technologies
- Having separate models raises questions about how hard to keep those models consistent, which raises the likelihood of using eventual consistency
- Using CQRS on a domain that doesn't match it will add complexity, thus reducing productivity and increasing risk

### Use cases

CQRS fits well with event-based programming models.
