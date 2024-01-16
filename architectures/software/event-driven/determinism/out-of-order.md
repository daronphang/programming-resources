## Out-of-Order

The very nature of an unbounded stream of events combined with intermittent failures means that full determinism can never be completely achieved. Out-of-order and late-arriving events are factors that you must consider in your designs. Watermarks and stream time can be used to identify and handle these events.

### Bounded

Bounded data sets, such as historical data processed in batch, are **typically fairly resilient to out-of-order data and can produce results with high determinism**. The entire batch can be thought of as one large window, and an event arriving out of order by many minutes is not relevant provided that the processing for that batch has not yet started.

However, this comes at the expense of high latency, especially for traditional nightly batch big data processing jobs where the results are available only after the 24h period.

### Unbounded

Unbounded data sets, such as ever-updating event streams, the developer must consider the requirements of latency and determinism when designing the microservice. Out-of-order events require the business to make specific decisions about how to handle them, and to determine whether latency or determinism takes priority.

## Handling Late Events

The strategy for handling late events should be determined at a business level prior to developing an engineering solution, as strategies will vary depending on the importance of the data.

Business requirements also dictate how much latency is acceptable, as waiting for events to arrive may increase determinism but at the expense of higher latency. This can negatively affect the performance characteristics of time-sensitive applications or those with tight service-level agreements.

There are several ways in which a late-arriving event can be handled.

### Drop Event

Simply drop the event.

### Wait

Delay output of the window results until a fixed amount of time has passed. This incurs higher determinism at the expense of increased latency. The old window needs to remain available for updating until the predetermined amount of time has passed.

### Grace Period

Output the windowed result as soon as the window is deemed complete. Keep the window around and available for the predetermined grace period.

Whenever a late event arrives for that window, update the aggregation and output the newly updated aggregation.

### Guidelines

Regardless of how long a microservice waits, eventually events will simply be too late and will need to be discarded. There is no cut-and-dry technical rule for handling this, but guidelines that can help as follows:

- How likely are late events to occur?
- How long does your service need to guard against late events?
- What are the business impacts of dropping late events?
- What are the business benefits of waiting a long time to capture late events?
- How much disk or memory does it take to maintain state?
- Do the expenses incurred in waiting for late events outweigh the benefits?
