## Overview

### Kibana

- Open-source log analysis platform, highly coupled with Elasticsearch
- Provides users with a tool for exploring, visualizing, and building dashboards on top of the log data stored in elasticsearch clusters
- Core feature is **data querying for root cause analysis and diagnostics**
- To extrapolate data from other sources, it needs to be shipped into the ELK stack i.e. via Filebeat or Metricbeat, then Logstash, then Elasticsearch
- Does not come with an out-of-the-box alerting capability; requires implementation with third party i.e. Logz.io, ElastAlert
- Does not provide user management features

### Grafana

- Open-source visualization tool that can be used across a variety of data stores i.e. Graphite, InfluxDB, Prometheus, Elasticsearch, MySQL, PostgreSQL, etc.
- Fork of Kibana to support metrics that Kibana did not provide
- Each data source is shipped with a specific query editor that is customized for the features and capabilities that are included in the data source
- Design caters for real-time monitoring of system CPU, memory, disk and I/O utilization
- More customizable and flexible than Kibana
- Does not allow full-text data querying
- Shipped with a built-in alerting engine that allows users to attach conditional rules to dashboard panels that result in triggered alerts to a notification endpoint of your choice i.e. email, Slack, webhooks, etc.
- Provides user management features out-of-the-box
