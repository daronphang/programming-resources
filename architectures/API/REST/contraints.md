## Key Constraints

### Client-Server

Client and server should be separate from each other and allowed to evolve individually and independently.

### Stateless

REST APIs are stateless, meaning that calls can be made independently of one another, and each call contains all of the data necessary to complete itself successfully.

It should not rely on data being stored on the server or sessions to determine what to do with a call, but solely rely on the data that is provided in that call itself. Nonetheless, in order to reduce memory requirements and keep your application scalable, a RESTful API requires that any **state is stored on the client** and not on the server.

### Cache

As a stateless API can increase request overhead, a REST API should be designed to encourage the storage of cacheable data. Hence, the response should indicate that the data can be stored up to a certain time (expire at), or that it should not be cached by the client. Caching is done on the client side.

Many cache implementations use query string parameters from the resource identifier as the key to cached data.

### Uniform Interface

The key to the decoupling client from server is having a uniform interface that allows independent evolution of the application without having the application's services, models or actions tightly coupled to the API layer itself.

The uniform interface lets the client talk to the server in a single language, independent of the architectural backend of either. It should also provide a standardized means of communication i.e. for REST APIs built on HTTP, the uniform interface includes HTTP verbs GET, POST, PUT, PATCH and DELETE for CRUD operations.

### Layered System

A layered system is one comprised of layers, with each layer having a specific functionality and responsibility i.e. caches, gateways, proxy servers. It lets you encapsulate legacy systems and move less commonly accessed functionality to a shared intermediary, while also shielding more modern and commonly used components from them.

There are substantial security benefits of having a layered system as it allows you to stop attacks at the proxy layer, or within other layers, preventing them from getting to your actual server architecture.

### Code on Demand (Optional)

Code-on-demand allows for code or applets to be transmitted via the API for use within the application. In essence, it creates a smart application that is no longer solely dependent on its own code structure.
