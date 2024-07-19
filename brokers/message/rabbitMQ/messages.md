## Message acknowledgements

If a consumer dies (channel closed, TCP connection lost), RabbitMQ will re-queue if it didn't receive an acknowledgement from the consumer. Timeout is 30minutes by default.

This can be turned off by setting auto_ack to True. However, any message delivered to the consumer will be marked for deletion, and if it terminates during processing, the message will be lost.

Acknowledgements must be sent on the same channel that received the delivery. Attempts to acknowledge using a different channel will result in a **channel-protocol exception**.

## Message durability

When RabbitMQ crashes or restarts, it will forget the queues and messages unless you tell it not to. This can be done by marking **both the queue and messages as durable**.

However, RabbitMQ doesn't allow you to redefine an existing queue with different parameters and will return an error to any program that tries to do that. A quick workaround is to define a new queue with a different name.

```go
q, err := ch.QueueDeclare(
  "hello",      // name
  true,         // durable queue
  false,        // delete when unused
  false,        // exclusive
  false,        // no-wait
  nil,          // arguments
)

err = ch.PublishWithContext(ctx,
  "",           // exchange
  q.Name,       // routing key
  false,        // mandatory
  false,
  amqp.Publishing {
    DeliveryMode: amqp.Persistent, // durable message
    ContentType:  "text/plain",
    Body:         []byte(body),
})
```

## prefetch_count

In a situation with two workers, when all odd messages are heavy and even messages are light, one worker will be constantly busy and the other one will do hardly any work. Well, RabbitMQ doesn't know anything about that and will still dispatch messages evenly.

This happens because RabbitMQ just dispatches a message when the message enters the queue. It doesn't look at the number of unacknowledged messages for a consumer. It just blindly dispatches every n-th message to the n-th consumer.

In order to defeat that we can use **prefetch_count** setting. This uses the basic.qos protocol method to tell RabbitMQ not to give more than one message to a worker at a time i.e. don't dispatch a new message to a worker until it has processed and acknowledged the previous one.

```go
channel.basic_qos(prefetch_count=1)
```

If all the workers are busy, your queue can fill up. You will want to keep an eye on that, and maybe add more workers, or use message TTL.
