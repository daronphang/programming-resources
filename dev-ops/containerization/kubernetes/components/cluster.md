## Cluster

Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit. The abstraction allow you to deploy containerized applications to a cluster without tying them specifically to individual machines.

Kubernetes automates the distribution and scheduling of application containers across a cluster in a more efficient way.

A cluster consists of the Control Plane and Nodes. Can be deployed on either physical or VMs. When applications are deployed, you tell the control plane to start the application containers.

Control plane schedules the containers to run on the cluster's nodes, and the nodes communicate with the control plane using Kubernetes API, which the control plane exposes.
