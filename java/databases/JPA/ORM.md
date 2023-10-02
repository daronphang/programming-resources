## ORM

A framework like Hibernate or EclipseLink codifies object-relational mapping into a library or framework, an ORM layer. From a programming perspective, the layer is considered as an adapter layer; it adapts the language of object graphs to the language of SQL.

As part of the application architecture, ORM layer is responsible for **managing the conversion of software objects to interact with the tables and columns in a relational database** i.e. converts Java classes and objects so that they can be stored and managed in a relational database.

By default, the name of the object being persisted becomes the name of the table, and columns become fields.

### Configuring ORM Layer

When you setup a new project to use JPA, you will need to configure the datastore and JPA provider:

- Datastore connector to connect to your database
- JPA provider such as Hibernate or EclipseLink
