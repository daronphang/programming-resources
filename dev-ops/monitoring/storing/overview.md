## Overview

### Loki

- Utilizes a **log-centric** data model where logs are stored as streams of log events with labels for identification
- Designed to be cost effective and highly scalable, inspired by Prometheus
- Labels act as an index to keep the complexity low, but does not support high cardinality efficiently
- Log data is structured in a time-ordered fashion
- Logging stack includes agents (Promtail) that scrape logs and turn them into streams by adding labels, and **pushes** the streams to Loki through an HTTP API

### Elasticsearch

- Employs a document-oriented data model, storing data in JSON-like documents
- Both the key and contents of the JSON object are indexed i.e. indexes data in every field
- Highly flexible and allows for indexing and searching structured and unstructured data

### Prometheus

- **Metrics aggregator** that supports various service discovery mechanisms to automatically discover and monitor new targets without manual configuration i.e. DNS-based, Kubernetes, file-based
- Allows dynamic configuration updates without restarting Prometheus server
- Uses a **pull-based model** for collecting metrics from configured targets by making HTTP requests to the target's metrics endpoint
- Stores metrics data locally in a time-series database with a configurable retention period
- Ships with a built-in alert manager and notification system
- Provides simple visualizations but can be integrated with Grafana as a dashboarding solution
