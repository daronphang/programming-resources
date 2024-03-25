## Volumes

Kubernetes supports many types of volumes i.e. block, file, and object storage. When the storage is exposed on Kubernetes, it is called a volume.

A Pod can use any number of volume types simultaneously. Volumes are defined in the `.spec.containers[*].volumeMounts` field of the Pod template.

```sh
$ kubectl get pv/pvc
```

https://kubernetes.io/docs/concepts/storage/volumes/

### Plugin

The plugin layer is the glue that connects external storage with Kubernetes. Modern plugins are based on the **Container Storage Interface (CSI)** which is an open standard aim at providing a clean storage interface for container orchestrators. The plugin usually runs as a set of Pods in the **kube-system** Namespace.

### Container Storage Interface (CSI)

The CSI is a vital piece of the Kubernetes storage jigsaw and has been instrumental in bringing enterprise-grade storage from traditional vendors to Kubernetes.

CSI is an open-source project that defines a standards-based interface so that storage can be leveraged in a uniform way across multiple container orchestrators.

CSI is the preferred way to write plugins (drivers) and means that plugin code no longer needs to exist in the main Kubernetes code tree. Main interaction with CSI from developer's perspective will be referencing the appropriate CSI plugin in YAML manifest files.

### Acesss modes

Kubernetes support three access modes for volumes:

- **ReadWriteOnce (RWO)**: Defines a PV that can only be bound as R/W by a single PVC, and attempting to bind it from multiple PVCs will fail
- **ReadWriteMany (RWM)**: Defines a PV that can be bound as R/W by multiple PVCs
- **ReadOnlyMany(ROM)**: Defines a PV that can be bound as R/O by multiple PVCs

It is important to note that a **PV can only be opened in one mode** i.e. not possible for a single PV to be bound to a PVC in ROM and another in RWM mode.

### Reclaim policy

A volume's reclaim policy tells Kubernetes how to deal with a PV when its PVC is released. Two policies are Delete and Retain.

Delete is the default for PVs created dynamically via SCs unless specified otherwise. It deletes the PV and associated storage resource on the external storage system when the PVC is released.

Retain will keep the associated PV object on the cluster as well as any data stored on the associated external asset. However, other PVCs are prevented from using it in the future. A disadvantage is that it requires manual clean-up.

### Volume Binding Mode

There are two types of volume binding mode: Immediate and WaitForFirstConsumer.

Setting it to 'Immediate' will create the volume on the external storage system as soon as the PVC is created. If you have multiple datacenters or cloud regions, the volume might be created in a different region than the Pod that eventually consumes it.

Setting it to 'WaitForFirstConsumer' will delay creation until a Pod using the PVC is created. This ensures that the volume will be created in the same datacenter or region as the Pod.

### emptyDir

For a Pod that defines an emptyDir volume, the volume is created when the Pod is assigned to a node. All containers in the Pod can read and write the same files in the emptyDir volume, though it can be mounted at the same or different paths in each container. When a Pod is removed, the **data in emptyDir is deleted permanently**.

## Example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod
spec:
  containers:
    - name: test
      image: busybox:1.28
      command: ["sh", "-c", 'echo "The app is running!" && tail -f /dev/null']
      volumeMounts:
        - name: config-vol
          mountPath: /etc/config
        - name: empty-vol
          mountPath: /etc/empty
  volumes:
    - name: config-vol
      configMap:
        name: log-config
        items:
          - key: log_level
            path: log_level
    - name: test-volume
      hostPath:
        # directory location on host
        path: /data
        # this field is optional
        type: Directory
    - name: empty-vol
      emptyDir: {}
```
