## Shared service

The primary alternative to using a shared library for common functionality is to use a shared service instead. Common functionality is made available at runtime through separate services.

One distinguishing factor about the shared service technique is that the shared code must be in the form of **composition, not inheritance**.

This technique is good to use **highly polyglot environments** (those with multiple heterogeneous languages and platforms), and also when shared functionality tends to change often.

### Change risk

A change to a shared service is a runtime change, as opposed to a compile-based change with the shared library technique. As a result, a “simple” change in a shared service can effectively bring down an entire system.

An approach would be to use **API endpoint versioning**. However, this assumes that access to a shared service is through RESTful API call. With other protocols (gRPC, messaging), it further complicates the versioning strategy for a change.

### Performance

As services requiring the shared functionality must make an interservice call to a shared service, performance is impacted because of network and security latency. This trade-off does not exist with shared library technique.

Use of gRPC can help mitigate some of the performance issues by significantly reducing network latency, as can the use of asynchronous protocols like messaging. With messaging, the service needing the shared functionality can issue a request through a request queue, perform other work, and once needed, can retrieve the results through a separate reply queue using a correlation ID.

### Scalability

Another drawback of the shared service technique is that the shared service must scale as services using the shared service scale. This can sometimes be a mess to manage, particularly with multiple services concurrently accessing the same shared service. This trade-off does not exist with shared library technique.

### Fault tolerance

While fault-tolerance issues can usually be mitigated through multiple instances of a service, nevertheless it is a trade-off to consider when using the shared service technique.

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>
<tr>
<td>
• Good for high code volatility </br>
• No code duplication in heterogeneous codebases </br>
• Preserves the bounded context </br>
• No static code sharing
</td>
<td>
• Versioning changes can be difficult </br>
• Performance is impacted due to latency </br>
• Fault tolerance and availability issues due to service dependency </br>
• Scalability and throughput issues due to service dependency </br>
• Increased risk due to runtime changes
</td>
</tr>
</table>
