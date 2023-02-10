## Threading

Pika does not have any notion of threading, and if want to use Pika with threading, need to make sure you have a Pika connection per thread, created in that thread i.e. Pika is not threadsafe to share one connection.
