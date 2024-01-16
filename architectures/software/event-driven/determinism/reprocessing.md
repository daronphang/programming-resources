## Reprocessing

Immutable event streams provide the ability to rewind consumer group offsets and replay processing from an arbitrary point in time, which is known as reprocessing. This is something that every event-driven microservice needs to consider in its design.

Reprocessing is typically performed only on event-driven microservices that use event time for processing events, and not those that rely on wall-clock aggregations and windowing.

Events can be late according to near real-time consumers, but not late to reprocessing-time consumers.

## Steps

### Determine the starting point

As a best practice, all stateful consumers should reprocess events from the very beginning of each event stream that they are subscribed to.

### Determine which consumer offsets to reset

Any streams that contain events used in stateful processing should be reset to the very beginning, as it is difficult to ensure that you will end up with a correct state if you start in the wrong location i.e. reprocessing bank's balance but omitting previous paychecks.

### Consider the volume of data

Some microservices may process huge quantities of events. Consider how long it may take to reprocess the events, and any bottlenecks that may exist.

### Consider the time to reprocess

It is worth calculating how much downtime you may need. Ensure that your downstream consumers are also okay with possibly stale data while your service reprocesses.

Scaling the number of consumer instances to maximum parallelism can significantly reduce the downtime, and can be scaled down once reprocessing is completed.

### Consider the impact

Some microservices perform side-effect actions that you may not want to occur during reprocessing i.e. sending email to consumers.
