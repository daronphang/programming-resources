## Background

Most business applications comprise of two main parts: Application and Configuration. When both of them are decoupled, the benefits include:

- Re-usuable application images
- Simpler development and testing (dev, test, prod environments)
- Simpler and fewer disruptive changes

### Tight coupling between application and configuration

There are several drawbacks to the approach of storing the application and its configuration as a single artifact:

- Each environment (dev, test, prod) will need its own image as they have different security credentials
- You need to store all images in distinct repositories, and need be careful about permissions to those repositories
- Changing configuration of an app requires rebuilding and packaging into a new image
- Harder to troubleshoot an issue if you push an update that includes both an application binary update as well as a configuration update

## ConfigMap (CM)

Kubernetes provide an object called CM that lets you store configuration data outside of a Pod. It also lets you dynamically inject the config into a Pod at runtime.

CMs are first-class objects in the Kubernetes API under the core API group which tells us:

- CMs are stable (v1)
- You can operate on them with the usual kubectl commands
- They can be defined via YAML manifests

CMs are used to store non-sensitive configuration including:

- Environment variables
- Configuration files
- Hostnames
- Service ports
- Account names

CMs are a map of key/value pairs called an entry.

### Native apps

Kubernetes-native apps can access ConfigMap data directly via the API without needing things like environment variables and volumes. This can simplify application configuration, but the application will only run on Kubernetes. However, this situation is rare.

### Example

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: test-conf
data:
  # key/value pairs
  given: "Nigel"
  family: "Poulton"
  # pipe treats following as a single literal value i.e. full config file
  test.conf: |
    env = plex-test
    endpoint = 0.0.0.0:31001
    char = utf8
    vault = PLEX/test
    log-size = 512M
```

### Commands

```bash
$ kubectl get cm
$ kubectl describe cm testmap
```

## Injecting ConfigMap data into Pods

There are three main ways to inject ConfigMap data:

- As environment variables
- As arguments to container startup commands
- As files in a volume

### Environment variables

A drawback to using this method is that environment variables are **static**. This means updates made to the ConfigMap are not reflected in running containers.

Use envFrom to define all of the ConfigMap's data as container environment variables.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod
spec:
  containers:
    - name: ctr1
      env:
        - name: FIRSTNAME
          valueFrom:
            configMapKeyRef:
              name: multimap
              key: given
        - name: LASTNAME
          valueFrom:
            configMapKeyRef:
              name: multimap
              key: family

      # alternative, to inherit all env variables
      envFrom:
        - configMapRef:
            name: multimap
        - secretRef:
            name: secret
```

```yaml
# using configmap env variables in Pod commands
# $(VAR_NAME) syntax
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod
spec:
  containers:
    - name: test-container
      image: registry.k8s.io/busybox
      command: ["/bin/echo", "$(SPECIAL_LEVEL_KEY) $(SPECIAL_TYPE_KEY)"]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:
            configMapKeyRef:
              name: special-config
              key: SPECIAL_LEVEL
        - name: SPECIAL_TYPE_KEY
          valueFrom:
            configMapKeyRef:
              name: special-config
              key: SPECIAL_TYPE
  restartPolicy: Never
```

### Volumes

Using ConfigMaps with volumes is the most flexible option. You can reference entire configuration files, as well as make updates and have them reflected in running containers. This means you can make changes to entries in a ConfigMap, after you have deployed a a container, and those changes will be reflected for running apps.

Each property name in this ConfigMap becomes a new file in the mounted directory after you mount it. Use `cat` to look at the contents of each file and you’ll see the values from the ConfigMap. A ConfigMap is always mounted as **readOnly**.

The high-level process for exposing ConfigMap data via a volume is as follows:

1. Create the ConfigMap
2. Create a ConfigMap volume in the Pod template
3. Mount the ConfigMap volume into the container
4. Entries in the ConfigMap will appear in the container as individual files
5. For updates, run 'kubectl apply' to repost to the API sserver

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: cmvol
spec:
    volumes:
        - name: volmap
          configMap:
            name: multimap  # creates a ConfigMap volume
            items:
              # all contents stored in multimap.data.hello
              # are mounted into the Pod in path /etc/name/world
              - key: hello
                path: world
    containers:
        - name: ctr
        image: nginx
        volumeMounts:
            - name: volmap
            mountPath: /etc/name
```

## Examples

### Running shell script

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-script-configmap
data:
  my-script.sh: |
    #!/bin/bash
    echo "Hello, World!"
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: my-container
      image: alpine
      volumeMounts:
        - name: my-script-volume
          mountPath: /script
      command: ["/script/my-script.sh"]
  volumes:
    - name: my-script-volume
      configMap:
        name: my-script-configmap
        defaultMode: 0744
```
