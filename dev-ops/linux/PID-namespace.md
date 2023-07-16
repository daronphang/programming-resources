## PIDs

When a process is created on Unix OS, it is given a specific numeric identifier called a PID. This PID helps to identify a process uniquely even if there are two processes that share the same human-readable name. For instance, if there are multiple SSH sessions active on a system and you need to close a specific connection, PID provides a way for the administrator to ensure the correct session is closed.

All of these processes are tracked in a special file system called **procfs**. While this file system can technically be mounted anywhere, most tooling expect the procfs to be mounted under /proc.

https://www.redhat.com/sysadmin/pid-namespace

## PID Namepsace

One of the main reasons for the PID namespace is to allow for process isolation. PID namespaces isolate the PID number space, meaning that processes in different PID namespaces can have the same PID.

PID namespaces allow containers to provide functionality such as suspending/resuming the set of processes in the container and migrating the container to a new host while the processes inside the container maintain the same PIDs.

This is important as it means that processes can be guaranteed not to have a conflicting PID with any other process. When considering a single system, there is no chance of PIDs conflicting as the system continuously increments the PID number and never assigns the same number twice. However, when dealing with containers across multiple machines, this issue becomes more salient.
