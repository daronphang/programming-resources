## Queues

Implements First-In-First-Out (FIFO) policy. Element to be deleted is always the one that has been in the set the longest time. Has a head and tail.

### Operations

```
enqueue(Q, x) {
  Q[Q.tail] = x
  if (Q.tail === Q.length)
    Q.tail = 1
  else
    Q.tail = Q.tail + 1
}

dequeue(Q) {
  x = Q[Q.head]
  if Q.head == Q.length
    Q.head = 1
  else
    Q.head = Q.head + 1
  return x
}
```

## Priority Queues

Heap data structure is primarily used to represent a PQ.

Python can only implement a min heap; make all values negative to simulate a max heap. Update operations and retrieving min/max take O(logn) time.

https://docs.python.org/3/library/heapq.html

```py
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapq.heapify(pq)
        for _ in range(k): heapq.heapreplace(pq, pq[0]//2)
        return -sum(pq)
```

### Heapify List of Objects

Can either transform each object into a tuple, and heapify will sort each item based on the first element of the tuple.

```py
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
heappop(h)
```

Alternatively, can modify lt() to specify the attribute to compare.

```py
import heapq

def __lt__(self, other):
  return self.x < other.x

heapq.__lt__ = __lt__
```

## Deque (Double-Ended Queue)

A linear collection that supports elements insertion and removal at both ends. Deque provides O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.
