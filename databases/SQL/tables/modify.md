### ADD

```sql
ALTER TABLE table_name ADD column_name type constraint
ALTER TABLE table_name ADD COLUMN new_col TINYINT NOT NULL AFTER col_2
```

### CONSTRAINTS

```sql

```

### MODIFY

```sql
ALTER TABLE table_name ALTER COLUMN col_name VARCHAR(255) NOT NULL --mssql
ALTER TABLE table_name MODIFY COLUMN col_name VARCHAR(255) NOT NULL --mysql
```

### DROP

```sql
ALTER TABLE account DROP COLUMN job CASCADE -- CASCADE removes all dependencies
ALTER TABLE account DROP COLUMN IF EXISTS col1
```

### RENAME

```sql
ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name
```

### TRUNCATE

Deletes all the rows from the table without using any condition.
