## Commands

### General

```console
$ kubectl get <nodes/pods/deployment/events/replicaset>
$ kubectl get pods --all-namespaces

$ kubectl describe <nodes/pods/deployment/services>
$ kubectl describe services/kubernetes-bootcamp

$ kubectl logs <pod name>

$ kubectl delete <service/deployment/pod>
$ kubectl delete service -l app=kubernetes-bootcamp # using label
$ kubectl delete deployment my-nginx
$ kubectl delete pod/my-nginx-544232

$ kubectl create -f file.yml    # Create resources via CLI or YAML
$ kubectl replace -f file.yml
$ kubectl apply     # Create/update anything via YAML
```

### Cluster

```console
$ kubectl cluster-info
```

### Deployment

```console
$ kubectl config view
```

### Generators

Helper templates for Run, Create and Expose commands. Every resource has a specification. Shows the output generated with that command.

```console
$ kubectl create deployment sample --image nginx --dry-run -o yaml
$ kubectl create job test --image nginx --dry-run -o yaml
```
