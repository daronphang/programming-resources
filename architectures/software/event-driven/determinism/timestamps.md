## Timestamps

Events can happen anywhere and at any time, and they often need to be reconciled with events from other producers. Synchronized and consistent timestamps are a hard requirement for comparing events across distributed systems.

An event stored in an event stream has both an offset and a timestamp. The **offset** is used by the consumer to determine which events it has already read, while the **timestamp** indicates when that event was created relative to other events, and to ensure that events are processed in the correct order.

It is possible to propagate the event time from the producer, to the event broker, and finally to the consumer. **This enables the consumer logic to make decisions based on when an event has happened.**

### Event Time

Local timestamp assigned to the event by the producer at the time the event occurred.

### Broker-Ingestion Time

Timestamp assigned to the event by the event broker. Most commonly configured to be the event time. In the event the producer's event time is unreliable, broker-ingestion time can provide a sufficient substitute.

### Consumer Ingestion Time

Time in which the event is ingested by the consumer.

### Processing Time

Wall-clock time at which the event has been processed by the consumer.

## Synchronizing Distributed Timestamps

No two indepedent systems can be guaranteed to have pricesely the same system-clock time. However, it is possible to establish local system clocks that are nearly in sync and end up being good enough for most computing purposes.

Consistent clock times are primarily accomplished by synchronizing with **NTP (Network Time Protocol)** servers, with a drift of only a few mS after 15 minutes. However, NTP synchronization is prone to failure, including network outages, misconfiguration, and transient issues.

## Processing with Timestamp Events

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
