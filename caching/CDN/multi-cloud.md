## Multi-cloud CDN

A CDN is a distributed network of servers that are designed to deliver content to users quickly and efficiently. The main purpose of a CDN is to reduce latency and improve the performance of websites and applications by caching and serving content from a location that is closer to the end user.

There are two ways you can distribute the load:

- Vertical stacking
- Horizontal stacking

Vertical stacking is not built to ensure availability but rather to dissipate the load on the origin server. It is also critical to ensure the uptime of all the vendors in play as the whole chain will collapse if one goes down.

Horizontal scaling is purported to ensure availability by distributing the load across many vendors.

## Routing

- Static DNS: Involves setting up fixed DNS entries for each CDN; straightforward but lacks automatic failover capabilities and does not consider additional factors such as cost or performance
- Managed DNS: Adding an intelligence layer to static DNS configuration by introducing smart routing to minimize manual interventions and enhance fault tolerance
- Round-robin: Directs incoming requests to different CDNs sequentially
- Geolocation: Chooses CDN located closest to the user's geographical location

## Benefits

### Improved reliability

Multi CDN helps to ensure that content is delivered even if one of the CDN providers experiences an outage or slowdown. By using multiple CDN providers, content delivery is balanced across different networks, reducing the risk of congestion or failure in a single network.

### Better performance

By selecting the best CDN provider for a particular location or user, Multi CDN enables organizations to optimize content delivery and improve performance. This can lead to lower latency, faster page load times, and a better overall user experience.

### Increased resilience

Multi CDN provides a fallback solution in the event of an outage or slowdown with one CDN provider, ensuring that content delivery continues without disruption. This helps to ensure that users can always access the content they need, even in the face of technical issues.

### Improved security

Multi CDN provides an additional layer of security, as multiple CDN providers can be used to distribute content, reducing the risk of a security breach. This is particularly important for organizations that handle sensitive information, as it helps to ensure that data is protected and secure.

### Enhanced flexibility

Multi CDN provides organizations with the ability to switch between CDN providers on the fly, ensuring that they can always use the best solution for their needs. This enables organizations to respond quickly to changes in their content delivery requirements, and to take advantage of new opportunities as they arise.

## Practices

### Group content by type

By grouping content by type, organizations can ensure that the most appropriate CDN provider is delivering each type of content. For example, static content, such as images and HTML pages, may be best delivered by one CDN provider, while video content may be best delivered by another. This helps to ensure that each CDN provider is delivering the type of content that they are best suited to handle, improving overall performance.

### Institute consistent hashing of your working set

Consistent hashing is a way of distributing content across multiple CDN providers in a balanced manner. It involves dividing the content into segments and then mapping each segment to a specific CDN provider, based on their strengths and weaknesses.

### Establish consistent monitoring parameters

To effectively manage a multi CDN implementation, it is important to have a consistent approach to monitoring performance. This includes monitoring the performance of each CDN provider, as well as the overall performance of the multi CDN solution. This helps to quickly identify and address any issues that arise, and to ensure that the multi CDN solution is functioning optimally.

Use real-time traffic monitoring tools to gather data on performance, latency, and load. With this data, adjust routing dynamically across CDNs, ensuring optimal user experience by selecting the fastest, most reliable path at any given moment.
