## kubectl

kubectl is used for most Kubernetes management tasks. You should use a version no more than one minor version higher/lower than your cluster.

At a high level, kubectl converts commands into HTTP REST requests with JSON content required by the API server. It uses a configuration file to know which cluster and API server endpoint to send commands to, and it takes care of sending authentication data with commands.

The kubeconfig file is located at `$HOME/.kube/config` and contains definitions for:

- Clusters: List of clusters that kubectl knows about (each has a name, certificate info and API server endpoint)
- Users: Credentials for different users with different permissions
- Contexts: Group together clusters and users under a friendly name

```yaml
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority: C:\Users\nigel\.minikube\ca.crt
    server: https://192.168.1.77:8443 name: shield
users:
- name: coulson
user:
    client-certificate: C:\Users\nigel\.minikube\client.crt
    client-key: C:\Users\nigel\.minikube\client.key
contexts:
- context:
    cluster: shield
    user: coulson
    name: director
current-context: director
```

### General

```bash
$ kubectl get <nodes/pods/deployment/events/replicaset>
$ kubectl get pods --all-namespaces

$ kubectl describe <nodes/pods/deployment/services>
$ kubectl describe services/kubernetes-bootcamp
$ kubectl describe configmaps

$ kubectl logs <pod name>

$ # to delete pods, need delete deployment first
$ kubectl delete <service/deployment/pod>
$ kubectl delete service -l app=kubernetes-bootcamp # using label
$ kubectl delete deployment my-nginx
$ kubectl delete pod/my-nginx-544232
```

### Shell

```sh
$ kubectl exec --stdin --tty shell-demo -- /bin/bash
```

### Cluster

```sh
$ kubectl cluster-info
```

### Deployment

```sh
$ kubectl config view
```

### Generators

Helper templates for Run, Create and Expose commands. Every resource has a specification. Shows the output generated with that command.

```sh
$ kubectl create deployment sample --image nginx --dry-run -o yaml
$ kubectl create job test --image nginx --dry-run -o yaml
```

### Output

The -o flag allows us to output details in different formats.

```sh
$ kubectl create namespace test-123 --dry-run -o json
$ kubectl create namespace test-123 --dry-run -o yaml
$ kubectl get pods -o wide # with additional info
```

### Logging

```sh
$ kubectl logs -f <pod-name>
$ kubectl logs -f <container-name> # for multiple containers

$ vim /var/log/pods
$ journalctl | grep apiserver
```

### Labels

```sh
$ kubectl get all --selector key=value
```

### Debugging network

```sh
$ kubectl port-forward svc/argocd-server -n argocd 8080:443
$ # ctrl + z to stop the process
$ bg # resume process in background
$ fg # bring process back to foreground later

$ curl localhost:8080 # to access the application
```
