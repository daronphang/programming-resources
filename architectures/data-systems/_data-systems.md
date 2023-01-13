## Data Systems

Many applications today are data-intensive as opposed to compute-intensive that provide commonly needed functionality:

- Storing data (databases)
- Remembering the results of an expensive operation (caching)
- Allowing users to search data by keyword or filter (search indexes)
- Sending a message to another process, to be handled asynchronously (stream processing)
- Periodically crunch a large amount of accumulated data (batch processing)

Increasingly, many applications have such demanding or wide-ranging requirements that a single tool can no longer meet all of its data processing and storage needs. When you combine several tools in order to provide a service, the API usually hides those implementation details from clients. However, designing such data-systems are tricky, and many factors influencing the design including legacy system dependencies, timescale for delivery, risk tolerance, regulatory constraints, etc. Nonetheless, three concerns that are important are reliability, scalability and maintainability.

## Reliability

Reliability means making systems work correctly, even when faults occur. Expectations include:

- Application performs the function that the user expects
- Can tolerate user making mistakes or using software in unexpected ways
- Performance is good enough for the required use case
- System prevents any unauthorized access and abuse

### Faults

The things that can go wrong/deviate from spec are called faults, and systems that anticipate and cope with them are fault-tolerant/resilient. Faults are different from failures, which is when the system as a whole stops providing the required service to the user. As it is impossible to reduce probability of a fault to zero, we can design fault-tolerance mechanisms that prevent faults from causing failures.

Counterintuitively, it can make sense to increase rate of faults by triggering them deliberately i.e. Chaos Monkey from Netflix. This ensures that the fault-tolerance machinery is continually exercised and tested, hence, increasing confidence.

#### Software

For systemic errors, they often lie dormant until they are triggered by an unusual set of circumstances i.e. reveals that the software is making some assumption about its environment.

## Scalability

Term used to describe a system's ability to cope with increased load, where we need to succinctly describe the current load parameters i.e. requests per second to a web server, ratio of reads to writes in a database, etc.

### Latency vs Response

**Response** time is what the client sees, which includes service time (actual time to process the request), network and queuing delays. **Latency** is the duration that a request is waiting to be handled.

### Performance

Should use percentiles (median is 50th) instead of mean. To figure out how bad outliers are, should look at higher percentiles i.e. if 95th percentile response time is 1.5s, 95/100 requests took less than 1.5s.

Optimizing the 99.99th percentile (tail latencies) are iportant as they are usually the customers who have the most data on their accounts i.e. most valuable customers. However, it can be too expensive and not yielding enough benefit as reducing response times at very high percentiles is difficult and they are easily affected by random events outside of your control.

Can efficiently calculate response time percentiles on an ongoing basis i.e. rolling window of requests in the last 10 minutes.

## Maintainability

Making life easier for engineering and operations teams who need to work with the system. Good abstractions can help reduce complexity and make the system easier to modify and adapt for new use cases.
