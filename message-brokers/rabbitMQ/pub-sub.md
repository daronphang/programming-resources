## Pub Sub

Delivering a message to multiple consumers via an exchange.

```py
# producer program

# creating an exchange
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'  # broadcasting to all queues
    )

# publishing to the exchange
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
    )
```

```py
# consumer program

# creating a queue
result = channel.queue_declare(
    queue='',   # empty parameter allows the server to choose a random queue name
    exclusive=True  # delete queue once consumer connection is closed
    )

# creating a binding to tell exchange to send messages to the queue
channel.queue_bind(
    exchange='logs',
    queue=result.method.queue
    )
```

### Temporary Queues

Specifying routing_key is crucial to point workers to the same queue. However, for broadcasting, we want each worker to hear all messages, not just a subset.

To achieve this, need a fresh, empty queue.

```py

result = channel.queue_declare(
    queue='',   # empty parameter allows the server to choose a random queue name
    exclusive=True  # delete queue once consumer connection is closed
    )
print(result.method.queue) # amq.gen-JzTY20BRgKO-HjmUJj0wLg
```
