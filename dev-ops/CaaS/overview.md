## Compute as a Service

CaaS refers to the computing hardware needed to run your programs. This simple concept maps into a system that will survive and scale as your organization evolves and grows.

### Automation of Toil

When you want to deploy a new code, you would SFTP the code onto one of the machines, SSH into the machine, compile and run the code. The is a tempting naive solution in its simplicity, but it runs into considerable issues over time and at scale, and automation needs to take over. Nonetheless, the underlying technology (SFTP and SSH) remains.

### Automations

There are simple things that an organization can do to mitigate some of the pain. The process of deploying a binary onto each machine can be easily automated through a shell script.

The monitoring of each machine can also be automated. Instead of manually monitoring for failures, one can use an agent on the machine that detects anomalies, and kills the process if an anomaly is detected. The cloud world equivalent is setting an autohealing policy.

Automated machine assignment is the next step i.e. automated scheduling. There needs to be a central service that knows the complete list of machines available to it and can pick a number of unoccupied machines and automatically deploy binary to them (on demand).

### Containerization and Multi-tenancy

So far, we have implicitly assumed a one-to-one mapping between machines and the programs running on them. This is highly inefficient in terms of computing resource (RAM, CPU) consumption:

- It is very likely to have many more different types of jobs (with different resource requirements) than types of machines, and many jobs will need to use the same machine type
- Machines take a long time to deploy, whereas program resource needs to grow over time
- Old machines will still exist and you need to manage a heterogenous fleet that does not adapt itself to your needs

The natural solution is to specify the resource requirements for each program. This would work well if everybody plays nicely. However, if one program starts consuming more than what it is provisioned with, it might cause neighbouring serving jobs to experience latency blips, or out-of-memory kills by the kernel.

Two programs on the same computer can interact badly as well if they require different versions of shared dependencies. Security is another issue: a program that handles sensitive data needs to be sure other programs on the same machine cannot access it.

Hence, a multi-tenant compute service must provide a degree of isolation, a guarantee of some sort that a process will be able to safely proceed without being disturbed by the other tenants of the machine.

A classical solution to isolation is the use of VMs. However, they come with significant overhead and startup time. For batch jobs that have small resource footprints and short runtimes, this is not an ideal solution. Nonetheless, for organizations that require a diverse set of OS to run (with pre-existing configurations), the choice of using VMs would be better to ease migration costs.

Finally, the solution that engineers at Google have ended up with is containers: a lightweight mechanism based on cgroups and chroot jails, bind mounts and/or union/overlay filesystems for filesystem isolation. **Container is an isolation mechanism that enables multi-tenancy while minimiing the interference between different tasks sharing on a single machine**. Open source container implementations include Docker and LMCTFY (Let Me Container That For You).
