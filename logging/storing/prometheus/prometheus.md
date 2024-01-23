## Prometheus

### Pull-based model

In an event-based monitoring system:

1. Each individual event (HTTP request, exception, etc.) is reported to a central monitoring system immediately as it happens
2. Central system then either aggregates the events into metrics (StatsD) or stores them individually for later processing (ELK)

Prometheus is not an event-based but pull-based system. Raw events are not sent to Prometheus, nor are they stored. Instead, it collects aggregated time series data i.e. it collects data from the services it monitors rather than having the services push the data to Prometheus.

Prometheus is only interested in regularly **collecting the current state of a given set of metrics**, not the underlying event that led to the generation of those metrics. This reduces the resource overhead on each target.
