## Kube-router

In Kubernetes, you need to solve three major networking problems:

1. Pod-to-Pod communication (across nodes)
2. Service load balancing
3. Network isolation (NetworkPolicy)

However, multiple components are required:

- CNI plugin (Calico, Flannel, Cilium)
- kube-proxy
- Network policy engine

kube-router is a Kubernetes networking solution that turns each node into a smart router, providing operational simplicity and high performance. It is a powerful alternative to several networking components used in a typical Kubernetes cluster, but abstracted into a single DaemonSet that runs one Pod per node. It provides:

- **Pod networking (CNI plugin)**: Uses native Linux routing and BGP to ensure other nodes know how to reach each Pod
- **Service proxy (replaces kube-proxy)**: Uses Linux IPVS/LVS to provide L4 load balancing. Kube-router watches the Kubernetes API server to get updates on the Services/Endpoints and automatically syncs the IPVS configuration to reflect the desired state of Services
- **Network policy controller**: Enforces Network Policy using iptables rules, controlling which Pod can talk to which Pod
- **BGP routing**: Each node runs as a BGP speaker, and advertises its Pods CIDR to other nodes. This allows direct routing (no overlay encapsulation) and integration with DC networks. The subnet of the node is obtained from the CNI configuration file on the node or through the Node.PodCidr

```
Node A has Pod CIDR: 10.1.0.0/24
Node B has Pod CIDR: 10.2.0.0/24
```
