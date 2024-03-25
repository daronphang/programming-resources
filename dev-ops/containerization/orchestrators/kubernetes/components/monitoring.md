## Monitoring metrics

Kubernetes has an monitoring server called Metrics server (per cluster) that aggregates metrics (CPU, memory, network, disk utilization, etc.) from Pods and stores them **in-memory**.

The Kubelet contains a sub component known as container advisor (cAdvisor) that is responsible for retrieving performance metrics from Pods and exposing them through the Kubelet API to make them available for the metrics server.

```sh
$ git clone https://github.com/kubernetes-incubator/metrics-serve
$ kubectl create -f deploy/1.8+/
$ kubectl top node # performance metrics
$ kubectl top pod
```

### Open-source solutions

Prometheus, ELK, Datadog, dynatrace, etc.
