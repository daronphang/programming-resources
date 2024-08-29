## Communication between microservices

Typical ways to perform synchronous communication between microservices is to use HTTP or gRPC protocols. The issue that arises with microservice communication is ensuring that a microservice will know which API URL to call.

## Hardcoding URLs

One solution to this obstacle could be to hard code the URLs into the microservice, however, this approach runs into problems:

- Changes require code updates
- Cloud is full of dynamic URLs
- Multiple environments mean multiple URLs

## Service discovery

Service discovery is a vital component that enables communication between microservices. It is the process that automatically detects, registers, and shares the locations of services in a network.

With service discovery, a central server, also known as a service registry, is responsible for registering all of the URL addresses and port locations of the services that exist in and interact with your app. Client servers can interact with this central server to locate the addresses of other services.

This central server is a layer of abstraction that is flexible enough to handle dynamic URLs and automatically respond to code changes.

### Health checks

In addition to helping services locate one another, this communication solution provides a way to perform vital health checks that verify your services and systems are up and running. Also, if a service becomes obsolete and goes offline, it can be deregistered via service discovery.
