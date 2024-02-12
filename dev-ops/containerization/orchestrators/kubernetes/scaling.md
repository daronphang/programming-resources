## Horizontal Pod Autoscaler (HPA)

HPA automatically updates a workload resource (Deployment, StatefulSet) with the aim of automatically scaling the workload to match demand.

The response to increased load is to deploy more Pods.

## Vertical Pod Autoscaler (VPA)

VPA automatically adjusts the CPU and memory reservations for the Pods to help 'right size' your applications. This adjustment can improve cluster resource utilization and free up CPU and memory for other Pods.

## Cluster Autoscaler (CA)

CA is a component that automatically adjusts the size of a Kubernetes Cluster so that all pods have a place to run and there are no unneeded nodes.

### Heterogenous cluster

Heterogenous clusters means having multiple instance types per cluster i.e. general purpose cluster. This greatly reduces cluster management overhead, as having fewer, more general purpose clusters reduces the number configurations to test.
