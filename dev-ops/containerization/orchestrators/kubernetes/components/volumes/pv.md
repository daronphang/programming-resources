## Persistent Volume (PV)

A PV is an abstraction representing storage available to the cluster, i.e. cluster-level storage resource exposed to Kubernetes. It represents storage that could come from many backends, including NFS, Ceph, LVMs, local disks, etc. PVs point to storage, but they do not create or manage the underlying storage system.

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

```sh
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

```sh
$ kubectl get pvc
```

### Pre-bind PVC to PV

You can use volumeName field. The binding happens regardless of some volume matching criteria, including node affinity. The control plane still checks that **storage class, access modes, and requested storage size are valid**.

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

## LVM (Logical Volume Manager)

LVM is a Linux storage construct created from physical disks. It allows you to pool multiple physical disks into a Volume Group (VG) and carve them into LVs, allowing you to:

- Resize disks
- Combine multiple disks
- Snapshot volumes
- Move data between disks

```
Physical Disk
 → Volume Group
   → Logical Volume
     → Filesystem
```

```
Pod
 ↓
PVC
 ↓
PV
 ↓
Actual storage (EBS / NFS / LVM / etc.)
```

## Ceph (distributed storage system)

Ceph is an open-source storage platform that provides a highly scalable and reliable solution for object, block, and file storage in a unified system. Some of the benefits it offers include fault tolerance, high availability, and scalability without a single point of failure. It automatically manages data replication and recovery. With Ceph, users can self-manage their storage data, minimizing administration time and other costs. Ceph storage is versatile, fitting various use cases due to its scalable and resilient nature.
Key features include:

- Scalability: Seamlessly scale out by adding more storage nodes to the cluster without disrupting service.
- High availability: Built-in redundancy and self-healing capabilities to ensure data availability and integrity
- Unified storage: Support for object, block and file storage in one platform, simplifying infrastructure and management

Ceph is ideal for large-scale deployments that require high-availability, fault tolerance, and scalability, such as data-intensive applications.
