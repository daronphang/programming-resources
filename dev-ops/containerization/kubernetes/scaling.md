## Scaling

Accomplished by changing the number of replicas in a Deployment. Ensures new Pods are created and scheduled to Nodes with available resources.

Services have an integrated load-balancer that will distribute network traffic to all Pods of an exposed Deployment. Services will monitor continuously the running Pods using endpoints, to ensure the traffic is sent only to available Pods.

```console
$ kubectl scale deployments/my-nginx --replicas=2
$ kubectl get deployments
```

## Updating

When you have multiple instances of an application running, you can do rolling updates without downtime. Updates are versioned and any Deployment update can be reverted to a previous version.

```console
$ kubectl set image deployments/kub-boot kub-boot=kub-boot:v2

$ kubectl rollout status deployments/kub-boot
$ kubectl describe services/kub-boot

$ kubectl rollout undo deployments/kub-boot
```
