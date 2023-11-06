## ClusterIP

ClusterIP is the default Service type, and provides internal connectivity between different components of an application. Kubernetes assign this Service a virtual IP address that can **solely be accessed from within the cluster** during its creation. This IP address is stable and doesn't change even if the Pods behind the Service gets rescheduled or replaced.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend
spec:
  type: ClusterIP # can be omitted as it is the default
  selector:
    app: backend
  ports:
    - name: http
      port: 80 # port on Service
      targetPort: 8080 # port on cluster
```
