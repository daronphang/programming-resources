## CREATE

To display information about the table.

```sql
DESCRIBE tablename;
```

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
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_NAME = 'lead_lot_tracking_shared_identifiers'
```

### DESCRIBE

Outputs the table columns' descriptions.

```sql
DESCRIBE table_name;
```

## MYSQL

```sql
USE portfolio;
CREATE TABLE contacts (
uuid BINARY(16) PRIMARY KEY NOT NULL,
contact_name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
company VARCHAR(255) NOT NULL,
message VARCHAR(255) NOT NULL,
created_datetime TIMESTAMP NOT NULL DEFAULT NOW()
)
```

### Examples

```sql
CREATE TABLE table_name (
  col_name1 TYPE col_constraint,
  col_name2 TYPE col_constraint,
  table_constraint table_constraint)

CREATE TABLE account(
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(50) NOT NULL,
  created_on TIMESTAMP NOT NULL,
  last_login TIMESTAMP)

CREATE TABLE account_job(
  user_id REFERENCES account(user_id),
  hire_date TIMESTAMP)

CREATE TABLE example(
  user_id SERIAL PRIMARY KEY,
  age SMALLINT CHECK(age > 21),
  parent_age SMALLINT CHECK(parent_age > age))

CREATE TABLE products(
  product_no INTEGER,
  name TEXT,
  price NUMERIC CHECK(price > 0),
  discounted_price NUMERIC,
  CHECK(discounted_price > 0 AND price > discounted_price))
```

```sql
USE stock_app;
CREATE TABLE user_portfolios (
id SERIAL,
userId CHAR(36) NOT NULL,
portfolioName VARCHAR(36) NOT NULL,
orderId TINYINT NOT NULL,
createdAt TIMESTAMP NOT NULL DEFAULT NOW(),   -- mssql uses DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
updatedAt TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
PRIMARY KEY (id, portfolioName),
CONSTRAINT constraint_1 UNIQUE(userId, portfolioName),
CONSTRAINT constraint_2 UNIQUE(userId, orderId),
FOREIGN KEY (userId) REFERENCES stock_app.users (_id)
)
```

### Adding Entries Violating Keys

Need to drop and add back the key.

```sql
--check index name for key
SHOW INDEX FROM user_portfolios;

ALTER TABLE user_portfolios DROP INDEX userId_2;
UPDATE user_portfolios
SET orderId =  CASE WHEN portfolioName='Semiconductor' THEN 2 WHEN portfolioName='Automobile' THEN 1 ELSE orderId END
WHERE userId = '7bd32724-550e-4921-93ab-e62798e24f6a';
ALTER TABLE user_portfolios ADD UNIQUE KEY `userId_2` (`userId`,`orderId`);
```

## Creating Tables Using SELECT

```sql
-- For single row, multiple columns
 SELECT
'12345ABE' AS req_id,
'instacap' AS req_type,
NULL AS req_completed
```

```sql
-- For multiple rows and columns
SELECT * FROM (
VALUES
('12345ABE', 'instacap', NULL),
('12345ABE', 'instacap', NULL)
) AS
PLACEHOLDER
(req_id, req_type, req_completed)
```

```sql
-- alternative using UNION
 SELECT
'12345ABE' AS req_id,
'instacap' AS req_type,
NULL AS req_completed
UNION ALL
(SELECT '12345ABE', 'instacap', NULL)
UNION ALL
(SELECT '12345ABE', 'instacap', NULL)
```
