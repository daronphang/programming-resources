## Storage Classes (SC)

SCs lets you dynamically create physical back-end storage resources that get automatically mapped to PVs on Kubernetes i.e. helps to automate the provisioning of PVs. You define SCs in YAML files that reference a plugin and tie them to a particular tier of storage on a particular storage back-end i.e. AWS SSD storage in the AWS EU Region.

When SCs are deployed, the SC watches the API server for new PVC objects referencing its name. When matching PVCs appear, the SC dynamically creates the required asset on the back-end storage system and maps it to a PV on Kubernetes. Apps can then claim it with a PVC.

Key components:

- SCs are immutable after they are deployed
- Parameters block is for **plugin-specific values**, and each plugin is free to support its own set of values

You can configure as many SCs as you need; however, each class can only relate to a single type of storage on a single back-end.

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
    name: fast-local
provisioner: ebs.csi.aws.com # tells k8s which plugin to use
parameters: # lets you finely tune storage attributes
    type: io1
    iopsPerGB: "10"
    encrypted: true
allowedTopologies: # list where replicas should go
- matchLabelExpressions:
    - key: topology.ebs.csi.aws.com/zone
    values:
    - eu-west-1a
```

### Workflow

1. Have a storage back-end (cloud or on-premise)
2. Create your Kubernetes cluster
3. Install and configure the CSI storage plugin
4. Create one or more SCs on K8s
5. Deploy Pods and PVCs that references those SCs

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: fast
provisioner: pd.csi.storage.gke.io
parameters:
  type: pd-ssd
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mypvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: fast
---
apiVersion: v1
kind: Pod
metadata:
    name: mypod
spec:
    volumes:
        - name: data
        persistentVolumeClaim:
            claimName: mypvc
containers:
    # ...
```
