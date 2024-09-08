## Cache read strategies

### Read through cache

A read-through cache strategy is a caching mechanism where the **cache itself is responsible for retrieving the data** from the underlying data store when a cache miss occurs. In this strategy, the application requests data from the cache instead of the data store directly. If the requested data is not found in the cache (cache miss), the cache retrieves the data from the data store, updates the cache with the retrieved data, and returns the data to the application.

This approach helps to maintain consistency between the cache and the data store, as the cache is always responsible for retrieving and updating the data. It also simplifies the application code since the application doesn't need to handle cache misses and data retrieval logic.

### Read aside cache (lazy loading)

A read-aside cache strategy is a caching mechanism where the **application is responsible for retrieving the data** from the underlying data store when a cache miss occurs. In this strategy, the application first checks the cache for the requested data. If the data is found in the cache (cache hit), the application uses the cached data. However, if the data is not present in the cache (cache miss), the application retrieves the data from the data store, updates the cache with the retrieved data, and then uses the data.

The read-aside cache strategy provides **better control** over the caching process, as the application can decide when and how to update the cache. However, it also adds complexity to the application code, as the application must handle cache misses and data retrieval logic.

This approach can be beneficial in scenarios where cache misses are relatively infrequent, and the application wants to optimize cache usage based on specific data access patterns.
