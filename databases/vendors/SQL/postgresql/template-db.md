## Template databases

Postgres has a feature called **template databases**. When creating a database, it works by copying an existing database from template1. If you add objects to template1, these objects will subsequently be copied into newly created databases.

Copying action is a cheap filesystem operation, whereas performing migrations on a new database is expensive. Hence, an alterative is to perform migrations on template1, and subsequently create a new database. This may help during integration testing.

There is a second standard system database named template0. This database contains the same data as the initial contents of template1, that is, only the standard objects predefined by your version of PostgreSQL. **template0 should never be changed after the database cluster has been initialized**.

https://www.postgresql.org/docs/current/manage-ag-templatedbs.html
