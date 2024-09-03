## Cluster

Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit. The abstraction allow you to deploy containerized applications to a cluster without tying them specifically to individual machines.

Kubernetes automates the distribution and scheduling of application containers across a cluster in a more efficient way.

A cluster consists of the **Control Plane and Nodes**. Can be deployed on either physical or VMs. When applications are deployed, you tell the control plane to start the application containers.

Control plane schedules the containers to run on the cluster's nodes, and the nodes communicate with the control plane using Kubernetes API, which the control plane exposes.

## Kubernetes Playgrounds

Playgrounds are the easiest way to get Kubernetes, but they are not for production. Examples include:

- Play with Kubernetes
- Katakoda
- Docker Desktop
- minikube
- k3d

## Hosted Kubernetes

All major cloud platforms offer a hosted Kubernetes service. This is a model where you outsource a bunch of Kubernetes infrastructure responsibility to your cloud provider, letting them take care of things including high availability, performance, and updates. Popular services include:

- AWS Elastic Kubernetes Service (EKS)
- Azure Kubernetes Service (AKS)
- Linode Kubernetes Engine (LKE)
- DigitalOcean Kubernetes (DOKS)
- GCP Kubernetes Engine (GKE)
