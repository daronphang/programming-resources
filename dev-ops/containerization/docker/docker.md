## Docker

Docker is a platform to build, ship and run distributed applications – meaning that it runs applications in a distributed fashion across many machines, often with a variety of hardware and OS configurations. For this to be possible, it needs a sandboxing environment capable of abstracting the specifics of the underlying host (for portability), without requiring a complete rewrite of the application (for ubiquity), and without introducing excessive performance overhead (for scale).

Allows users to create independent and isolated environments (called containers) to launch and deploy applications. Not a virtual machine as it only shares resources of host machine in order to run its environments (does not include complete OS). The containers are run in **PID namespaces**.

### Benefits

- Can be built and destroyed faster than VM.
- Multi-platform i.e. can launch containers on any system on Mac, PC, Linux.
- Each environment is isolated.
- Reduces complexity and maintenance as backend, frontend, db, queues are packaged in containers.

### Stack

1. Developer interacts with Docker daemon through Docker CLI tool
2. Docker daemon (dockerd) is a process that runs in the background and talks to the container runtime (containerd)
3. containerd sits above the low-level container runtime (runc) that pulls images, manages networking and storage, and uses runc to run containers
4. runc uses native features of Linux to create and run containers and follows OCI standard

### Global Commands

```console
$ docker --help
$ docker version
$ docker info

$ docker system prune --all                   Delete all images/containers/volumes
$ docker volume prune --force
$ docker container prune --force
$ docker image prune --force

$ watch docker service ls                     Runs command repeatedly

$ docker run -e HTTP_PROXY="http://example.com:80" hello-world
```

### Running Bash in Docker Container

```console
$ docker exec -it <container_name> /bin/bash
```

### Docker Proxy

Need to configure proxy for docker engine and container. For Windows, need to set HTTP_PROXY, HTTPS_PROXY and NO_PROXY in docker engine settings. To propagate proxy settings to containers, need to set using env variables.

```console
$ docker run \
    --env http_proxy="http://my.proxy.com:3128" \
    --env https_proxy="http://my.proxy.com:3128" \
    nginx sh -c "curl google.com"
```

## File Directory

Ensure codes that are going to be used inside containers are placed in /Users.

## GUI

Can use Cmder. Runs PowerShell, CMD Prompt or Bash. Before unzipping, make sure to unblock the folder. To tell Docker how to find server in Cmder:

```
docker-machine env default
```

## Docker on Linux

Easiest OS to use Docker. Install Linux VM on Windows. Can either install with script, store or docker-machine. Can use Ubuntu or CentOS. Need to also install Docker Machine and Docker Compose.

```console
$ curl -sSL https://get.docker.com/ | sh
```
