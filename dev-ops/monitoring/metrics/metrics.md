## Metrics

While a log tells you what happened (an event), a metric tells you how many or how fast things are happening (a state). There are three primary metric types: counter, gauge and histogram/summary.

### Counter

A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase. Suitable for recording the cumulative number of events, e.g. total requests, errors, or bytes served. It resets to zero only if the process restarts.

```
http_requests_total
disk_io_time_seconds_total
disk_read_bytes_total
tasks_completed_total
```

#### Rate

Rate is the slope of the line between two data points. **The rate() should only be used with counters**. When combining rate() with an aggregation operator, always take the rate() first, followed by aggregate. Moreover, rate automatically adjusts for resets.

### Gauge

A gauge is a metric that represents a single numerical value that can arbitrarily go up and down. Used for current memory usage, number of active goroutines, or available disk space.

```
mysql_global_status_connections
http_requests_in_flight
pg_stat_activity_count
node_disk_io_now
kube_pod_status_phase
```

### Summary/histogram

Measures the distribution of values, and samples observations (request durations, response sizes) while providing a total count of each. This is useful when you want to calculate statistical distribution over time, e.g. latency. It tells you "80% of requests took less than 50ms."

```
tls_handshake_duration_seconds
task_duration_seconds
http_request_duration_seconds_sum
```

## Labels and dimensions

This is the most powerful part of modern metrics. Instead of logging total_requests, you log total_requests with labels.

## Calculation process

```
q("sum:1min-avg-zero:rate{counter}:toutiao.ti.cdn.bde.req_total.store{cluster=literal_or($cluster), domain=literal_or($domain), dc=literal_or(edge)}", "$start", "")
```

1. System filters raw data based on the tags
2. System calculates the rate for each series given a counter. For example, if Y2 is 1000, and Y1 is 9500, with a time interval of 10s, the rate is 50 requests per second
3. System performs downsampling by grouping the values into 1min buckets and takes the average
4. System performs aggregation by taking all the values and collapsing them into a single line. Aggregation is needed because of **cardinality**. For any rate (gauge or counter), we usually sum across the servers to get the total traffic
