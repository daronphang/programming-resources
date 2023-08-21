## Volumes

Kubernetes supports many types of volumes. A Pod can use any number of volume types simultaneously Volumes are defined in the .spec.containers[*].volumeMounts field of the Pod template.

```bash
$ kubectl get pv/pvc
```

https://kubernetes.io/docs/concepts/storage/volumes/

## Types

### PersistentVolume (PV)

Storage resource located in the cluster. Administrators can manually provision PVs.

### PersistentVolumeClaim (PVC)

Storage request made by a user. Consumes PV resources rather than Node resources. Kubernetes searches for PVs that correspond to the PVCs' requested capacity and specified properties, so that each PVC can bind to a single PV.

When there are multiple matches, can use labels and selectors to bind a PVC to a particular PV. This helps guard against a situation where a small PVC binds to a larger PV, as PV and PVCs have one-to-one relationship. **Remaining storage in the bound PVs are inaccessible to other users.**

### Ephemeral

Do not store data persistent across restarts and bound to the Pod's lifetime.

### EmptyDir

Created when Kubernetes assigns a Pod to a Node. Lifespan is tied to a Pod's lifecycle existing on that specific Node.
