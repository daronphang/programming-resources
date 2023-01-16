## Publish Subscribe

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

```
direct      Message goes to queues whose binding_key == routing_key of message
topic
headers
fanout      Ignores binding key specified in queue_bind
```

## Temporary Queues

Specifying routing_key is crucial to point workers to the same queue. However, for broadcasting, we want each worker to hear all messages, not just a subset.

To achieve this, need a fresh, empty queue.

```py

result = channel.queue_declare(
    queue='',   # empty parameter allows the server to choose a random queue name
    exclusive=True  # delete queue once consumer connection is closed
    )
print(result.method.queue) # amq.gen-JzTY20BRgKO-HjmUJj0wLg
```
