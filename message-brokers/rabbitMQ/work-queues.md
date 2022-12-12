## Work Queues

Work queue has the ability to parallelise work easily by scaling with more workers.

Before sending a message, need to make sure the recipient queue exists. RabbitMQ will drop the message if sent to a non-existent queue. The queue_declare() is idempotent.

Messages cannot be sent directly to a queue but through an exchange.

For better durability of queues and messages, use Publisher Confirms.

To ensure workload is evenly distributed among workers (fair dispatch), need to inform RabbitMQ not to give more than one message to a worker at a time with prefetch_count arg.

```py
# send.py
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create the queue if it doesn't exist
channel.queue_declare(
    queue='hello',
    durable=True    # queue survives if RabbitMQ restarts
    )

channel.basic_publish(
    exchange='',            # default exchange
    routing_key='hello',    # specifying which queue to go
    body='Hello World!',
    properties=pika.BasicProperties(
        delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent 'Hello World!'")
connection.close() # flush network buffers
```

Receiving messages works by subscribing a callback function to a queue.

```py
# worker.py
import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello', durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

        # consequences are serious if ack is missed
        # as messages will be redelivered and memory will be eaten
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='hello',
        on_message_callback=callback,
        auto_ack=True   # turn off acknowledgement
        )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
```

```console
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

$ # start 2 workers, can scale up easily and parallelise work
$ python worker.py
$ python worker.py
$ python send.py
```
