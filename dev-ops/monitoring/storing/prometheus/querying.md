## Querying

Prometheus provides a functional query language (PromQL) that lets the user select and aggregate time series data in real-time. The result of an expression can either be shown as a graph, viewed as tabular data, or consumed by external systems i.e. HTTP API.

## Expression types

### Scalar

A simple numeric floating point value.

### Instant vector

A set of time series containing a single sample for each time series, all sharing the same timestamp. It gives you an instant in time for the metrics values i.e. **last/latest scrapped value** for each metric.

```
http_requests_total
```

### Range vector

A set of time series containing a range of data points over time for each time series i.e. range of data over the last 30 seconds. Range vector is mostly used for graphs, where you want to show an expression over a given time range.

```
http_requests_total{job="prometheus"}[5m]
```

### Instant vs Range

- Instant vectors (single value) can be charted while range vectors (multiple values) cannot as charting requires a data point on the y-axis for every timestamp on the x-axis
- Instant vectors can be compared and have arithmetic performed on them, while range vectors cannot
