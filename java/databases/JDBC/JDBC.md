## JDBC

The JDBC API allows programmers to connect to a database to query/update using SQL. Programs written according to the API talk to the driver manager, which in turn, uses a driver to talk to the actual database. JDBC is a layer of abstraction that lets an application issue SQL commands without thinking about the underlying database implementation.

### Driver Types

#### Type 1

Translates JDBC to ODBC and relies on an ODBC driver to communicate with the database. Java 8 no longer provides the JDBC/ODBC bridge as it was never intended for production use.

#### Type 2

Written partly in Java and native code. It communicates with the client API of a database. You must install some platform-specific code onto the client in addition to a Java library.

#### Type 3

Pure Java client library that uses a database-independent protocol to communicate database requests to a server component, which then translates the requests into a database-specific protocol.

#### Type 4

Pure Java library that translates JDBC requests directly to a database-specific protocol.

### Three-Tier Client/Server Model

The traditional client/server model has a rich GUI on the client and a database on the server. In this model, a JDBC driver is deployed on the client.

However, nowadays, it is more common to have a three-tier model where the client application does not make database calls. Instead, it calls on a middleware layer on the server that in turn makes the database queries.

This model **separates visual presentation (on the client) from business logic (middle tier) and the raw data (in database)**. Therefore, it becomes possible to access the same data from multiple clients i.e. desktop, web browser, mobile app.

Communication between the client and middle tier typically occurs through HTTP. JDBC manages the communication between the middle tier and the backend database.

```
Client -> Middle tier + JDBC -> Database Server
```
