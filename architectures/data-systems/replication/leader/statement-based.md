## Statement-based replication

Leader logs every write request (INSERT, UPDATE, DELETE) that it executes and sends that statement log to its followers. However, there are various ways in which this approach can break down:

- Any statement that calls a non-deterministic function i.e. NOW() to get the current date, is likely to generate a different value on each replica
- Statements that have side effects (triggers, stored procedures, user-defined functions) may result in different side effects occurring in each replica unless they are deterministic

Although it is possible to workaround by replacing non-deterministic function calls with a fixed return value, there are too many edge cases, and other methods are preferred.
