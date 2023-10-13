## Node (Worker/Compute)

A machine that can be a physical machine, VM, Raspberry Pis, or cloud instances that contains the services necessary to run containerized applications. The worker node hosts the **Pods** that are the components of the application workload. Pods are scheduled and orchestrated to run on nodes. Cluster can be scaled up/down by adding/removing nodes.

Each node has a Kubelet, which is an agent for managing the node and communicating with the Kubernetes control plane. The node should also have tools for handling container operations i.e. containerd or Docker.

Comes unopinionated i.e. doesn't have to adopt a particular workflow to make something work. Have Imperative and Declarative.

### Kubelet

Small service in each node responsible for relaying information to and from the control plane service and interacts with etcd store to read configuration details and Wright values. One of the main jobs is to watch the API server for new work tasks, executes and maintains a reporting channel back to the control plane.

### Container runtime

The kubelet needs a container runtime to perform container-related tasks including pulling images, and starting and stopping containers. Kubernetes has dropped native support for Docker, and replaced it with containerd that implements the CRI.

### Kube-proxy

Runs on each node and helps in making services available to external host and forwarding request to correct containers i.e. responsible for local cluster networking. It ensures each node gets its own unique IP address, and implements local iptables or IPVS rules to handle routing and load-balancing of traffic on the Pod network.
