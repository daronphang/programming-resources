## Threading with Pika

Pika does not have any notion of threading, and if want to use Pika with threading, need to make sure you have **one Pika connection per thread**, created in that thread i.e. Pika is not threadsafe to share one connection. Nonetheless, you can have multiple channels per connection i.e. for listening to multiple queues.

An alternative would be to use multiple threads triggered from the callback function for processing messages, but acknowledgement of message to be in the main thread that establishes the connection and retrieves the message.

https://github.com/pika/pika/blob/0.13.1/examples/basic_consumer_threaded.py
