## Determinism with Event-Driven Workflows

Fully deterministic processing is the ideal case, where every event arrives on time and there is no latency, no producer or consumer failures, and no intermittent network issues. However, since we need to deal with them, there are a number of components and processes that work together to help us achieve best-effort determinism, which should be sufficient for most cases.

## Timestamps

Synchronized and consistent timestamps are a hard requirement for comparing events across distributed systems.

### Synchronizing Distributed Timestamps

No two indepedent systems can be guaranteed to have pricesely the same system-clock time. However, it is possible to establish local system clocks that are nearly in sync and end up being good enough for most computing purposes.

Consistent clock times are primarily accomplished by synchronizing with NTP (Network Time Protocol) servers, with a drift of only a few mS after 15 minutes. However, NTP synchronization is prone to failure, including network outages, misconfiguration, and transient issues. 

### Processing with Timestamp Events

Timestamps provide a way to process events distributed across multiple event streams and partitions in a consistent temporal order. For instance, a bank processing deposit and withdrawal event streams must ensure they are processed in the correct temporal order.

```
Deposit Stream
$10, 10s
$20 100s

Withdrawal Stream
$25, 120s

Order: +10, +20, -25 (considering event's timestamp)
Order: +10, -25, +20 (naive approach, round-robin)
```