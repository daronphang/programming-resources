## Prometheus

A time-series monitoring and alerting system that collects metrics from applications and systems, storing data locally on the Prometheus server. Good for short to medium-term storage (days to weeks).

### Pull-based model

In an event-based monitoring system:

1. Each individual event (HTTP request, exception, etc.) is reported to a central monitoring system immediately as it happens
2. Central system then either aggregates the events into metrics (StatsD) or stores them individually for later processing (ELK)

Prometheus is not an event-based but pull-based system. Raw events are not sent to Prometheus, nor are they stored. Instead, it collects aggregated time series data from the services it monitors on a schedule rather than having the services push the data to Prometheus.

Prometheus is only interested in regularly **collecting the current state of a given set of metrics**, not the underlying event that led to the generation of those metrics. This reduces the resource overhead on each target.

### How it works

```
Applications → expose /metrics as an HTTP endpoint
        ↑
Prometheus server scrapes metrics
        ↓
Time-series database
        ↓
Queries / dashboards / alerts
```

### Exporter container

Sometimes the applications may not expose metrics. Hence, an exporter container is required to push data to Prometheus server. These may run as separate Pods, DaemonSets, or sidecars, and Prometheus then scrapes the exporters:

- Node Exporter: Node CPU and memory
- Blackbox Exporter: HTTP checks
- MySQL Exporter: MySQL metrics

In Kubernetes, instead of editing the Prometheus config, we can create a ServiceMonitor.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
spec:
  selector:
    matchLabels:
      app: my-service
  endpoints:
    - port: metrics
```

### Config

```yaml
global:
  scrape_interval: 15s # how often to scrape targets
  evaluation_interval: 15s # how often to evaluate alert rules

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "my-app"
    static_configs:
      - targets:
          - "10.0.0.5:8080"
          - "10.0.0.6:8080"
```
