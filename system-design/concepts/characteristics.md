## Key characteristics of distributed systems

Key characteristics of a distributed system include Scalability, Reliability, Availability, Efficiency, and Manageability.

## Scalability

Scalability is the capability of a system, process, or a network to grow and manage increased demand. Any distributed system that can continuously evolve in order to support the growing amount of work is considered to be scalable.

A system may have to scale because of many reasons like increased data volume or increased amount of work, e.g., number of transactions. A scalable system would like to achieve this scaling without performance loss.

Generally, the performance of a system declines with the system size due to the management or environment cost. For instance, network speed may become slower because machines tend to be far apart from one another. More generally, some tasks may not be distributed, either because of their inherent atomic nature or because of some flaw in the system design. At some point, such tasks would limit the speed-up obtained by distribution. A scalable architecture avoids this situation and attempts to balance the load on all the participating nodes evenly.

Scaling can achieved by:

- Vertical: Adding more power (CPU, RAM, storage) to existing server
- Horizontal: Adding more servers into your pool of resources

## Reliability

Reliability refers to the ability of a system to continue operating correctly and effectively in the presence of faults, errors, or failures.

Obviously, redundancy has a cost and a reliable system has to pay that to achieve such resilience for services by eliminating every single point of failure.

## Availability

Availability is the time a system remains operational to perform its required function in a specific period.

### Reliability vs availability

If a system is reliable, it is available. However, **if it is available, it is not necessarily reliable**. In other words, it is possible to achieve high availability for an unreliable service.

## Efficiency

Two standard measures of its efficiency are:

- Latency: Delay to obtain the first item
- Bandwidth (throughput): The number of items delivered in a given time unit

Operations that can be measured include:

- Time taken for searching a specific key in a distributed index
- Number of messages sent globally by nodes, regardless of the message size

However, it is quite difficult to develop a precise cost model that would accurately take into account all these performance factors; therefore, we have to live with rough but robust estimates of the system behavior.

## Serviceability or manageability

Another important consideration while designing a distributed system is how easy it is to operate and maintain. Serviceability or manageability is the simplicity and speed with which a system can be repaired or maintained.

Early detection of faults can decrease or avoid system downtime.
