## Overlay Network

The overlay network driver creates a distributed network among multiple Docker daemon hosts. This network sits on top of the host-specific networks, allowing containers connected to it to communicate securely when encryption is enabled.

### Prerequisites

Requires the following ports to be opened on both hosts.

```
TCP 2377
TCP 7946
UDP 7946
UDP 4789
```

### Create

```console
$ docker nerwork create --driver=overlay my-overlay
$ docker nerwork create --driver=overlay --attachable my-overlay
```

## Standalone Containers

https://docs.docker.com/network/network-tutorial-overlay/#use-an-overlay-network-for-standalone-containers
