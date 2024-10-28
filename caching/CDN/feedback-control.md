## Feedback-control loop

The sheer size of a CDN requires that hosted documents are automatically distributed and replicated. In most cases, a large-scale CDN is organized similar to a feedback-control loop.

<img src="../assets/feedback-control.png">

## Metrics aggregation

Aggregating metrics can be used to estimate how well a CDN is performing. However, measuring is a complex task, and in practice, what really counts for commercial CDNs is whether they can **meet the SLAs** that have been made with customers.

### Latency

Latency refers to the time taken for an action to take place. However, this becomes difficult when a process needs to decide on the placement of replicas, as it also needs to know the delay between a client and the remote server. For such, an algorithm for globally positioning nodes will need to be deployed.

### Bandwidth

Instead of estimating latency, it may be more important to measure the available bandwidth between two nodes. This information is particularly important when large documents have to be transferred. In this case, the responsiveness of the system is largely dictated by the time that a document can be transferred. However, accurate measurements can be difficult to attain.

### Spatial

Spatial metrics consist of measuring the distance between nodes in terms of the number of network-level routing hops, or hops between autonomous systems. However, determining the number of hops can be difficult, and may not even correlate with latency.

Moreover, looking at routing tables is not going to work when low-level techniques such as Multi-Protocol Label Switching (MPLS) are deployed. MPLS circumvents network-level routing to immediately and efficiently forward packets to their destination i.e. packets may follow an entirely different route than advertised in the tables.

### Network usage

Network usage metrics often entails consumed bandwidth i.e. number of bytes transferred. However, to do this correctly, we need to consider how often the document is read, how often it is updated, and how often it is replicated.

### Consistency

Consistency metrics tells us to what extent a replica is deviating from its master copy.

### Financial

Financial metrics form another class for measuring how well a CDN is doing. As most CDNs operate on a commercial basis, it is clear that often financial metrics will be decisive. Moreover, the financial metrics are closely related to the actual infrastructure of the Internet.

## Adaptation triggering

To determine when and how adaptations are to be triggered, a simple model is to periodically estimate metrics and subsequently take measures as needed. This approach is often seen in practice.

## Managing replication

An interesting aspect of CDNs is that they need to make a trade-off between many aspects when it comes to hosting replicated content:

- Access times for a document may be optimal if it is massively replicated
- Incurs financial cost
- Incurs bandwidth usage for disseminating updates

When considering improving performance of Web applications through caching and replication, matters are complicated by the fact that several solutions can be deployed, with no single one standing out as the best.

<img src="../assets/replication-alternatives.png">

### Full replication

To improve performance, we can decide to apply full replication of the data stored at the origin server. This scheme works well whenever the update ratio is low and when queries require an extensive database search.

Another case for full replication is when queries are generally complex i.e. relational database with multiple table joins.

### Content-aware caches

An alternative to partial replication is to make use of content-aware caches. The basic idea is that an edge server maintains a local database that is now tailored to the type of queries that can be handled at the origin server i.e. organized according to the structure of queries and **not normalized**.

However, data at the edge server needs to be kept consistent, and the origin server needs to know which records are associated with which templates, so that any update of a record, or any update of a table, can be properly addressed.

### Content-blind caching

The idea of content-blind caching is simple: when a client submits a query to an edge server, the server first computes a **unique hash value for that query**. Using this hash value, it subsequently looks in its cache whether it has processed this query before. If not, the query is forwarded to the origin and the result is cached before returning it to the client.

The main advantage of this scheme is the reduced computational effort that is required from an edge server in comparison to database queries.

However, content-blind caching can be wasteful in terms of storage, as the caches may contain much more redundant data in comparison to content-aware caching or database replication. Such redundancy also complicates the process of keeping the cache up-to-date, as the origin server may need to keep an accurate account of which updates can potentially affect cached query results.
