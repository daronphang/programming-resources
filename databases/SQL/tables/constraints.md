### PRIMARY KEY

Primary key is a column or gorup of columns used to identify a row uniquely in a table. A table can have multiple primary keys, and each table SHOULD have a primary key to uniquely identify a row for CRUD.

```sql
col_1 uniqueidentifier NOT NULL DEFAULT newid()   --mssql, mysql doesn't allow
```

### UNIQUE KEY

Used to prevent duplicate values in a column. A table can have only one PRIMARY KEY but it can have multiple UNIQUE KEYS.

### FOREIGN KEY

Foreign key is a field or group of fields in a table that uniquely identifies a row in another table; references to the primary key of the other table i.e. FK in child table, PK in parent table. A table can have multiple FK depending on its relationship with other tables.

### CONSTRAINTS

Rules enforced on data columns in a table. Used to prevent invalid data from being entered into the database and hence, ensuring accuracy and reliability.
Commonly used in PK and FK. Constraints can be for column or table.

To view constraints in table, execute the following in query.

```
NOT NULL
UNIQUE          Combination of unique columns UNIQUE(col1, col2, col3)
CHECK           Value must satisfy Boolean
REFERENCES      Used for indicating foreign key
PRIMARY KEY     Multiple columns can be PK. Same as UNIQUE NOT NULL
```

```sql
SELECT
TABLE_NAME,
CONSTRAINT_NAME,
CONSTRAINT_TYPE
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS;
```
