## Commits and Offsets

Whenever we call poll(), it returns records written to Kafka that consumers in our group have not read yet. Hence, we have a way of tracking which records were read by a consumer of the group. One of Kafka's unique characteristics is that it does not track acknowledgements from consumers the way many JMS queues do. Instead, it allows consumers to use Kafka to track their position (offset) in each partition.

The action of updating the current position in the partition is called an **offset commit**. Consumers commit the last message they have succcessfully processed from a partition and implicitly assume that every message before the last was also successfully processed.

If a consumer crashes or a new consumer joins the group, a rebalance is triggered, and each consumer may be assigned to a new set of partitions than the one it processed before. In order to know where to pick up the work, the consumer will read the latest committed offset of each partition and continue from there.

### Offset Management

If the committed offset is smaller than the offset of the last message the client processed, messages between the last processed offset and committed offset will be processed twice. Vice versa, messages may also be missed by the group.

When committing offsets either automatically or without specifying the intended offsets, the default behavior is to commit the offset after the last offset that was returned by poll().

### Automatic Commit

Configured by setting enable.auto.commit to be true. By default, automatic commits occur every five seconds. If the consumer crashes within the five seconds, **events that arrived in that period will be processed twice**.

With autocommit enabled, when it is time to commit offsets, the next poll will commit the last offset returned by the previous poll. As it doesn't know which events were actually processed, it is critical to always process all the events returned by poll() before calling poll() again.

### Explicit Commit

The simplest and most reliable of the commit API is commitSync(). This API will commit the latest offset returned by poll() and return once the offset is committed.

Similarly, if commitSync() is called before processing all records in the collection, you risk missing the messages that were committed but not processed, in the event the application crashes. When there is an error committing, commitSync() will continue to retry.

### Asynchronous Commit

Instead of waiting for the broker to respond to a commit, we just send the request and continue on with commitAsync(). Drawback is that it will not retry in the event the commit encounters an error:

- commit offset 2000 is made but encounters temporary network error
- commit offset 3000 is made and successful
- commit offset 2000 is successful and overwrites 3000
- during rebalancing, duplicates may occur

There is an option to pass a callback that will be triggered when the broker responds. It is common to use it to log commit errors or to count them in a metric.

A simple pattern to get the commit order right for asynchronous retries is to use a monotonically increasing sequence number. Every time a commit is made, the sequence number is increased and added to the commitAsync callback.

### Combning Sync and Async Commits

A common pattern is to combine both commitSync() and commitAsync() before shutdown.

```java
Duration timeout = Duration.ofMillis(100);
try {
    while (!closing) {
        ConsumerRecords<String, String> records = consumer.poll(timeout);
        for (ConsumerRecord<String, String> record : records) {
            System.out.printf("topic = %s, partition = %s, offset = %d,
            customer = %s, country = %s\n",
            record.topic(), record.partition(),
            record.offset(), record.key(), record.value());
        }
        consumer.commitAsync();
    }
    consumer.commitSync();
    } catch (Exception e) {
        log.error("Unexpected error", e);
    } finally {
        consumer.close();
}
```

### Committing a Specified Offset

Useful if the poll() returns a huge batch and you want to commit offsets in the middle to avoid having to reprocess all rows in the event a rebalance occurs. Not able to call either commitSync() and commitAsync() as they will only commit the last offset returned.

### Consuming Records with Specific Offsets

Sometimes you want to start reading at a different offset. You can also start reading from the start or at the end of the partition.

```
seekToBeginning()
seekToEnd()
```

## Exiting Consumer

If you want to exit immediately even though the consumer may be waiting on a long poll(), you can call consumer.wakeup() in a separate thread that is thread-safe. This will abort the poll() with WakeupException that does not need to be handled.

You can call consumer.close() before exiting to commit offsets if needed, and to send the group leader a message that the consumer is leaving the group. Ths coordinator will trigger rebalancing immediately and you will not need to wait for session timeout before partitions are reassigned.
