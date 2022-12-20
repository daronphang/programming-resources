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
