## Does Kubernetes use Docker?

Kubernetes was previously bound to a specific container (Docker, containerd, CRI-O, etc.) runtime which spawned a lot of maintenance overhead for the upstream Kubernetes community. Moreover, vendors building solutions on top of the Kubernetes experienced the same overhead. This necessitated the development of CRI to make Kubernetes container runtime-agnostic by decoupling it from various runtimes. The CRI API allows different container runtimes to be plugged into it.

https://kubernetes.io/blog/2020/12/02/dont-panic-kubernetes-and-docker/

### dockershim

Inside of Kubernetes cluster, container runtime is responsible for pulling and running your container images. Docker is a popular choice for that runtime, but Docker was not designed to be embedded inside Kubernetes.

Docker runtime refers to the entire tech stack, and one part of it is called containerd, a high-level container runtime by itself. It also consists of UX enhancements which are not neccessary for Kubernetes as it is not meant to be interacted by humans.

Docker Engine is not compliant with CRI, and to bridge the gap, the Kubernetes project included a component called dockershim, which allowed Kubernetes to run containers with the Docker runtime.

### dockershim Deprecation

As of Kubernetes 1.24, the dockershim component was removed completely, and you need to choose a container runtime that implements CRI. The logical successor to Docker Engine in Kubernetes clusters is **containerd**.

Nonetheless, the images built from running <mark style="background-color: #D8D6D6">docker build</mark> can still run in your kubernetes cluster.
