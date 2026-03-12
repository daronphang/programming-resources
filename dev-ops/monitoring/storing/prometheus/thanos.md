## Thanos

A layer on top of Prometheus that provides long-term storage (object storage including S3, GCS, etc.), high availability, and global view. Aggregates data from multiple Prometheus instances and adds HA (redundancy). Thanos can query across multiple Prometheus instances globally, and supports multi-cluster and multi-region monitoring.

### How it works

1. You deploy Prometheus instances per cluster/service
2. Thanos sidecar runs next to each Prometheus instance
3. Thanos uploads metrics to object storage and exposes a global query API
