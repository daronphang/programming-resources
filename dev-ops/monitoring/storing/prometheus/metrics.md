## Metrics

### Counter

A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or be reset to zero on restart.

**The rate() should only be used with counters**. When combining rate() with an aggregation operator, always take the rate() first, followed by aggregate. Moreover, rate automatically adjusts for resets.

### Gauge

A gauge is a metric that represents a single numerical value that can arbitrarily go up and down.
