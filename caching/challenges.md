## Challenges

### Stale set

This happens when the cache is set with outdated data and there’s no easy way of invalidating it.

### Thundering herd

This problem occurs in a highly concurrent environment when a cache miss triggers a thundering herd of requests to the database.

## Solutions

### Leasing

Leasing can help to solve both stale sets and thundering herds. With leasing, cache provides a lease (token bound to a specific key) to a particular client to set data into the cache whenever there is a cache miss.

The client has to provide this token when setting the value in the cache and memcache can verify whether the data should be stored by verifying the token. If the item was already invalidated by the time the client tried to update, Memcache will invalidate the lease token and reject the request.

The cache can also regulate the rate of issuing the lease tokens. For example, it may return a token once every 5 seconds per key.

For any requests for the key within 5 seconds of the lease token being issued, Memcache sends a special response requesting the client to wait and retry so that these requests don’t hit the database needlessly. This is because there’s a high probability that the client holding the lease token will soon update the cache and the waiting clients will get a cache hit when they retry.

<img src="../assets/leasing.png">
