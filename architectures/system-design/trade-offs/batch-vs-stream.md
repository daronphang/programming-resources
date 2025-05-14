## Batch vs stream processing

### Batch

- Data is collected over a period of time, and processing occurs in batches (chunks) at scheduled intervals
- Simpler to implement and maintain but has higher latency
- Stronger fault tolerance, can be easily retried
- Higher latency, suitable where real-time insights are not critical and delayed processing is acceptable

### Stream

- Data is processed in real-time as it arrives, enabling immediate processing and insights
- Requires more complex infrastructure to handle continuous flow of data, including managing state, data-in-flight, message ordering, and data deduplication
- Eventual consistency and requires careful handling of failures
- Best for applications requiring real-time decision-making
