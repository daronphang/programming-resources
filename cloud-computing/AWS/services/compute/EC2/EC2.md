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

## Instance families

### General Purpose

Provides a balance of compute, memory and networking resources. You can use them for application servers, gaming servers, backend servers for enterprise applications, and small/medium databases.

### Compute optimized

Ideal for compute-bound applications that benefit from high-performance processors including high performance web servers, compute-intensive applications, and dedicated gaming servers. You can also use them for batch processing workloads.

### Memory optimized

Designed to deliver fast performance for workloads that process large datasets in memory. Can be useful for situations where you have a workload that requires large amounts of data to be preloaded before running an application.

### Accelerated computing

Instances that use hardware accelerators (coprocessors) to perform functions more efficiently than is possible in software running on CPUs. Examples include machine learning, computational fluid dynamics, autonomous vehicles, floating-point number calculations, graphics processing, game streaming, application streaming, and data pattern matching.

### Storage optimized

Designed for workloads that require high, sequential read and write access to large datasets on local storage. Example of workloads include distributed file systems, data warehousing applications, and high frequency OLTP (online transaction processing) systems.

In computing IOPS (input/output operations per second) is a metric that measures the performance of a storage device. Storage optimized instances are designed to deliver tens of thousands of low-latency, random IOPS to applications.

### HPC optimized (High Performance Computing)

HPC instances are purpose built to offer the best price performance for running HPC workloads at scale on AWS. Ideal for applications that benefit from high-performance processors, such as large, complex simulations and deep learning workloads.

## Amazon Machine Image (AMI)

When launching an EC2 instance, the first setting you configure is which OS you want by selecting an AMI.

In the traditional infrastructure world, spinning up a server consists of installing an OS from installation disks, drives, or wizards over the network. In AWS, the OS installation is built into the AMI.

An AMI includes the OS, storage mapping, architecture type, launch permissions, and any additional preinstalled software applications.

There are multiple ways to select an AMI:

- AWS Marketplace
- Personal AMIs
- Community
- Custom image

Each AMI in the AWS Management Console has an AMI ID, which is prefixed by `ami-`.

### AMI and EC2 instances

The AMI is how you model and define your instance i.e. AMI is the class, EC2 is the instance.

One advantage of using AMIs is that they are reusuable. If you can spin up another EC2 instance with the same configuration, you can simply create an AMI from your running instance and use it to start a new instance.

## EC2 Image Builder

EC2 Image Builder is used to automate the creation, maintenance, validation and testing of VMs or container images:

1. Creates an EC2 instance
2. Builds components and customize software on instance
3. Creates an AMI
4. Runs a test suite on AMI (working, secure, etc.)
5. Distributes AMI to multiple Regions

It is a **free** service and only pay for the underlying resources i.e. EC2, AMI storage, etc. It can be run on a schedule.

## EC2 User Data

It is possible to bootstrap our instances using an EC2 User Data script (runs with root user). Bootstrapping means launching commands when a machine starts.

The script is run once at the instance first start and is used to automate boot tasks including:

- Installing updates
- Installing software
- Downloading common files from the internet

```bash
#!bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
```

## Connecting to EC2

Can either use SSH (port 20), Putty or EC2 Instance Connect (uses temporary SSH keys).
