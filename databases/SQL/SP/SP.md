## SP (Stored Procedures)

SPs have become part of the SQL standard since 1999.

## Cons

### Language Barrier and Lack of Ecosystem

Each database vendor has its own language for SP (Oracle has PL/SQL, SQL Server has T-SQL, etc). These langauges have not kept up with developments in general-purpose programming languages, and lack the ecosystem of libraries that you find with most programming languages.

### Difficult to Debug

Code running in a database is difficult to manage, harder to debug, more awkward to keep in version control and deploy, trickier to test, and difficult to integrate with a metrics collection system for monitoring.

### Performance-Sensitive

A database is much more performance-sensitive than an application server, as a database intance is often shared by many application servers. A badly written SP (using alot of memory or CPU) can cause much mroe trouble than a badly written application code.

## Resolutions

Modern implementations of SP have abandoned PL/SQL and use existing general-purpose programming languages instead i.e. VoltDB uses Java/Groovy, Dataomic uses Java/Clojure, Redis uses Lua.
