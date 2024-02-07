## Aggregator design pattern

The aggregator design pattern describes a service that gets a request, then makes several requests to different services, combines the results, and then responds to the initial request.

This implementation helps to reduce chattiness and communication overhead between client and microservices. Aggregation services should not perform any processing or transformation.

### Parallel aggregation (Scatter gather pattern)

In parallel aggregation, requests are sent to necessary services in parallel. The responses are then aggregated and sent back to the consumer.

### Chain of responsibility pattern

Chain pattern is used when a service has a dependency on another service.

1. Consumer first sends the request to Service A
2. Service A sends request to Service B
3. Service B sends request to Service C

### Branch pattern

This pattern extends both Aggregator and Chain of responsibility pattern. A service can simultaneously call two or more different chains of microservices and generate an aggregated response processing from them.

1. Service A calls Service B and Service C in parallel
2. Service C calls Service D in a chain
