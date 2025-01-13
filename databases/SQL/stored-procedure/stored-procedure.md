## Stored Procedure (SP)

Stored procedure is a batch of statements (separated by semicolons) that is stored in relational database management system as a group that can be reused. Can access/modify data in a database, but not tied to a specific database. Allows passing of dynamic parameters.

## Drawbacks

### Language barrier and lack of ecosystem

Each database vendor has its own language for SP (Oracle has PL/SQL, SQL Server has T-SQL, etc). These languages have not kept up with developments in general-purpose programming languages, and lack the ecosystem of libraries that you find with most programming languages.

### Difficult to debug

Code running in a database is difficult to manage, harder to debug, more awkward to keep in version control and deploy, trickier to test, and difficult to integrate with a metrics collection system for monitoring.

### Performance-sensitive

A database is much more performance-sensitive than an application server, as a database instance is often shared by many application servers. A badly written SP (using a lot of memory or CPU) can cause much more trouble than a badly written application code.

## Resolutions

Modern implementations of SP have abandoned PL/SQL and use existing general-purpose programming languages instead i.e. VoltDB uses Java/Groovy, Datatomic uses Java/Clojure, Redis uses Lua.
