## CREATE

### DESCRIBE

To display information about the table.

```sql
DESCRIBE tablename;
```

### UUID

```sql
-- sql server

CREATE TABLE table_name (
  uuid uniqueidentifier NOT NULL DEFAULT newid()
)

```

```sql
-- mysql
CREATE TABLE table_name (
  uuid BINARY(16) PRIMARY KEY NOT NULL
)

INSERT INTO table_name (uuid) VALUES (UUID_TO_BIN(UUID()))

SELECT BIN_TO_UUID(uuid)
```

### INCREMENTING

```sql
--sql server
CREATE TABLE table_name (
  id_num IDENTITY(1,1) PRIMARY KEY NOT NULL
)
```

```sql
-- mysql
CREATE TABLE table_name (
  id_num SERIAL PRIMARY KEY NOT NULL
)
```

### TIMESTAMP

```sql
-- sql server
CREATE TABLE table_name (
  created_datetime DATETIME DEFAULT GETDATE(),
  created_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- cannot create default for TIMESTAMP, avoid this
)

```

```sql
-- mysql
CREATE TABLE table_name (
  created_datetime TIMESTAMP NOT NULL DEFAULT NOW()
)
```

## Examples

```sql
-- mysql
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

```sql
CREATE TABLE table_name (
  col_name1 TYPE col_constraint,
  col_name2 TYPE col_constraint,
  table_constraint table_constraint
)

CREATE TABLE account(
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(50) NOT NULL,
  created_on TIMESTAMP NOT NULL,
  last_login TIMESTAMP
)
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
