## Relocating Docker

Docker stores files in /var/lib/docker by default. However, if the file space is insufficient, must relocate the directory.

1. Create daemon.json in /etc/docker.

```json
{
  "data-root": "/path/to/new/docker"
}
```

2. Stop Docker and copy contents.

```console
$ sudo systemctl stop docker
$ sudo systemctl stop docker.socket
$ sudo systemctl stop containerd

$ sudo mkdir -p path/to/new/docker
$ sudo mv /var/lib/docker path/to/new/docker

$ sudo systemctl start docker
$ sudo dockerd --debug

$ docker info -f '{{ .DockerRootDir}}'
```
