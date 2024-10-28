## Work Queues

Main idea is to avoid doing a resource-intensive task immediately and waiting for it to complete. Work queue has the ability to parallelize work easily by scaling with more workers. Exchange medium is 'direct' and routing_key needs to be specified.

RabbitMQ uses **round-robin dispatching** by default. To ensure workload is evenly distributed among workers (fair dispatch), need to inform RabbitMQ not to give more than one message to a worker at a time with prefetch_count arg.

For better durability of queues and messages, need to declare durable argument for queue. However, marking messages as persistent doesn't guarantee a message won't be lost as there is short window when RabbitMQ has accepted a message and hasn't saved to a disk. For stronger durability, use **Publisher Confirms**.

```py
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()
```

```py
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
```

```sh
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

$ # start 2 workers, can scale up easily and parallelize work
$ python worker.py
$ python worker.py
$ python send.py
```
