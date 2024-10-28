## Load balancer vs API gateway

Load Balancer and API Gateway are two crucial components in modern web architectures, often used to manage incoming traffic and requests to web applications. While they have some overlapping functionalities, their primary purposes and use cases are distinct.

## Load balancer

Load Balancer is primarily used to distribute network or application traffic across multiple servers. This distribution helps to optimize resource use, maximize throughput, reduce response time, and ensure reliability.

There are different types of load balancers, that can operate at different layers of the OSI model (layer 4, layer 7).

## API gateway

An API Gateway is an API management tool that sits between a client and a collection of backend services. It acts as a reverse proxy to route requests, simplify the API, and aggregate the results from various services.

The API Gateway can handle a variety of tasks, including request routing, API composition, rate limiting, authentication, and authorization.

## Hybrid

You can use both a load balancer and an API gateway together as they often complement each other in managing traffic and providing efficient service delivery.

### Load balancer before API gateway

The Load Balancer is placed in front of the API Gateway. This is the typical configuration in many architectures.

The Load Balancer distributes incoming traffic across multiple instances of the API Gateway, ensuring that no single gateway instance becomes a bottleneck.

### Load balancer after API gateway

The API Gateway first processes and routes the request to an internal Load Balancer, which then distributes the request to the appropriate service instances. Useful when different services behind the API Gateway require their own load balancing logic.
