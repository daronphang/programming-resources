## Denial of Service (DoS)

There are many types of DoS attacks, but a well-known variation is overloading a system to the point it can no longer service requests.

### Protecting cluster resources

A best practice is to replicate essential control plane services on multiple nodes for high availability. You should also consider replicating control plane nodes across availability zones. For worker nodes, you should configure appropriate limits to help **prevent system resources from being starved** for the following:

- Memory
- CPU
- Storage
- Kubernetes objects

### Protecting cluster store

A default installation of Kubernetes installs etcd on the same servers as the rest of the control plane. However, large production clusters should consider a dedicated etcd cluster. This will provide better performance and greater resilience.

On the performance front, **etcd is the most common choking point** for large Kubernetes clusters. Hence, you should perform testing to ensure the infrastructure it runs on is capable of sustaining performance at scale.
