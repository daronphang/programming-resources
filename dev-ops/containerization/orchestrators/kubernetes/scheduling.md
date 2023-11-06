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

## Taints and Tolerations

Node affinity is a property of Pods that attracts them to a set of nodes. Taints are the opposite - they allow a node to **repel** a set of Pods.

**Tolerations are applied to Pods**. Tolerations allows the scheduler to schedule Pods with **matching taints**. Tolerations allow scheduling but don't guarantee scheduling as it also evaluates other parameters as part of its function.

Taints and tolerations work together to ensure that Pods are not scheduled onto inappropriate nodes. One or more **taints are applied to a node**; this marks that the node should not accept any Pods that do not tolerate the taints.

However, taints and tolerations **do not tell the Pod to go to a particular Node** i.e. Pod with matching toleration may not be scheduled on node with matching taint. Instead, it tells the node to only accept Pods with matching tolerations.

```bash
# no Pod can schedule onto node1 unless it has a matching toleration
$ kubectl taint nodes node1 key1=value1:NoSchedule
```

```yaml
# specified for a Pod in PodSpec
# tolerations must match with taint in order
# to be scheduled onto the node
tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    # NoSchedule, PreferNoSchedule NoExecute
    effect: "NoSchedule"

---
tolerations:
  - key: "key1"
    operator: "Exists"
    effect: "NoSchedule"
```

## Node Selectors

NodeSelector is the simplest recommended form of node selection constraint. You can add the nodeSelector field to your Pod spec and specify the node labels you want the target node to have. Kubernetes only schedules the Pod onto nodes that have each of the labels you specify. However, for **more complex rules**, use node affinity and anti-affinity features.

```yaml
apiVersion:
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: nginx
      image: nginx
  nodeSelector:
    # key/value pairs
    size: large
```

```bash
$ kubectl label nodes <node-name> <key>=<value>
$ kubectl label nodes node1 size=large
```

## Node affinity and anti-affinity

Affinity and anti-affinity expands the types of constraints you can define. Some of the benefits include:

- Language is more expressive and gives you more control over selection logic
- You can indicate that a rule is soft/preferred
- You can constrain a Pod using labels on other Pods running on the node

There are two types of node affinity:

- **requiredDuringSchedulingIgnoredDuringExecution**: The scheduler can't schedule the Pod unless the rule is met
- **preferredDuringSchedulingIgnoredDuringExecution**: The scheduler tries to find a node that meets the rule and if no matching nodes are found, the scheduler ignores the rule and schedules the Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: topology.kubernetes.io/zone
                operator: In
                values:
                  - antarctica-east1
                  - antarctica-west1
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 1
          preference:
            matchExpressions:
              - key: another-node-label-key
                operator: In
                values:
                  - another-node-label-value
  containers:
    - name: with-node-affinity
      image: registry.k8s.io/pause:2.0
```
