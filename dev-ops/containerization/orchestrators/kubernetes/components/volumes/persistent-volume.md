## Persistent Volume (PV)

Storage resource located in the cluster. Administrators can manually (static) provision PVs or they can be **dynamically provisioned using Storage Classes**. PVs are mapped to external storage assets. However, you cannot map an external storage volume to multiple PVs i.e. cannot have 50GB external storage that has two 25GB PVs.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: foo-pv
spec:
  storageClassName: "" # disables dynamic provisioning, uses static
  claimRef:
    name: foo-pvc
    namespace: foo
  accessModes:
    - ReadWriteOnce
  capacity:
    storage: 10Gi
  hostPath:
    path: "/mnt/data"
  persistentVolumeReclaimPolicy: Retain
```

```bash
$ kubectl get pv
```

### Pre-bind PV to PVC

Use the ClaimRef field referencing a PVC that you will subsequently create.

```yaml
spec:
  claimRef:
    name: foo-pvc # name of PVC
    namespace: foo
```

## Persistent Volume Claim (PVC)

Storage request made by a user. Consumes PV resources rather than Node resources. Kubernetes searches for PVs that correspond to the PVCs' requested capacity and specified properties, so that each PVC can bind to a single PV.

PVCs are like tickets that authorize applications (Pods) to use them i.e. Pods use a PVC to claim access to the PV and start using it.

When there are multiple matches, can use labels and selectors to bind a PVC to a particular PV. This helps guard against a situation where a small PVC binds to a larger PV, as PV and PVCs have one-to-one relationship. **Remaining storage in the bound PVs are inaccessible to other users.**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: foo-pvc
  namespace: foo
spec:
  storageClassName: "" # Empty string must be explicitly set otherwise default StorageClass will be set
  volumeName: foo-pv
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

```bash
$ kubectl get pvc
```

### Pre-bind PVC to PV

Use volumeName field.

```yaml
spec:
  volumeName: foo-pv # name of PV
```

## Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
```
