## Event Scheduling

Event scheduling is the process of selecting the next events to process when consuming from multiple input partitions. For an immutable log-based event stream, records are consumed in an offset-based order. 

The most common event-scheduling implementation selects and dispatches the event with the oldest timestamp from all assigned input partitions to the downstream processing toplogy.

Event scheduling is a feature of many stream-processing frameworks, but is typically absent from basic consumer implementations.