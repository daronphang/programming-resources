## Magnetic Disks/SSD

Durable (contents are not lost if power is turned off) and have a lower cost per gigabyte than RAM.

## In-Memory

As RAM becomes cheaper, it can feasible to store entirely in memory, distributed across several machines.

Some in-memory key-value stores such as Memcached are intended for caching, where it is acceptable for data loss if a machine is restarted. Nonetheless, durability can be achieved by writing a log of changes to disk.

Products such as VoltDB, MemSQL, and Oracle TimesTen are in-memory databases with a relational model and can offer big performance improvements by removing all overheads associated with managing on-disk data structures. Also, data structures such as priority queues and sets can be used, whereas they can be difficult to implement with disk-based indexes.

Counterintuitively, the performance advantage is not due to the fact they don't need to read from disk, but they can avoid overheads of encoding in-memory data structures in a form that can be written to disk.
