## Containerization

Containerization is a software deployment process that bundles an application’s code with all the files and libraries it needs to run on any infrastructure.

Traditionally, to run any application on your computer, you had to install the version that matched your machine’s operating system. For example, you needed to install the Windows version of a software package on a Windows machine.

With containerization, you can create a single software package, or container, that runs on all types of devices and operating systems.

### How it works

Containerization involves building self-sufficient software packages that perform consistently, regardless of the machines they run on. Software developers create and deploy container images—that is, files that contain the necessary information to run a containerized application.

Developers use containerization tools to build container images based on the Open Container Initiative (OCI) image specification. OCI is an open-source group that provides a standardized format for creating container images. Container images are read-only and cannot be altered by the computer system.

## Images

Container images are the top layer in a containerized system that consists of four layers.

### Infrastructure

Infrastructure is the hardware layer of the container model. It refers to the physical computer or bare-metal server that runs the containerized application.

### OS

The second layer of the containerization architecture is the operating system. Linux is a popular operating system for containerization with on-premise computers. In cloud computing, developers use cloud services such as AWS EC2 to run containerized applications.

### Container engine

The container engine, or container runtime, is a software program that creates containers based on the container images. It acts as an intermediary agent between the containers and the operating system, providing and managing resources that the application needs. For example, container engines can manage multiple containers on the same operating system by keeping them independent of the underlying infrastructure and each other.

### Application and dependencies

The topmost layer of the containerization architecture is the application code and the other files it needs to run, such as library dependencies and related configuration files. This layer might also contain a light guest operating system that gets installed over the host operating system.

## Containers

Containers share an OS kernel with the host.

## VM

A virtual machine (VM) is a digital copy of the host machine's physical hardware and operating system. A host machine might have several VMs sharing its CPU, storage, and memory. A hypervisor, which is software that monitors VMs, allocates computing resources to all the VMs regardless of whether the applications use them.

## Containerization vs VM

Containerization is a similar but improved concept of a VM. Instead of copying the hardware layer, containerization removes the operating system layer from the self-contained environment. This allows the application to run independently from the host operating system. Containerization prevents resource waste because applications are provided with the exact resources they need.
