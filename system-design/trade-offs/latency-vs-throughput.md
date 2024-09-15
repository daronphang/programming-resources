## Latency vs throughput

Latency and throughput are two critical performance metrics in software systems, but they measure different aspects of the system's performance.

## Latency

Latency is the time it takes for a piece of data to travel from its source to its destination. Lower latency indicates a more responsive system. It is the delay between the initiation of a request and the receipt of the response.

Latency is particularly important in scenarios where real-time or near-real-time interaction or data transfer is crucial e.g. online gaming, video conferencing, high-frequency trading. Latency focuses on **speed**.

### How to improve latency

- **Optimize network routes**: Use CDNs to serve content from locations geographically closer to the user
- **Implement caching**: Cache frequently accessed data in memory to reduce the need for repeated data processing (follow 80-20 rule)
- **Upgrade hardware**: Faster processors, more memory, quicker storage (SSDs) can reduce processing time
- **Use faster communication protocols**: HTTP/2
- **Database optimization**: Use indexing, optimized queries, and in-memory databases to reduce data access and processing time
- **Load balancing**: Distribute incoming requests efficiently among servers to prevent any single server from becoming a bottleneck
- **Code optimization**: Optimize algorithms and remove unnecessary computations to speed up execution
- **Minimize external calls**: Reduce the number of API calls or external dependencies in your application
- **Parallel processing**: Use parallel computing techniques where tasks are divided and processed simultaneously
- **Async processing**: Execute long running tasks in the background
- **Data compression**: Compress data before sending over the network

## Throughput

Throughput refers to the amount of data transferred over a network or processed by a system in a given amount of time. It's a measure of how much work or data processing is completed over a specific period i.e. Mbps.

Throughput is a critical measure in systems where the volume of data processing is significant, such as in data backup systems, bulk data processing, or video streaming services. Throughput focuses on **capacity**.

### How to improve throughput

- **Scale horizontally**: Add more servers to handle increased load
- **Implement caching**: Cache frequently accessed data in memory to reduce the need for repeated data processing (follow 80-20 rule)
- **Parallel processing**: Use parallel computing techniques where tasks are divided and processed simultaneously
- **Batch processing**: For non-real-time data, processing in batches can be more efficient than processing each item individually
- **Optimize database performance**: Ensure efficient data storage and retrieval such as partitioning and sharding
- **Asynchronous processing**: Use asynchronous processes for tasks that don’t need to be completed immediately
- **Network bandwidth**: Increase the network bandwidth to accommodate higher data transfer rates
- **Data compression**: Perform data compression to reduce size during transfer
