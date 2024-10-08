## Admission policies

Cache admission policies determine which items should be stored in the cache when new data arrives and space is needed. These policies help optimize cache performance by deciding which data will provide the most benefit when cached.

## Always cache

All incoming data is cached regardless of current cache status. Simple but can lead to cache overflow and inefficiency.

## Cache on demand

Only cache data that is requested. This approach focuses on caching items that users are actively seeking, potentially improving relevance.

## Threshold-based caching

Caching decisions are made based on certain criteria or thresholds, such as size, frequency of access, or the age of the data. If the data exceeds the threshold, it may not be cached.

## Frequency-based admission

Caches items based on how often they are accessed. High-frequency items are prioritized for caching, as they are likely to be requested again.

## Recency-based admission

Caches items based on how recently they were accessed. Items that have been accessed recently are more likely to be accessed again.

## User-specific caching

Caches items based on individual user behavior, preferences, or profiles, personalizing the cache to improve relevance for specific users.

## Predictive caching

Uses machine learning or heuristics to predict which items are likely to be accessed in the near future and caches them proactively.
