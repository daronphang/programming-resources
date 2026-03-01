## Cilium

Cilium is a cloud-native networking, security and observability platform for Kubernetes, built on eBPF. Cilium replaces or enhances Kubernetes networking by using eBPF to provide high-performance networking, fine-grained security, and deep observability. Cilium runs as a DaemonSet, with one Cilium agent per node, not per Pod.

## Traffic routing

Cilium can act as a CNI plugin to provide pod-to-pod connectivity. Whenever a packet is sent to a Service VIP or pod IP, Cilium handles the routing (intercepts packet in the kernel). Advantages include:

- High performance: All decisions are made in the kernel with minimal context switching
- Identity-based routing: Policies are pod/service-aware, not IP-based
- Scalable: Handles thousands of Services/Pods efficiently
- Observability: Tracks which Pod sent traffic to which Pod/Service
