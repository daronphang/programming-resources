### IF NOT EXISTS

Can be used to prevent inserting duplicates if duplicate key is not UNIQUE or PRIMARY constraint.

```sql
IF NOT EXISTS (
       SELECT 1 FROM dbo.testing
       WHERE username = 'JOHN'
)
INSERT INTO dbo.testing(username, fab) VALUES('testing123', 'f10w')
```

### OVER

Used in almost all invocations of window functions like AVG(), MAX(), and RANK(). Window functions operate on window frames which are sets of rows taht can be different for each record in the query result.

### PARTITION BY

Subclause of the OVER clause. Contrasting with GROUP BY, GROUP BY collapses individual records into a group and as a consequence, you cannot refer to any individual record field i.e. only the columns in the GROUP BY clause can be referenced.

If you want to get individual records of collapsed columns, need to use window functions.

```sql
-- GROUP BY
SELECT car_make,
       AVG(car_price) AS average_price,
       MAX(car_price) AS top_price
FROM   car_list_prices
GROUP BY car_make

-- PARTITION BY
SELECT
    car_make,
    car_model,
    car_price,
    AVG(car_price) OVER() AS "overall average price",
    AVG(car_price) OVER (PARTITION BY car_type) AS "car type average price"
FROM car_list_prices
```

### MERGE/ON DUPLICATE

Used to synchronize two tables by inserting, updating and deleting the target table based on condition with source table.

MySQL uses ON DUPLICATE key while SQL Server uses MERGE.

```sql
MERGE myassistant.dbo.automation_requests AS TARGET
USING (
SELECT
'12345ABE' AS req_id,
'instacap' AS req_type,
'DARONPHANG' AS req_user,
'submitted' AS req_status,
'oh yeah' AS req_message,
NULL AS req_completed
) AS SOURCE
ON TARGET.request_Id = SOURCE.req_id

WHEN MATCHED THEN UPDATE SET
TARGET.request_Id = SOURCE.req_id,
TARGET.request_type = SOURCE.req_type,
TARGET.username = SOURCE.req_user,
TARGET.status = SOURCE.req_status,
TARGET.message = SOURCE.req_message,
TARGET.completed_at = SOURCE.req_completed

WHEN NOT MATCHED BY TARGET THEN INSERT (
request_Id,
request_type,
username,
status,
message,
completed_at
)
VALUES (
SOURCE.req_id,
SOURCE.req_type,
SOURCE.req_user,
SOURCE.req_status,
SOURCE.req_message,
SOURCE.req_completed
);
```

### LEAD, LAG

LAG is used to access previous rows data as per defined offset value while LEAD is for subsequent rows. Useful function in comparing the current row value from the previous row value.

```sql
LAG (return_col, offset, default_value)
OVER ([partition_by_clause] order_by_clause)

LAG (col1, 1, 'this is default') OVER (ORDER BY col2 DESC) AS PREV_ROW_VALUE
```

### WITH (NOLOCK)

Used to override the default transaction isolation level of the table or the tables within the view in a specific query. Allows users to retrieve data without being affected by the locks, on the requested data, due to another process changing it i.e. another user updating the same table but transaction has not been committed. 

Considered as "dirty read" as data may or may not exist depending on the final outcome of an update transaction. There is a possibility of reading data that has been changed, but not yet committed to the database. This is not ideal if the data needs to be in a consistent state. 

```sql
UPDATE Person.Contact SET Suffix = 'B' WHERE ContactID < 20    

-- if updates are recorded but transaction has not completed, query will still return updated data
SELECT * FROM Person.Contact WITH (NOLOCK) WHERE ContactID < 20 
```
