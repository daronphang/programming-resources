## Producer

Before sending a message, need to make sure the recipient queue exists. RabbitMQ will drop the message if sent to a non-existent queue. The queue_declare() is idempotent. Messages cannot be sent directly to a queue but through an exchange.

```py
import pika

# establishing a connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declaring a queue
channel.queue_declare(queue='hello')

# publishing a message
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
```

## Subcriber

```py
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(
        queue='hello',
        on_message_callback=callback,
        auto_ack=True   # turns off message acknowledgement
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
