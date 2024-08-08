## Compute Options

To setup servers, you can either run as VMs, container services, or serverless.

## VMs

A VM emulates a physical server and allows you to install an HTTP server to run your applications. To run VMs, you install a **hypervisor** on a host machine.

### Hypervisor (Virtual Machine Monitor)

A hypervisor is a software or firmware that makes it possible to share physical hardware resources (memory, processing) across one or more virtual machines. The hypervisor provisions the resources to create and run your VMs by isolating the hypervisor OS and resources from the virtual machines.

The physical hardware, when used as a hypervisor, is called the host, while the many VMs that use its resources are guests.

All hypervisors need some operating system-level components to run VMs i.e. memory manager, process scheduler, I/O stack, device drivers, security manager, network stack, etc.

The hypervisor gives each VM the resources that have been allocated and manages the scheduling of VM resources against the physical resources. The physical hardware still does the execution.

Many different OS can run alongside each other and share the same virtualized hardware resources with a hypervisor. without virtualization, you can only run one OS on the hardware.

There are many choices for hypervsiors from traditional vendors and open-source i.e. VMware, Kernel-based Virtual Machine (KVM), Microsoft Hyper-V.

## Containers vs Hypervisor

| Container                                                                                                                                                                                 | Hypervisor                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Allow applications to run independently of an OS<br><br>Can run on any OS (requires container engine to run)<br><br>Lightweight and portable (application has everything it needs to run) | Allow an OS to run independently from the underlying hardware through the use of VMs<br><br>Share virtual computing, storage and memory resources<br><br>Can run multiple OS on top of one server (bare-metal hypervisor) |
