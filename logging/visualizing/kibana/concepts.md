## Index Pattern

Kibana requires an index pattern to tell it which Elasticsearch data you want to access, and whether the data is time-based. An index pattern can point to one or more Elasticsearch data streams, indices, or index aliases by name.

```
logs-elasticsearch-prod-*       Time-based index pattern with field @timestamp (immutable)
```
