## Naming

Use singular when naming tables as each table represents a "type" or "entity", not a collection. However, using plural is the default for most ORMs.

### Reserved keywords

```
`column` `table` `status` `select` `key` `order` `desc` `group` `rank` `limit` `like` `int` `value` `type` `user` `date` `time` `float` `text` `primary` `default` `exists` `null` `index` `unique` `references` `foreign` `constraint` `check` `case` `when` `then` `else` `end` `interval` `if` `now` `schema` `database` `cursor` `procedure` `lock` `view` `column` `desc` `asc` `having` `union` `intersect` `except` `cast` `coalesce` `collate` `current_user` `current_date` `current_time` `current_timestamp` `isnull` `notnull` `replace` `rownum` `sysdate` `tablespace` `temporary` `trigger` `truncate` `with` `row` `rows` `percent` `rank` `dense_rank` `lag` `lead` `ntile` `first_value` `last_value` `nth_value` `over` `partition` `range` `row_number`
```

## Optimizing queries

- SELECT fields individually instead of using `SELECT *`
- Avoid using SELECT DISTINCT by adding more SELECT fields as GROUPing is expensive and may be inaccurate
- When joining tables, exclude unnecessary columns and perform query first before joining
- use WHERE instead of HAVING to define filters

```sql
SELECT * FROM table1 AS TB1
INNER JOIN table2 AS TB2 ON TB1.col2 = TB2.col2
WHERE TB1 = 'hello'
AND TB2 = 'world'

-- optimized
SELECT * FROM table1 AS TB1
INNER JOIN (
SELECT col1 FROM table2 WHERE col1 = 'world'
) AS TB2 ON TB1.col2 = TB2.col2
WHERE TB1.col1 = 'hello'
```

## Indexing

Indexes are special lookup tables that the database search engine can use to speed up data retrieval i.e. pointer to data in a table. Helps to speed up SELECT queries and WHERE clauses, but slows down data input with UPDATE and INSERT statements. Can be created/dropped without any effect on data.

Whether to create single/composite index depends on the columns used frequently in WHERE clause. Implicit indexes are indexes automatically created by database server when an object is created i.e. for PK/unique constraints.

```sql
-- single-column index
CREATE INDEX index_name ON table_name (column1)

-- unique indexes; can be used for both performance and data integrity (no duplicates)
CREATE UNIQUE INDEX index_name ON table_name (column_name)

-- composite indexes
CREATE INDEX index_name ON table_name (col1, col2)
```

### Unique indexes vs constraint

- When a unique constraint is created, a unique index is also created
- No functional difference between both of them
- Boils down to preferred style/consistency where constraint is more for business rule and index for querying
- Unique index can be disabled while constraint cannot be disabled

### When to Avoid indexes

- Indexes should not be used on small tables
- For tables that have frequent, large database UPDATES or INSERT operations
- Indexes should not be used on columns that have high number of NULL values
- Columns that are frequently manipulated should not be indexed

## Removing duplicates

### Row number

```sql
WITH CTE (Col1, Col2, Col3, DuplicateCount)
AS
(
  SELECT Col1, Col2, Col3,
  ROW_NUMBER() OVER(PARTITION BY Col1, Col2,
       Col3 ORDER BY Col1) AS DuplicateCount
  FROM MyTable
) SELECT * from CTE Where DuplicateCount = 1
```

### GROUP BY

```sql
SELECT FirstName, LastName, MobileNo
FROM  CUSTOMER
GROUP BY FirstName, LastName, MobileNo;
```

### Self-join

```
emp_name   emp_address  sex  matial_status
uuuu       eee          m    s
iiii       iii          f    s
uuuu       eee          m    s
```

```sql
-- use self join
SELECT emp_name, emp_address, sex, marital_status
FROM YourTable a
WHERE NOT EXISTS (
  SELECT 1
  FROM YourTable b
  WHERE
  b.emp_name = a.emp_name AND
  b.emp_address = a.emp_address AND
  b.sex = a.sex AND
  b.create_date >= a.create_date
)
```

### LAG

```sql
SELECT
    *,
    LAG(unique_row,1) OVER (ORDER BY event_note_datetime ASC) AS next_unique_row
INTO #ETOSTATES2
FROM
    #ETOSTATES

SELECT
    equip_id,
    equip_state,
    equip_semi_state,
    event_code,
    comments,
    event_note_datetime
FROM
    #ETOSTATES2
WHERE
    unique_row != next_unique_row
```

## Avoid storing delimited lists

Violates First Normal Form. Exception would be employing de-normalization. If tables are normalized, to avoid storing entries in column as delimited lists for following reasons:

- Can't ensure each value is right data type i.e. 1,2,3,banana,5
- Can't use FK to link values to lookup table and unable to enforce referential integrity
- Can't enforce uniqueness and consistency i.e. 1,3,3,5
- Can't delete a value from list without fetching the whole list
- Can't store a list longer than the specified length of string column
- Difficult to search for all entities with a given value in list with inefficient table-scan
- Difficult to count elements in list or perform aggregate functions
- Difficult to fetch list in sorted order

https://stackoverflow.com/questions/3653462/is-storing-a-delimited-list-in-a-database-column-really-that-bad

## Querying from different DB servers

For SQL Server, can use link server. Alternative is to create and insert into a temporary table and inner join to that temporary table.
