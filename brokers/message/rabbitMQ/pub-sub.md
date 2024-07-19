## Publish/Subscribe

Delivering a message to multiple consumers via an exchange. A binding is a relationship between an exchange and a queue i.e. the queue is interested in reading messages from this exchange.

### Publisher

```py
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
```

### Subscriber

```py
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(
    queue='',   # empty parameter allows the server to choose a random queue name
    exclusive=True # delete queue once consumer connection is closed
    )
queue_name = result.method.queue

# creating a binding to tell exchange to send messages to the queue
channel.queue_bind(
    exchange='logs',
    queue=queue_name,
    routing_key='black' # binding_key for exchange
    )

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
    )

channel.start_consuming()
```

## Exchanges

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.

Instead, the producer can only send messages to an exchange. Exchanges are message routing agents, defined by the virtual host within RabbitMQ. An exchange is responsible for routing the messages to different queues with the help of header attributes, bindings, and routing keys.

An exchange:

- Receives messages from producers and the other side it pushes them to queues
- Must know exactly what to do with a message it receives
- Rules are defined by the exchange type

There are different types of exchanges:

- **Default**: Nameless; messages are routed to the queue with the name specified by routing_key parameter
- **Direct**: Message goes to queues whose binding_key equals to routing_key of message (exact match)
- **Topic**: Allows queues to subscribe to a subset of messages (wildcards)
- **Headers**: Similar to topic exchanges, but route messages based on header values instead of routing keys
- **Fanout**: dumb broadcast to all queues; ignores binding key specified in queue_bind
- **DLE**: If no matching queue can be found for the message, the message is silently dropped; DLQ provides functionality to capture undeliverable messages

### Bindings

A binding is a relationship between an exchange and a queue. This can be simply read as: the queue is interested in messages from this exchange. Bindings can take an extra binding_key parameter.

The meaning of a binding key depends on the exchange type. The fanout exchanges simply ignored its value.

It is perfectly legal to bind multiple queues with the same binding key.

## Temporary queues

Specifying routing_key is crucial to point workers to the same queue. However, for broadcasting, we want each worker to hear all messages, not just a subset.

To achieve this, need a fresh, empty queue.

```py

result = channel.queue_declare(
    queue='',   # empty parameter allows the server to choose a random queue name
    exclusive=True  # delete queue once consumer connection is closed
    )
print(result.method.queue) # amq.gen-JzTY20BRgKO-HjmUJj0wLg
```
