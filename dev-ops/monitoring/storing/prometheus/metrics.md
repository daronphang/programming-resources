## Metrics

### Counter

A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or be reset to zero on restart. It is suitable for recording the cumulative number of events.

**The rate() should only be used with counters**. When combining rate() with an aggregation operator, always take the rate() first, followed by aggregate. Moreover, rate automatically adjusts for resets.

```
http_requests_total
disk_io_time_seconds_total
disk_read_bytes_total
tasks_completed_total
```

### Gauge

A gauge is a metric that represents a single numerical value that can arbitrarily go up and down.

```
mysql_global_status_connections
http_requests_in_flight
pg_stat_activity_count
node_disk_io_now
kube_pod_status_phase
```

### Summary

Similar to a histogram, a summary samples observations (request durations, response sizes) while providing a total count of each. This is useful when you want to calculate statistical distribution over time.

```
tls_handshake_duration_seconds
task_duration_seconds
http_request_duration_seconds_sum
```
