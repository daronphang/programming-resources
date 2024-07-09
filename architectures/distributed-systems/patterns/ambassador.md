## Ambassador pattern

An ambassador container brokers interactions between the application container and the rest of the world i.e. service mesh.

### Sharding

Sometimes the data that you want to store in a storage layer becomes too big for a single machine to handle. In such situations, you can employ sharding.

When adapting an existing application to a sharded backend, you can introduce an ambassador container that contains all of the logic needed to route requests to the appropriate storage shard. Thus, your frontend or middleware application only connects to what appears to be a single storage backend running on localhost. However, this server is in fact actually a sharding ambassador proxy, which receives all of the requests from your application code, sends a request to the appropriate storage shard, and then returns the result to your application.
