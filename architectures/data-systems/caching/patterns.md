## Look-aside pattern

### Read

- Application requests data from cache
- Cache delivers data if available
- If data is not available (cache miss), application gets data from database and writes it to the cache for future requests (read aside)

### Write

After a particular key is updated in the database, the system doesn’t directly update the corresponding value in the cache. Instead, it removes the data for that key from the cache entirely. This process is known as cache invalidation.

## Inline pattern

### Read

- Application requests data from cache
- Cache delivers data if available
- If data is not available (cache miss), cache retrieves data from database, caches it, and returns the value to the requesting application
