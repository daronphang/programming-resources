## Cache metrics

Caches are measured along two primary axes:

- **Efficiency**: Measures how well the cache can store and serve the required data
- **Throughput performance**: How fast the cache can serve data and help scale the application

## Cache efficiency

A lower miss ratio indicates higher cache efficiency, as more requests are served directly from the cache, reducing backend load, access latency, and bandwidth costs.

### Cache miss ratio

The fraction of requests that are cache misses.

```
cache miss / (cache hits + cache miss)
```

### Byte miss ratio

The fraction of bytes that are cache misses.

### Cache evictions

Monitor the number of evictions occurring in the cache. Frequent evictions might suggest the cache is too small or the eviction policy is not optimal for your use case.
