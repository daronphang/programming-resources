## Elastic Cloud Compute (EC2)

Provides compute capacity in the cloud that is secure and resizable based on the user's requirements. Web service that allows developers to rent VMs and automatically scales the compute capacity when required.

Offers various instance types so that developers can choose required resources including CPU, memory, storage and networking capacity.

### Components

When launching an EC2 instance, the following are required/optional:

- Instance type
- Storage type
- OS (AMI)
- User data (optional)
- Tenancy (optional)

### Instance Types

The instance can be broken down as follows:

- First position (c): Indicates the instance family
- Second position (5): Indicates the generation of the instance
- Remaining letters before period (n): Indicates additional attributes
- After the period (xlarge): Indicates the instance size (including CPU and RAM)

```
c5n.xlarge
```

### Lifecycle

Pending, running, rebooting, and stopping.

### EC2 instance placements

- Cluster placement group: For applications that need low network latency and high network throughput such as big data and analytics workloads
- Partition placement group: Instances do not share underlying hardware with instances in other partitions, for distributed, replicated workloads
- Spread placement group: Instances have distinct underlying hardware to reduce correlated failures with its own network and power source

## Amazon Machine Image (AMI)

When launching an EC2 instance, the first setting you configure is which OS you want by selecting an AMI.

In the traditional infrastructure world, spinning up a server consists of installing an OS from installation disks, drives, or wizards over the network. In AWS, the OS installation is built into the AMI.

An AMI includes the OS, storage mapping, architecture type, launch permissions, and any additional preinstalled software applications. You must use an AMI from the same region as that of the EC2 instance, but the region of the AMI has no bearing on the performance of the EC2 instance.

There are multiple ways to select an AMI:

- AWS Marketplace
- Personal AMIs
- Community
- Custom image

Each AMI in the AWS Management Console has an AMI ID, which is prefixed by `ami-`.

### AMI and EC2 instances

The AMI is how you model and define your instance i.e. AMI is the class, EC2 is the instance.

One advantage of using AMIs is that they are reusable. If you can spin up another EC2 instance with the same configuration, you can simply create an AMI from your running instance and use it to start a new instance.

## EC2 Image Builder

EC2 Image Builder is used to automate the creation, maintenance, validation and testing of VMs or container images:

1. Creates an EC2 instance
2. Builds components and customize software on instance
3. Creates an AMI
4. Runs a test suite on AMI (working, secure, etc.)
5. Distributes AMI to multiple Regions

It is a **free** service and only pay for the underlying resources i.e. EC2, AMI storage, etc. It can be run on a schedule.

### Features

- Automated image creation
- Golden image creation
- Simpler to secure
- Consistent workflow
- Version management

## EC2 User Data

It is possible to bootstrap our instances using an EC2 User Data script (runs with root user). Bootstrapping means launching commands when a machine starts.

The script is run once at the instance first start and is used to automate boot tasks including:

- Installing updates
- Installing software
- Downloading common files from the internet

```sh
#!bin/bash
$ yum update -y
$ yum install -y httpd
$ systemctl start httpd
$ systemctl enable httpd
```

## Connecting to EC2

Can either use SSH (port 20), Putty or EC2 Instance Connect (uses temporary SSH keys).

## Elastic Network Interface (ENI)

An ENI is a logical networking component in a VPC that represents a virtual network card. It can include the following attributes:

- A primary private IPv4 address
- A primary IPv6 address
- One or more secondary IPv4 addresses
- One public IPv4 address
- One or more security groups
- A MAC address

From a security perspective, ENIs play a crucial role in protecting your AWS infrastructure.

You can create and configure network interfaces and attach them to instances in the same AZ. Separates and virtualizes the networking aspect of your EC2 instances. ENI can be detached and attached to different EC2 instances. Flow logs can be enabled to capture information about IP traffic going to and from the ENI.

When you launch an EC2 instance, it will be configured with a **primary ENI** called 'ethernet zero' which is assigned a primary private IPv4 address. The primary ENI cannot be detached while the EC2 is running or stopped i.e. fixed to the EC2 instance.

You can attach **secondary ENIs** to EC2. They are useful for scenarios including network appliances, management networks, or to create a low budget high availability solution. It can have one primary and multiple secondary private IP addresses. They can also be associated with different security groups than the primary ENI, allowing for varied network and security configurations. Secondary ENIs will persist even if the EC2 instances are stopped.

## Elastic Network Adapter (ENA)

Many AWS customers create high-performance systems that run across multiple EC2 instances and make good use of all available network bandwidth. To take advantage of the increased concurrency (more vCPUs) found in today’s processors, can make use of ENA that provides up to 20 Gbps of consistent, low-latency performance when used within a Placement Group, at no extra charge.

**ENA will scale as network bandwidth grows and the vCPU count increases**; this will allow you to take advantage of higher bandwidth options in the future **without the need to install newer drivers or to make other changes to your configuration**, as was required by earlier network interfaces.

## Elastic Fabric Adapter (EFA)

Elastic Fabric Adapter (EFA) is a network interface for Amazon EC2 instances that enables customers to run applications requiring high levels of inter-node communications at scale on AWS. Its custom-built operating system (OS) bypass hardware interface enhances the performance of inter-instance communications, which is critical to scaling these applications.

With EFA, High Performance Computing (HPC) applications using the Message Passing Interface (MPI) and Machine Learning (ML) applications using NVIDIA Collective Communications Library (NCCL) can scale to thousands of CPUs or GPUs. As a result, you get the application performance of on-premises HPC clusters with the on-demand elasticity and flexibility of the AWS cloud.

EFA is suitable for applications that require extremely low network latency and high throughout for communication between multiple EC2 instances.

EFA is available as an optional EC2 networking feature that you can enable on any supported EC2 instance at no additional cost.
