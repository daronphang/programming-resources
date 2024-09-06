## Service discovery (centralized service)

A **centralized service** such as Zookeeper can be configured as the service discovery to keep track of the state of every node in the system. It is the process that automatically detects, registers, and shares the locations of services in a network.

## Health checks

The centralized service here has the responsibility of listening to **heartbeats** or pulling health information about other nodes periodically and keeping the records of all the dead and alive nodes.

Although this provides a strong consistency guarantee, the primary drawbacks are that the service becomes a single point of failure, and it runs into scalability problems for a large distributed system.

## Dynamic URLs for communication between microservices

Typical ways to perform synchronous communication between microservices is to use HTTP or gRPC protocols. The issue that arises with microservice communication is ensuring that a microservice will know which API URL to call.

### Hardcoding URLs

One solution to this obstacle could be to hardcode the URLs into the microservice, however, this approach runs into problems:

- Changes require code updates
- Cloud is full of dynamic URLs
- Multiple environments mean multiple URLs

### Using service discovery

With service discovery, a central server, also known as a service registry, is responsible for registering all of the URL addresses and port locations of the services that exist in and interact with your app. Client servers can interact with this central server to locate the addresses of other services.

This central server is a layer of abstraction that is flexible enough to handle dynamic URLs and automatically respond to code changes.
