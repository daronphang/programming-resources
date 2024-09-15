## Functions as a Service

There is a class of applications that might only need to temporarily come into existence to handle a single request, or simply need to respond to a specific event. This style of request or event-driven application design has flourished recently as large-scale public cloud providers have developed FaaS products.

### FaaS vs serverless computing

Oftentimes, FaaS is referred to as serverless computing. While this is true, it’s worth differentiating between **event-driven FaaS** and the broader notion of serverless computing.

Serverless computing can apply to a wide variety of computing services; for example, a multi-tenant container orchestrator (container-as-a-service) is serverless but not event-driven. Conversely, an open source FaaS running on a cluster of physical machines that you own and administer is event-driven but not serverless. Understanding this distinction enables you to determine when event-driven, serverless, or both is the right choice for your application.

### Benefits

- Dramatically simplifies the distance from code to running service
- Code deployed is managed and scaled automatically
- Functions are an even more granular building block for designing distributed systems
- Stateless

### Challenges

- Forces you to strongly decouple each piece of your service
- Each function is entirely independent
- Only communication is across the network, and each function instance cannot have local memory (persistent storage service is required)
- Cyclic functions are hard to detect

## When FaaS is not suited

### The need for background processing

FaaS is inherently an event-based application model. Functions are executed in response to discrete events that occur and trigger the execution of the functions. Additionally, because of the serverless nature of the implementation of theses services, the runtime of any particular function instance is generally time bounded. This means that **FaaS is usually a poor fit for situations that require processing** e.g. transcoding a video, compressing log files, etc.

### The need to hold data in memory

An architectural limitation of FaaS is the inability to load a significant amount of data in memory to process user requests.
