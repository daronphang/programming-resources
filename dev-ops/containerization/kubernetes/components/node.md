## Node (Worker/Compute)

VM or physical machine that contains the services necessary to run containerized applications. The worker node hosts the **Pods** that are the components of the application workload. Pods are scheduled and orchestrated to run on nodes. Cluster can be scaled up/down by adding/removing nodes.

Each node has a Kubelet, which is an agent for managing the node and communicating with the Kubernetes control plane. The node should also have tools for handling container operations i.e. containerd or Docker.

Comes unopinionated i.e. don't have to adopt a particular workflow to make something work. Have Imperative and Declarative.

## Docker

Helps running encapsulated application containers in isolated and lightweight operating environment.

## Kubelet Service

Small service in each node responsible for relaying information to and from the control plane service and interacts with etcd store to read configuration details and Wright values.

## Proxy Service

Runs on each node and helps in making services available to external host and forwarding request to correct containers.

## Pods

A Pod is the smallest unit that can be deployed and managed by Kubernetes i.e. containers. Pods can contain multiple containers that are tightly coupled (deployed on the same server in pre-container world). A Pod always run on a Node, and each Node can have multiple pods.

**Each Pod is meant to run a single instance of a given application**. If you want to scale horizontally, should use multiple Pods, one for each instance i.e. replication.

Pods that are running inside Kubernetes are running on a private, isolated network. By default, they are visible from other pods and services within the same cluster, but not outside of the network. When we use kubectl, we are interacting through an API endpoint to communicate with our application.

### Motivation

Having an additional layer of abstraction by the Pod instead of deploying a single container directly is needed as Kubernetes requires additional information including restart policy or live probe to manage a container. Instead of overloading the existing container, using a new entity, Pod, that logically wraps one or more containers and managed as a single entity.

### Multi-Container Pods

Primary purpose is to support co-located, co-managed helper processes for a primary application including proxies (Apache, Nginx), bridges, adapters, log/data watchers, etc.

Grouping multiple containers is a relatively advanced use case, and should only use in specific instances when your containers are tightly coupled.

Containers in a Pod will share resources including networking (IP address, namespace), volumes, and information about how to run each container. They are always co-located and co-scheduled, and run in a shared context on the same Node.

### Pods Assignment

The selection of appropriate nodes onto which to schedule Pods is handled by Kubernetes scheduler. Ensures that the right node is selected by checking its capacity for CPU and RAM, and comparing it to the Pod's resource requests.

### Pods Distribution

To avoid assignment of multiple replicas of a Pod on a single worker Node, can configure PodAntiAffinity.
