## Time-series databases (TSDB)

A TSDB is optimized for measuring change over time. Time-series data are simply measurements or events that are tracked, monitored, downsampled, and aggregated over time i.e. show a pattern of change over time. This could be server metrics, application performance monitoring, network data, sensor data, events, clicks, trades in a market, and many other types of analytics data. A company may adopt a TSDB if they need to monitor data in real time or if they are running applications that continuously produce data.

Since all records are timestamped, the **order of the data points is a native characteristic of the data**. This order can be used to deliver the data to a stream processing engine that can treat the ordered data as if it were a data stream.

Ensuring data quality and accuracy is critical for making data-driven decisions. Time series data can be “noisy” and contain missing or corrupted values. Time series databases often provide tools for cleaning and filtering data, as well as methods for detecting anomalies and outliers.

### Applications

- IoT and smart buildings
- Manufacturing
- Retail
- Telecommunications
- Healthcare

### Choosing a TSDB

- Data model
- Query language
- Reliability
- Performance
- Ecosystem
- Operational management
- Company and community support

### What distinguishes time series workload?

Time series databases have key architectural design properties that make them very different from other databases. These include:

- Time-stamp data storage and compression
- Data lifecycle management i.e. deleting data after a period of time
- Data summarization e.g. aggregation
- Ability to handle large time series dependent scans of many records
- Time series aware queries

### Alternatives

NoSQL databases are also often used to store time series data e.g. Cassandra, DynamoDB, MongoDB, etc. As NoSQL databases are more flexible in terms of the data format for each record, they are good for capturing time series data from a number of distinct sources.
