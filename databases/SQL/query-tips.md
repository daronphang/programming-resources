## Get Average Count

```sql
SELECT AVG(rowsPerDay)
FROM
(
 SELECT COUNT(*) AS rowsPerDay
 FROM dbo.automation_requests
 GROUP BY CONVERT(DATE, created_at)
) AS dummy
```

## Retrieve IP Address and Port

```sql
SELECT DISTINCT local_net_address, local_tcp_port
FROM sys.dm_exec_connections
WHERE local_net_address IS NOT NULL
```

## Concatenate Rows

### SQL Server

```sql
SELECT
STRINGAGG(column, ',') AS ATTRIBUTES
FROM
CORR_TABLE

-- with grouping
SELECT
GROUP_NAME,
STRINGAGG(column, ',') AS ATTRIBUTES
FROM
CORR_TABLE
GROUP BY GROUP_NAME
```

### Snowflake

```sql
SELECT
LISTAGG(column, ',') WITHIN GROUP (ORDER BY column ASC) AS ATTRIBUTES
FROM
CORR_TABLE
```
