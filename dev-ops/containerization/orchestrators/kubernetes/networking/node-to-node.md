## Node Networking Models

Kubernetes support various networking models that determine how nodes communicate with each other.

### Overlay

- Each Node has its own private network
- Containers within a Node communicate over this private network
- Containers across Nodes communicate over an overlay network
- Overlay networks encapsulte packets and route them between nodes using an overlay network driver (VXLAN, Flannel)

### Underlay

- All Nodes share a single flat network
- Each Node has a unique IP address within this network
- Containers communicate with each other using the Node's IP address and port mapping

## Communication Mechanisms

### kube-proxy

- kube-proxy is a network proxy and load balancer running on each Node
- Handles service-based communication within the cluster
- Maintains a set of network rules and ensures that traffic is correctly forwarded to the appropriate destination
- Supports different proxy modes i.e. userspace, iptables, IPVS

### Service Discovery

- Kubernetes offers a built-in service discovery mechanism that allows containers to locate other containers/services
- Kubernetes DNS service automatically assigns a DNS name to each service, making it discoverable by other containers within the cluster

### Pod Networking

- Kubernetes assigns a unique IP address to each Pod within a cluster
- Pods communicate with each other directly using their IP addresses
