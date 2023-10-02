## Persisting Data

When working with relational databases, you have two options: JDBC and Spring Data, and Spring supports both abstractions.

### Repository

Configuring and establishing a database connection in the Java ecosystem is a cumbersome affair, with lots of repetitive ceremony. To resolve this, Spring Data introduces the concept of repositories.

A repository is an interface as a useful abstraction above various databases. The repository itself is a mere placeholder for the following types:

- The object stored in the database
- The object's unique ID/primary key field
