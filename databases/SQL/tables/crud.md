### INSERT

SERIAL columns do not need to be provided a value. Inserted row values must match up for the table including constraints.

```sql
INSERT INTO account(username, passwword, create_on)
VALUES('Jose', '1234', CURRENT_TIMESTAMP),
      ('John', '1234', CURRENT_TIMESTAMP)

INSERT INTO table(col1,col2) SELECT col1,col2 FROM table2
```

### UPDATE

```sql
# Use UPDATE and SET
UPDATE account SET last_login = CURRENT_TIMESTAMP WHERE username = 'Jose'
UPDATE account SET col1 = CURRENT_TIMESTAMP, col2 = "hello" WHERE username = 'Jose'
```

### RETURNING

```sql
UPDATE account SET last_login = CURRENT_TIMESTAMP RETURNING username, last_login
```

### DELETE

To delete multiple items, use IN.

```sql
-- Delete all rows
TRUNCATE TABLE myassistant.dbo.celery_taskmeta

DELETE FROM table WHERE row_id = 1

DELETE FROM table WHERE id IN (value1, value2)

--sub query must return only one column
DELETE FROM your_table
WHERE id IN (select aColumn from ...);

DELETE FROM your_table
WHERE id >= a_value AND id <= another_value

DELETE FROM table
WHERE id BETWEEN 125 AND 150
```
