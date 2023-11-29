## Elevation of privilege

Privilege esclation is gaining higher access than what is granted, in order to cause damage or gain unauthorized access.

### Protecting API server

Kubernetes offers several authorization modes that help safeguard access to the API server. All requests to the API server must be authenticated and authorized. These include:

- Role-based Access Control (RBAC)
- Webhook (offload authorization to an external REST-based policy engine)
- Node (authorizing API requests made by kubelets, different from users)

### Protecting Pods

#### Do not run processes as root

You can configure which user to run as at Pod or container level. User namespaces is a Linux kernel technology that allows a process to run as root within a container, but run as a different user outside of the container.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo
spec:
  securityContext: # Applies to all containers in this Pod
    runAsUser: 1000 # Non-root user
  containers:
    - name: demo
      image: example.io/simple:1.0
      securityContext:
        runAsUser: 2000 # overrides the Pod setting at container level
```

#### Dropping capabilities

Though most processes don't need to run as root inside the container, many processes do require more privileges than a typical non-root user. One way to grant the exact set of privileges is **capabilities**.

The power of the root user comes from the combination of capabilities:

- SYS_TIME: Allows a user to set the system clock
- NET_ADMIN: Allows a user to perform network-related operations

Having a modular set of capabilities allows you to be extremely modular when granting permissions. There are over 30 capabilities, and choosing the right ones can be daunting.

For Docker runtimes, it drops over half of them by default. However, this may not be suitable for production environments.

A common way to find the absolute minimum set of capabilities an application requires (least-privilege model), is to run it in a test environment with all capabilities dropped. This will cause the application to fail and log messages about missing permissions. You then add them to the application's Pod spec, and rerun the application until it can run properly.

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: capability-test
spec:
    containers:
    - name: demo
      image: example.io/simple:1.0
       securityContext:
        capabilities:
            add: ["NET_ADMIN", "CHOWN"]
```

#### Filtering syscalls via seccomp

seccomp (secure computing) is a concept similar to capabilities, but works by filtering syscalls rather than capabilities.

The way a Linux process asks the kernel to perform an operation is by issuing a syscall. seccomp lets you control which syscalls a particular container can make to the host kernel.

seccomp profiles include:

- Non-blocking: Allows a Pod to run and record every syscall it makes to an audit log that you can use to create a custom profile
- Blocking: Blocks all syscalls
- Runtime Default: Forces a Pod to use the seccomp profile defined by its container runtime (balance of usable and secure)
- Custom: A profile that only allows the syscalls your application needs in order to run

#### Preventing privilege escalation by containers

By default, Linux allows a child process to claim more privileges than its parent. This is a bad idea, as you will often want a child process to have the same or less privileges than its parent. Fortunately, this can be prevented in Kubernetes.

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: capability-test
spec:
    containers:
    - name: demo
      image: example.io/simple:1.0
       securityContext:
        allowPrivilegeEscalation: false
```
