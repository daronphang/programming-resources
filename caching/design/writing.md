## Write-through cache

Data is written into the cache and the corresponding database simultaneously. There is **complete data consistency between cache and storage**, but results in higher latency for write operations as every write operation must be done twice.

## Write-around cache

Write directly goes to the database or permanent storage, bypassing the cache. It may **reduce latency but increases cache misses**.

## Write-back cache

Write is only done to the caching layer and the write is confirmed as soon as the write to the cache completes. The cache then asynchronously syncs this write to the database.

There is a risk of data loss in case the caching layer crashes. We can improve this by having more than one replica acknowledging the write in the cache.
