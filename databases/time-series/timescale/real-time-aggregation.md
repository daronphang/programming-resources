## Continuous aggregates

Continuous aggregates allow one to specify a SQL query that continually processes raw data into a so-called **materialized table**. However, unlike a materialized view, **continuous aggregates do not need to be refreshed manually**.

Continuous aggregates are a kind of hypertable that is refreshed automatically in the background as new data is added, or old data is modified. Changes to your dataset are tracked, and the hypertable behind the continuous aggregate is automatically updated in the background. Continuous aggregates are updated continuously and incrementally, which means they are less resource intensive to maintain than materialized views.

```sql
CREATE MATERIALIZED VIEW stock_candlestick_daily
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 day', "time") AS day,
  symbol,
  max(price) AS high,
  first(price, time) AS open,
  last(price, time) AS close,
  min(price) AS low
FROM stocks_real_time srt
GROUP BY day, symbol
```

### Hypertables

Hypertables are PostgreSQL tables with special features that make it easy to handle time-series data. Anything you can do with regular PostgreSQL tables, you can do with hypertables. In addition, you get the benefits of improved performance and user experience for time-series data.

### Benefits

- **Query performance**: By executing queries against pre-calculated results, rather than the underlying raw data, continuous aggregates can significantly improve query performance
- **Storage savings with downsampling**: Continuous aggregates are often combined with data retention policies for better storage management i.e. raw data will be dropped after it reaches a certain age, while aggregated data can be stored for much longer

For example, if we are collecting CPU usage metrics per second, and we want to compute hourly histogram of usage consumption over the course of 7 days for 10 servers:

```
Raw data:
10 servers * 60s * 60m * 24h * 7 days = 6,048,000 rows of data

Pre-computed/aggregated data per hour:
10 severs * 24h * 7 days = 1680 rows of data
```

However, although pre-computed data will cut down the amount of data processed at query time significantly, it will lag behind the latest data i.e. stale data. Making the refresh lag smaller comes at a higher cost and load.

## Real-time aggregation

Real-time aggregates build on continuous aggregates' ability to increase query speed and optimize storage. With real-time aggregation, when you query a continuous aggregate view, rather than just getting the pre-computed aggregate from the materialized table, the query will transparently combine this pre-computed aggregate with raw data from the hypertable that’s yet to be materialized.

When processing the query, the database engine will conceptually take a UNION ALL between results from the materialized table up to the completion threshold, with results from the raw table from the completion threshold up to now().

```
Materialized table: 10 servers * (22 hours + 24 hours * 6 days) = 1660 rows

Raw data: 10 servers * 60 seconds * 90 minutes = 54,000 rows
```
