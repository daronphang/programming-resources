## Control Plane (Master/Head Node)

Coordinates all activities in your cluster (worker nodes, pods), such as scheduling applications, maintaining applications' desired state, scaling applications, and rolling out new updates.

In production environments, it usually runs across multiple computers, providing fault tolerance and high availability. Not recommended to run user workloads on master node.

### etcd

Distributed storage system for key values similar to Swarm's RAFT algorithm. Stores configuration information which can be used by each of nodes in cluster. High availability key value store that can be distributed among multiple nodes.

### API Server

Provides all operation on cluster using API. API server implements an interface which means different tools and libraries can readily comunicate with it.

### Controller Manager

Looks at state of the whole cluster and compares the instructions given and output. Responsible for most of collectors that regulate the state of cluster and perform a task. Can be considered as a daemon which runs in a non-terminating loop (event loop) and responsible for collecting and sending information to API server.

### Scheduler

Service in master which is responsible for distributing the workload, tracking utilization of working load on cluster nodes and placing workload on which resources are available and accepting the workload i.e. allocating pods to nodes. Controls how/where containers are placed in Pods.

## Node (Worker/Compute)

VM or physical machine that contains the services necessary to run containerized applications. The worker node hosts the **Pods** that are the components of the application workload. Pods are scheduled and orchestrated to run on nodes. Cluster can be scaled up/down by adding/removing nodes.

Each node has a Kubelet, which is an agent for managing the node and communicating with the Kubernetes control plane. The node should also have tools for handling container operations i.e. containerd or Docker.

Comes unopinionated i.e. don't have to adopt a particular workflow to make something work. Have Imperative and Declarative.

### Docker

Helps running encapsulated application containers in isolated and lightweight operating environment.

### Kubelet Service

Small service in each node responsible for relaying information to and from the control plane service and interacts with etcd store to read configuration details and Wright values.

### Proxy Service

Runs on each node and helps in making services available to external host and forwarding request to correct containers.

### Pods

A group of one or more application containers that are tightly coupled i.e. API and database, and shared resources for them including networking, volumes, and information about how to run each container.

Containers in a Pod share an IP address and port space, are always co-located and co-scheduled, and run in a shared context on the same Node.

Pods that are running inside Kubernetes are running on a private, isolated network. By default, they are visible from other pods and services within the same cluster, but not outside of the network. When we use kubectl, we are interacting through an API endpoint to communicate with our application.

a Pod always run on a Node, and each Node can have multiple pods.

## Namespaces

Namespaces isolate different groups of resources and avoid name collisions by scoping the visibility of your resources. Can be used to divide resources between users and teams by appling **role-based access control**.

## ReplicaSets

Used to consistently replicate a Pod. If a Node/Pod goes offline, Kubernetes will automatically schedule a new Pod instance to maintain the specified replica count.

## Cluster

Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit. The abstraction allow you to deploy containerized applications to a cluster without tying them specifically to individual machines.

Kubernetes automates the distribution and scheduling of application containers across a cluster in a more efficient way.

A cluster consists of the Control Plane and Nodes. Can be deployed on either physical or VMs. When applications are deployed, you tell the control plane to start the application containers.

Control plane schedules the containers to run on the cluster's nodes, and the nodes communicate with the control plane using Kubernetes API, which the control plane exposes.

## Deployment

To deploy containerized applications on top of a running cluster, need to create a Kubernetes Deployment configuration. The Deployment instructs Kubernetes how to create and update instances of your application, and keep them running across Nodes in the event of failure. Resides within the Control Plane. Deployments are the recommended way to manage the creation and scaling of Pods.

When creating a Deployment, need to specify the container image and number of replicas you want to run. Once a deployment is created, the control plane schedules the application instances included in the Deployment to run on individual Nodes in the cluster.

Once the application instances are created, the Deployment Controller continuously monitors those instances. If a node goes down, the controller replaces the instance with an instance on another Node i.e. **provides self-healing mechanism to address machine failure or maintenance**.
