## Serializability

When handling race conditions, isolation levels are difficult to understand and inconsistently implemented across different databases. Using **serializable isolation** is the best solution; however, not everyone uses it as either it doesn't scale (serial execution) or performance well (2PL).
