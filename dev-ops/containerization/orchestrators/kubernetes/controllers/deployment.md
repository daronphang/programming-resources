## Deployment

To deploy containerized applications on top of a running cluster, need to create a Kubernetes Deployment configuration. The Deployment instructs Kubernetes how to create and update instances of your application, and keep them running across Nodes in the event of failure. Resides within the Control Plane. Deployments are the recommended way to manage the creation and scaling of Pods as it offers scalability, self-healing, and rolling updates for stateless apps.

When creating a Deployment, need to specify the container image and number of replicas you want to run. Once a deployment is created, the control plane schedules the application instances included in the Deployment to run on individual Nodes in the cluster.

Once the application instances are created, the Deployment Controller continuously monitors those instances. If a node goes down, the controller replaces the instance with an instance on another Node i.e. **provides self-healing mechanism to address machine failure or maintenance**.

### Objects

#### volumes

A volume represents a directory with data that is accessible across multiple containers in a Pod.

#### volumeMounts

A volumeMount entails mounting of the declared volume into a container in the same Pod. The "name" property specifies which volume is to be mounted.

Volume and volumeMounts go hand in hand i.e. cannot create a volume without mounting it and vice versa.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: redis
spec:
  containers:
    - name: redis
      image: redis
      volumeMounts:
        - name: redis-storage
          mountPath: /data/redis
  volumes:
    - name: redis-storage
      emptyDir: {}
```
