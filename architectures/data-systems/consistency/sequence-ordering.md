## Sequence number ordering

We can use sequence numbers or timestamps to order events. A timestamp need not come from a time-of-day clock (which has many problems) but from a logical clock (an algorithm to generate a sequence of numbers to identify operations, typically incremented for every operation).

## Lamport timestamps

A simple method for generating sequence numbers that is consistent with causality. Each node has a unique identifier and keeps a counter of the number of operations it has processed. Every client also keeps track of the maximum counter value it has seen so far.

When a node receives a request or response with a maximum counter value greater than its own counter value, it immediately increases its own counter to that maximum.

```
Lamport timestamp = (counter, nodeID)
```

### Example

1. Client A writes to Node 1 (1,1) and receives counter as 1
2. Client B writes to Node 2 (1,2) and receives counter as 1
3. Client B writes to Node 2 (2,2) and receives counter as 2
4. Client B writes to Node 2 (3,2) and receives counter as 3
5. Client A writes to Node 2 (4,2) and receives counter as 4
6. Client A writes to Node 1 (5,1) and receives counter as 5 (counter updated from 1 to 4)
