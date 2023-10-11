## Control Plane (Master/Head Node)

A control plane node is a server running collection of system services that make up the control plane of the cluster. Coordinates all activities in your cluster (worker nodes, pods), such as scheduling applications, maintaining applications' desired state, scaling applications, and rolling out new updates.

In production environments, it usually runs across multiple computers, providing fault tolerance and high availability. Not recommended to run user workloads on master node as this frees them up to concentrate entirely on managing the cluster.

### API Server

Provides all operation on cluster using API. API server implements an interface which means different tools and libraries can readily comunicate with it.

**All communication between all components must go through the API server**. It exposes a RESTful API that you POST YAML configuration files (manifests) to over HTTPS. Manifests describe the desired state of an application.

All requests to the API server are subjected to authentication and authorization checks. Once these are done, config in the YAML is validated, persisted to the cluster store, and work is scheduled to the cluster.

### Cluster Store

The cluster store is the only stateful part of the control plane and persistently stores the entire configuration and state of the cluster. The cluster store is based on etcd.

#### etcd

Distributed storage system for key values similar to Swarm's RAFT algorithm. Stores configuration information which can be used by each of nodes in cluster. High availability key value store that can be distributed among multiple nodes.

As it is the single source of truth for the cluster, you should run berween 3-5 etcd replicas for high-availability, and should provide adequate ways to recover when things go wrong. A default installation of Kubernetes installs a replica of the cluster store on every control plane node, and automatically configures HA.

On top of availability, etcd prefers consistency over availability. This means it does not tolerate split-brains and will halt updates to the cluster in order to maintain consistency.

As with all distributed databases, consistency of writes is vital. RAFT consensus algorithm is used to accomplish this.

### Controller Manager

The controller manager implements all the background controllers that monitor cluster components and respond to events. Looks at the state of the whole cluster and **ensures the observed state matches the desired state**. Can be considered as a daemon which runs in a non-terminating loop (event loop) and responsible for collecting and sending information to API server.

Responsible for most of collectors that regulate the state of cluster and perform a task. Architecturally, it is a controller of controllers i.e. spawns independent controllers and monitors them. Examples include:

- Deployment controller
- StatefulSet controller
- ReplicaSet controller

Logic implemented by each controller is as follows:

1. Obtain desired state
2. Observe current state
3. Determine differences
4. Reconcile differences

### Scheduler

Service in master which is responsible for distributing the workload, tracking utilization of working load on cluster nodes and placing workload on which resources are available and accepting the workload i.e. allocating pods to healthy nodes. Controls how/where containers are placed in Pods.

Behind the scenes, it implements complex logic that filters out nodes incapable of running tasks with a ranking system.
