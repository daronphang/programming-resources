## Scheduling

In Kubernetes, scheduling refers to making sure that Pods are matched to Nodes so that Kubelet can run them.

Even distribution of Pods across all Nodes in a cluster is crucial:

- **Load Balancing**: Even distribution ensures that no single node is overwhelmed with too many pods, leading to better performance and stability
- **High Availability**: If one Node fails, only a fraction of Pods are affected, minimizing the impact on your applications
- **Resource Utilization**: By spreading Pods evenly, you can make the most of your resources, avoiding waste and saving costs

## Kube-scheduler

Kube-scheduler is the default scheduler for Kubernetes and runs as a part of the Control-plane. You can also write your own scheduling component if needed.

Kube-scheduler selects an optimal node to run newly created/unscheduled Pods. As containers in Pods, or Pods themselves, can have different requirements, the scheduler filters out any nodes that don't meet a Pod's specific scheduling needs.

In a cluster, Nodes that meet the scheduling requirements for a Pod are called **feasible nodes**. If none of the Nodes are suitable, the Pod remains unscheduled.

Factors that need to be taken into account for scheduling decisions include:

- Individual and collective resource requirements
- Hardware/software/policy constraints
- Affinity and anti-affinity specifications
- Data locality
- Inter-workload interference

## Node Selection

A scheduler watches for newly created Pods that have no Node assigned, and becomes responsible for finding the best Node for that Pod to run. The scheduler reaches this placement decision by taking into account the scheduling principles of filtering and scoring.

### Filtering

The filtering step finds the set of Nodes where it is feasible to schedule the Pod i.e. checking resource requirements, hardware, software, etc.

### Scoring

In the scoring step, the scheduler ranks the remaining nodes to choose the most suitable Pod placement. The scheduler assigns a score to each Node that survived filtering, basing this score on the active scoring rules.

### Assignment

Finally, kube-scheduler assigns the Pod to the Node with the highest ranking. If there is more than one Node with equal scores, it is selected at random.
