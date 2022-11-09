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
