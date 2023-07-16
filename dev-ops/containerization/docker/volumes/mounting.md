## Declaring Volume from Dockerfile

Statement declares that a specific path of the container must be mounted to a Docker volume. When the container is run, Docker will create an anonymous volume (with unique id) and mount it to the specified path.

```dockerfile
FROM nginx:latest

RUN echo "<h1>Hello from Volume</h1>" > /usr/share/nginx/html/index.html
VOLUME /usr/share/nginx/html
```

## Mounting Volume to Container

```
type                "volume" to indicate a volume mount
src                 name of volume or source directory
dst                 destionation mount point in the container
volume-driver
readonly            rw for read/write
```

```bash
$ docker run --mount source=[volume_name],destination=[path_in_container] [docker_image]

$ docker run -it --name=example --mount source=demo-volume,destination=/data ubuntu

$ docker run --mount \
  'type=volume,src=data-volume,\
  dst=/var/opt/project,volume-driver=local,\
  readonly' \
  bash -c "ls /var/opt/project"
```

## Using Docker Compose

Multiple services can share the same volume; a named volumed MUST be declared in the top-level volumes key.

```yaml
version: "3.2"
services:
  web:
    image: nginx:latest
    ports:
      - 8080:80
    volumes:
      # mount ./target from host to /usr/share/nginx/html of the container (mount point)
      - ./target:/usr/share/nginx/html
  web1:
    image: nginx:latest
    ports:
      - 8081:80
    volumes:
      - html_files:/usr/share/nginx/html
  web2:
    image: nginx:latest
    volumes:
      - type: bind
        source: $HOST/location
        target: /container/location
      - type: volume
        source: html_files
        target: /container/location
volumes:
  html_files:
  # implicit volume creation by Docker
```

## Mounting Network Drives

### Using Docker Volumes

Recommended approach is to use volumes (pointing to your CIFS shares) and mapping them into a folder inside the container, which the containerized app can then use to view/modify the contents.

```bash
nslookup server_name
```

#### Creating Volume

The addr option is required if using a hostname instead of an IP so Docker can perform the hostname lookup.

```bash
$ docker volume create \
--driver local \
--opt type=cifs \
--opt device=//uxxxxx.your-server.de/backup \
--opt o=addr=uxxxxx.your-server.de,username=uxxxxxxx,password=*****,file_mode=0777,dir_mode=0777 \
--name cif-volume

$ docker volume create \
--driver local \
--opt type=cifs \
--opt o=username=rdr_fab10_rda,password=password,vers=3.0,rw \
--opt device=//10.193.11.11/F10N_PY28_autostaging \
--name rda-f10n-dir

$ docker volume create --driver local --opt type=cifs --opt device=//fsf10peeuipathfs/F10_PEE_UIPATH/daronphang --opt o=user=daronphang,password=123 mydockervolume
```

#### Docker Compose

```yaml
volumes:
  foldermix:
    driver_opts:
      type: cifs
      o: username=daronphang,password=123,vers=3.0,rw
      device: //ip-address/some/folder # for Windows: \\ip-address\some\folder
```

### Using Host Mounted Volume

If using this approach, make sure to specify user in docker compose so that the container has permissions for RW access.

```bash
$ sudo mount -t cifs -o username=daronphang,password=password //10.195.111.11/F10_PEE_UIPATH/daronphang /mnt/uipath
```

```yaml
services:
  email_service:
    container_name: df_email_service
    user: "${UID}:${GID}" # specify UID and GID in .env file in same directory as compose file
    volumes:
      - /mnt/uipath:/uipath
```
