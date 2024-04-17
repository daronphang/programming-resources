## Networking

Docker containers and services can be connected with each other, or to non-Docker workloads. They can be managed in platform-agnostic way i.e. doesn't matter if Docker hosts run Linux, Windows or mix.

By default, when a container is created and run, it does not publish any of its ports to the outside world. To make a port available to services outside of Docker or to Docker containers, need to use --publish flag. This creates a firewall rule which maps a container port to a port on the Docker host to the outside world.

Each container is connected to a private virtual network called the 'bridge' (default network driver). Each virtual network routes through NAT firewall on host IP. All containers on a virtual network can talk to each other without -p. Each app with frontend/backend should sit on the same network. Can attach containers to more than one virtual network.

```
bridge              Communication between containers running on same Docker host
overlay             Communication between containers running on different Docker hosts
```

```sh
$ docker container run -p 8080:80   # map TCP port 80 in container to port 8080 of host machine
$ docker network ls
```

### IP Address and Hostname

By default, the container is assigned an IP address for every Docker network it connects to. When the container starts, it can only be connected to a single network using --network. However, you can connect a running container to multiple networks.

```sh
$ docker container run --network --ip   # ip to specify the IP address

$ docker network connect --ip   # to connect a running container to other networks
```

### DNS

Static IP's for talking to containers is an anti-pattern and avoid it as this requires updating the application configuration frequently and makes the app fragile. Instead, use DNS naming (host name). Docker daemon has built-in DNS server that containers use by default.

https://www.joyent.com/blog/container-native-discovery

### Accessing Containers within Docker Compose Network

**When one container calls another directly**, use the Compose service name and the default port.

**When the browser application calls a container**, use the host's DNS name (localhost if local) and the container's port. For instance, when running a dockerized React/Angular, it is running in the user's browser which is outside of Docker's space and hence, doesn't has access to Docker's internal networking.
