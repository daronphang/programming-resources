## Images

Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, metadata and settings. Container images become containers at runtime. Not a complete OS i.e. no kernel, drivers, etc. For containers using the same image, they are stacked ontop of same image i.e. **image is only stored once on host**.

```shell
$ docker pull nginx # Download latest version
$ docker pull nginx1.11

$ docker images -a # List images
$ docker image rm <image_name> # Delete a specific image
$ docker rmi $(docker images -a -q) # Delete all images, need run inside Windows powershell
$ docker rmi $(docker images -q)
$ docker images -f dangling=true # Filters images that have no relationship with tagged images
$ docker images -a |  grep "pattern"

$ docker image prune -a # Removes all unused images, not just dangling ones
```

### Building

Docker build is run by Docker daemon and not CLI. Order is critical. Keep things that do not change at top. Can add .dockerignore file. Need to disable builtkit if have error. Don't need virtualenv as Docker achieves the same isolation.

Need to check which image is used to built from.

```
alpine            Uses apk add
Ubuntu/Debian     Uses apt-get
```

```shell
$ docker build .                    # Builds an image from a dockerfile and context
$ docker build -f path/to/file
$ docker build -t test-image:1.1    # Specify repo (test-image) and tag (1.1)
$ docker build -t test-image:1.1 -t test-image:latest   # multiple tags

$ docker images

$ docker build --build-arg http_proxy=http://10.239.4.80:913 --build-arg https_proxy=http://10.239.4.80:913 .
```

### Pushing Images to DockerHub

```shell
$ rm ~/.docker/config.json # if encounter storing credentials error
$ docker login -u username
$ docker push username/image_tag_name
```

### Parser Directives

Must be at top of dockerfile. Affects the way in which subsequent lines are handled and do not add layers to build. Can only be used once. supports syntax and escape.

```
Escape: \ or `
#directive=value1
FROM imageName
```

## Errors

### Failed to create LLB definition: failed to authorize: rpc error: code = Unknown desc = failed to fetch anonymous token

```
# linux
$ export DOCKER_BUILDKIT=0
$ export COMPOSE_DOCKER_CLI_BUILD=0

# windows
"buildkit": false         Found in docker engine settings
```

## Execution

### Shell (If need to run shell)

```dockerfile
# <instruction> <command>
# automatically calls /bin/sh -c <command>
RUN apt-get install python3
CMD echo "Hello world"
ENTRYPOINT echo "Hello world"
```

### Exec

```dockerfile
# <instruction> ["executable", "param1", "param2", ...]
RUN ["apt-get", "install", "python3"]
CMD ["/bin/echo", "Hello world"]
ENTRYPOINT ["/bin/echo", "Hello world"]
```

https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c

## Best Practices

- WORKDIR should always use absolute paths.
- Use ARG for build-time customization as ENV will persist when a container starts running.
- COPY is preferred over ADD as it is more transparent.
- Don't install unnecessary packages.
- For Windows, don't use backslash in WORKDIR, and not allowed in COPY.
- Use explicit Docker base image tags (default is :latest) as they are inconsistent and exposed to vulnerabilities.
- Containers run with root privileges by default (unrestricted management); however, exposes to high risk when running in production env as anyone who has access to container can inject malicious code or change user; always run containers as non-root.
- To increase Docker build performance, add dockerignore file.

### Use multi-stage builds for more secure Docker images

Multi-stage builds (using two or more FROM) let you split up your Dockerfile into multiple distinct stages. Each stage completes a step in the build process, and you can bridge the different stages to create your final image in the end. **Only the instructions in the last stage will end up as layers in the final image**.

Use multi-stage build to copy only necessary production artifacts. A lot of build-time dependencies and files are not needed for running the application. Multi-stage builds are an easy way to get rid of overweight and security threats.

```dockerfile
FROM node:14.4.0 AS build
COPY . .
RUN npm install && npm run build

# Use smaller image
FROM node.slim-14.4.0
COPY --from=build /home/node/app/dist /home/node/app/package.json /home/node/app/package-lock.json ./
RUN npm install --production

CMD ["node", "dist/app.js"]
```

### Plan for efficient caching

Ordering your Dockerfile instructions appropriately helps you avoid unnecessary work at build time.

Docker images consist of layers. When we build an image, any instruction that modifies the file system creates a new layer (RUN, COPY, ADD, WORKDIR, LABEL, CMD, ENTRYPOINT). If none of the files have changed, the image layers will just be read from the cache. Otherwise, if a layer has changed since the last build, **all layers that follow must be rebuilt**.

As dependencies change less often than code, it should be placed at the top of your Dockerfile and the ones constantly changing should be at the bottom.

```dockerfile
COPY package.json package-lock.json ./
RUN npm ci
COPY ./app ./app
```

### Bootstrap using node command, avoid npm start

Avoid using npm scripts as they do not pass OS signals to the code. This prevents problems with child-process, signal handling, graceful shutdown and having processes.

When no signals are passed, your code will never be notified about shutdowns. Without this, it will lose its chance to close properly, possibly losing requests and data.

```dockerfile
FROM node:21-alpine AS build

WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm ci --production && npm clean cache --force
CMD ["node", "server.js"]
```
