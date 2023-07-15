## REST (Representational State Transfer)

REST is an architectural style for building distributed systems based on hypermedia. REST APIs are designed around resources.

While REST can be use over nearly any protocol, it is most commonly implemented using HTTP as the application protocol as HTTP uses open standards and does not bind the implementation of the API or the client applications to any specific implementation i.e. REST web service can be written in ASP.NET, Python, Javascript. HTTP protocol has similar concepts with REST.

RESTful systems support messaging in different formats including plain text, HTML, YAML, XML, and JSON, while SOAP only allows XML.

### Resources

Concept of resources is core to the REST architectural style. A resource is any kind of object, data or service that can be accessed by the client i.e. an item of interest. It is an object with a type, associated data, relationships to other resources, and a set of methods that operate on it.

A resource has an identifier (URI) that uniquely identifies that resource i.e. URLs for HTTP.

A resource is usually something that can be stored on a computer and represented as a stream of bits i.e. a document, text file, images, videos, row in database, or the result of running an algorithm.

Clients interact with a service by **exchanging representations of resources**. Many web APIs use JSON as the exchange format.

### Methods

REST APIs often involve the use of CRUD functions (create, read, update, delete) that are used for interacting with database applications of persistent storage, but are not limited to them.

## Benefits

### Decoupled client and server

REST allows for better abstraction than RPC. A system with abstraction levels is able to encapsulate its details to better identify and sustain its properties. This makes REST API flexible enough to evolve over time while remaining a stable system.

### Discoverability

Communication between client and server describes everything so that no external documentation is required to understand how to interact with a REST API.

### Cache-friendly

Reusuing a lot of HTTP tools, REST is the only style that allows caching data on the HTTP level.

### Multiple formats support

The ability to support multiple formats for storing and exchanging data is one of the reasons REST is currently a prevailing choice for building public APIs.

## Drawbacks

### No single REST structure

There is no exact right way to build a REST API and hence, making it difficult in practice.

### Big payloads (over and under-fetching)

REST returns a lot of rich metadata so that the client can understand everything necessary about the state of the application just from its responses. It can also contain not enough of the necessary data and hence, often create the need for another request.
