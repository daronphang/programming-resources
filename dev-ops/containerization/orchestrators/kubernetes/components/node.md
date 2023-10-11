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

## Pods

A Pod is the smallest unit that can be deployed and managed by Kubernetes i.e. containers. Pods can contain multiple containers that are tightly coupled (deployed on the same server in pre-container world). A Pod always run on a Node, and each Node can have multiple pods.

**Each Pod is meant to run a single instance of a given application** i.e. one-container-per-pod model. If you want to scale horizontally, should use multiple Pods, one for each instance i.e. replication. Kubernetes manages Pods rather than managing containers directly.

Pods that are running inside Kubernetes are running on a private, isolated network. By default, they are visible from other pods and services within the same cluster, but not outside of the network. When we use kubectl, we are interacting through an API endpoint to communicate with our application.

### Motivation

Having an additional layer of abstraction by the Pod instead of deploying a single container directly is needed as Kubernetes requires additional information including restart policy or live probe to manage a container. Instead of overloading the existing container, using a new entity, Pod, that logically wraps one or more containers and managed as a single entity.

### Multi-Container Pods

Primary purpose is to support co-located, co-managed helper processes for a primary application including proxies (Apache, Nginx), bridges, adapters, log/data watchers, sidecars etc. Examples include:

- Service meshes
- Web containers supported by a helper container pulling updated content
- Containers with a tightly coupled log scraper

Grouping multiple containers is a relatively advanced use case, and should only use in specific instances when your containers are tightly coupled.

Containers in a Pod will **share resources** including networking (IP address, namespace), volumes, and information about how to run each container. They are always co-located and co-scheduled, and run in a shared context on the same Node. To communicate with each other, they can use the Pod's localhost.

### Pods Assignment

The selection of appropriate nodes onto which to schedule Pods is handled by Kubernetes scheduler. Ensures that the right node is selected by checking its capacity for CPU and RAM, and comparing it to the Pod's resource requests.

### Pods Distribution

To avoid assignment of multiple replicas of a Pod on a single worker Node, can configure PodAntiAffinity.

### Service Mesh

It is recommended to put each container in one Pod and loosely couple them over the network. However, this creates a lot of potentially un-encrypted network traffic. Should consider using a service mesh to secure traffic between Pods and application services.

### Pods Deployment

The deployment of a Pod is an atomic operation i.e. it is only ready for service when all its containers are up and running.
