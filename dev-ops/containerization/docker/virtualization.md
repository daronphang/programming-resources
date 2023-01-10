## Virtualization

Before the introduction of virtualization, users had to dual boot Windows and Linux if they wanted to run both OS on the same computer. VMs gave more flexibility, and now we can run Linux using WSL.

## Hyper-V vs WSL

One of Docker's goals is to provide an experience of working with containers as natively close as possible from a Desktop environment on Windows, Mac or Linux.

The original WSL was an impressive effort to emulate a Linux kernel on top of Windows, but there are foundational differences that made certain things impossible to implement as with native Linux, including Kubernetes inside WSL. The alternate solution developed was using Hyper-V VMs and LinuxKit to achieve the seamless integration.

Hyper-V is a VM application that runs as a complete machine, and uses a hypervisor like VirtualBox.

## WSL2

Microsoft announced a major architecture change that instead of using emulation, they are actually providing a real Linux kernel running inside a lightweight VM that is tightly integrated with the host. Docker daemon runs well on it with great performance.

https://www.docker.com/blog/docker-hearts-wsl-2/

### Hyper-V

WSL2 uses Hyper-V features to create a lightweight VM with a minimal Linux kernel. To support WSL2, Hyper-V has been split up in Windows:

- **Hypervisor (Virtual Machine Platform)**: available on all Windows versions and is the minimum required to run WSL.
- **Hyper-V Manager**: Distinct Windows feature that is used for running full-featured VMs whose integration with the host is limited.

### Linux Workspaces

When using Docker Desktop today, the VM running the daemon is completely opaque i.e. you can interact with the Docker and Kubernetes API from Windows, but can't run anything within the VM except Docker containers or Kubernetes Pods.

With WSL2 integration, Linux programs running inside WSL can do the same i.e. not need to maintain both Linux and Windows build scripts. This is a huge impact for developers working on projects targeting a Linux environment. Devleopers can work on the Linux Docker daemon on Windowss, using the same set of tools and scripts as a developer on a Linux machine.

Bind mounts from WSL will support inotify events have nearly identical I/O performance as on a native Linux machine.

### Performance

With WSL2, the VM is setup to use dynamic memory allocation, and can schedule work on all the host's CPUs, while consuming as little memory it requires (uses part of Window's Hyper-V). Hence, overhead for WSL2 is much lower than running a full VM, and is useful for CPU/memory intensive tasks.

### Bind Mounts (File Systems)

In an enterprise environment, the reliability of Windows file bind mounts is limited: relies on Samba Windows service which may be deactivated/blocked by GPOs, firewalls, etc.

No configuration is needed for WSL2 relating to bind mounts on Windows.
