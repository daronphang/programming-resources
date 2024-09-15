## Back-of-the-envelope

Back-of-the-envelope estimation is a technique used to quickly approximate values and make rough calculations using simple arithmetic and basic assumptions. The unknown performance numbers can be determined through prototyping.

The back of the envelope calculation is commonly used to evaluate different architectural designs. Although the optimal design depends on the system requirements, the back of the envelope calculation provides an opportunity to compare different architectural designs without prototyping.

The back of the envelope calculation is also known as **capacity planning**. In general, measuring system performance and performing back of the envelope is important in any deployment to satisfy the service level agreement (**SLA**). Following are some of the popular reasons:

- Decide whether the database should be partitioned
- Evaluate the feasibility of a proposed architectural design
- Identify potential bottlenecks in the system
- Ensuring high availability
- Improving cost efficiencies
- Meeting SLAs
- Providing insights into hot workflows and traffic spikes
- Predicting system capacity requirements

## How to calculate

The back of the envelope calculation should be performed for efficient resource management and to meet scalability requirements. The different approaches to scaling a web service are the following:

- Vertical scaling
- Horizontal scaling
- Diagonal scaling (hybrid)

The back of the envelope calculation allows you to identify the sweet spot between diagonal scaling and a feasible price point. The following concepts should be well understood to perform a quick back of the envelope calculation:

- Powers of two
- Availability numbers
- Latency numbers

You should also make reasonable assumptions.

### Powers of two

The power of two is a handy reference to perform the back of the envelope.

```
Power   Exact Value     Bytes
7       128
8       256
10      1024            1 KB
16      65,536          64 KB
20      1,048,576       1 MB
30      1,073,741,824   1 GB
```

### Availability numbers

High availability is the ability of a service to remain reachable and not lose data even when a failure occurs. High availability is typically measured in terms of a percentage of uptime over a given period.

A service-level agreement (**SLA**) is an explicit or implicit contract between a service provider and the users. The SLA documents the set of services the service provider will offer to the user and defines the service standards the provider is obligated to fulfill.

```
Availability        Downtime per year
99%                 3.6days
99.99%              52 minutes
99.999%             5 minutes
99.9999%            31 seconds
```

### Latency numbers

The latency numbers can be summarized as the following:

- Read from memory is fast and disks are slow
- Network bandwidth can be saved by using a compression algorithm
- Writes are more expensive than reads
- Globally shared data is expensive
- At most 7 round trips between inter-region data centers per second are possible
- Approximately 2000 round trips per second can be achieved within a data center

```
Operation                           Time
L1 cache reference                  0.5 ns
Mutex lock/unlock                   25 ns
Main memory reference               100 ns
HDD seek                            10 ms
Read 1 MB from SSD                  1 ms
Round trip within same datacenter   500 us
```

## Calculation types

Common types of back of the envelope calculations include:

- Traffic estimation
- Storage estimation
- Memory estimation
- Bandwidth estimation
- Resource estimation
- Latency estimation

### Load estimation

Queries per second (QPS) is a metric used to measure the number of requests for information a server receives per second. It is commonly used to measure how much traffic an information retrieval system (search engine, database) is receiving and, therefore, its capacity.

Suppose you’re asked to design a social media platform with 100 million daily active users (DAU) and an average of 10 posts per user per day. To estimate the load, you’d calculate the total number of posts generated daily:

```
100 million DAU * 10 posts/user = 1 billion posts/day
QPS = 1 billion post/day / 86,400 seconds = 11,574 requests/second
```

### Latency estimation

When fetching an API from multiple resources and data fetching process is sequential:

```
latency = latency_resource_1 + latency_resource_2
```

When fetching process is parallel:

```
latency = max(latency_resource_1, latency_resource_2)
```

### Resource estimation

Imagine you’re designing a web application that receives 10,000 requests per second, with each request requiring 10 ms of CPU time. Assuming each CPU can handle 1,000ms of processing per second, to estimate the number of CPU cores needed, you can calculate the total CPU time per second:

```
10,000 requests/second * 10 ms/request = 100,000 ms/second
100,000 ms/second / 1,000 ms/core = 100 cores
```

## Example

Given the following traffic for URL shortener:

- DAU (write): 100 million
- QPS (write): 1000
- QPS (read): 100,000
- Time of persistence of data: 5 years

### Storage

Assuming 1 byte per character, an average URL is approximately 2.5 KB in size.

```
Storage required = 2.5 KB/URL * 100 million URL/day * 300 days * 5 years * 3 replication
= 1.35 PB
```

### Bandwidth

```
Ingress = 2.5 KB/URL * 10 billion URL/day = 250MB/sec
```

### Memory

The URL redirection traffic (egress) is cached to improve the latency. Following the 80/20 rule, 80% of egress is served by 20% of URL data stored on the cache servers. The remaining 20% of the egress is served by the cache store to improve the latency. A Time-to-live (TTL) of 1 day is reasonable.

```
Memory = 2.5KB/URL * 10 billion URL/day * 0.2
= 5 TB/day
```
