## Elastic Network Interface (ENI)

An ENI is a logical networking component in a VPC that represents a virtual network card. It can include the following attributes:

- A primary private IPv4 address from the CIDR range of VPC
- A primary IPv6 address from the CIDR range of VPC
- One or more secondary private IPv4 addresses from the CIDR range of VPC
- One public IPv4 address
- One or more IPv6 addresses
- One or more security groups
- A MAC address
- A source/destination check flag

From a security perspective, ENIs play a crucial role in protecting your AWS infrastructure.

You can create and configure network interfaces and attach them to instances in the same AZ. Separates and virtualizes the networking aspect of your EC2 instances. ENI can be detached and attached to different EC2 instances (but an ENI belongs to a single VM). Flow logs can be enabled to capture information about IP traffic going to and from the ENI.

When you launch an EC2 instance, it will be configured with a **primary ENI** called 'ethernet zero' which is assigned a primary private IPv4 address. The primary ENI cannot be detached while the EC2 is running or stopped i.e. fixed to the EC2 instance.

You can attach **secondary ENIs** to EC2. They are useful for scenarios including network appliances, management networks, or to create a low budget high availability solution. It can have one primary and multiple secondary private IP addresses. They can also be associated with different security groups than the primary ENI, allowing for varied network and security configurations. Secondary ENIs will persist even if the EC2 instances are stopped.

If you have an Elastic IP address, **you can associate it with one of the private IPv4 addresses for the network interface**. You can associate one Elastic IP address with each private IPv4 address.

## Elastic Network Adapter (ENA)

Many AWS customers create high-performance systems that run across multiple EC2 instances and make good use of all available network bandwidth. To take advantage of the increased concurrency (more vCPUs) found in today’s processors, can make use of ENA that provides up to 20 Gbps of consistent, low-latency performance when used within a Placement Group, at no extra charge.

**ENA will scale as network bandwidth grows and the vCPU count increases**; this will allow you to take advantage of higher bandwidth options in the future **without the need to install newer drivers or to make other changes to your configuration**, as was required by earlier network interfaces.

## Elastic Fabric Adapter (EFA)

Elastic Fabric Adapter (EFA) is a network interface for Amazon EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS. Its custom-built operating system (OS) bypass hardware interface enhances the performance of inter-instance communications, which is critical to scaling these applications.

With EFA, High Performance Computing (HPC) applications using the Message Passing Interface (MPI) and Machine Learning (ML) applications using NVIDIA Collective Communications Library (NCCL) can scale to thousands of CPUs or GPUs. As a result, you get the application performance of on-premises HPC clusters with the on-demand elasticity and flexibility of the AWS cloud.

EFA is suitable for applications that require extremely low network latency and high throughout for communication between multiple EC2 instances.

EFA is available as an optional EC2 networking feature that you can enable on any supported EC2 instance at no additional cost.

The OS-bypass capabilities of EFAs are **not supported on Windows instances**. If you attach an EFA to a Windows instance, the instance functions as an Elastic Network Adapter without the added EFA capabilities.
