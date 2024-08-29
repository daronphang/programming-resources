## Sidecars and service mesh

One of the design goals of microservices architectures is a high degree of decoupling, often manifested in the advice “Duplication is preferable to coupling.”

Architects generally frown on duplicating code because it causes synchronization issues, semantic drift, and a host of other issues, but sometimes forces exist that are worse than the problems of duplication, and coupling in microservices often fits that bill. Hence, the answer to the question of "should we duplicate or couple to some capability?" is "it depends".

For common operational capabilities such as monitoring, logging, authentication, authorization, circuit breakers that each service should have, they can benefit from **high coupling**, as allowing each team to manage these dependencies often descends into chaos.

The common solution that has emerged in the microservices ecosystem is the **service mesh with sidecar pattern**.

If architects and operations can safely assume that every service includes the sidecar component (governed by fitness functions), it forms a service mesh, with services interconnecting with each other.

Having a mesh allows architects and DevOps to create dashboards, control operational characteristics such as scale, and a host of other capabilities.
