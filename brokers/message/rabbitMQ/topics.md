## Topics

Messages sent to a topic exchange can't have an arbitrary routing_key: it must be a list of words, delimited by dots, limited to 255 bytes.

```
stock.usd.nyse
quick.orange.rabbit
```

Each queue can have multiple binding_keys. The binding_key must also be in the same form. The logic behind the topic exchange is similar to a direct one: a message sent with a particular routing key will be delivered to all the queues that are bound with a matching binding_key.

However, there are two important special cases for binding_keys:

- \* (star) can substitute for exactly one word
- \# (hash) can substitute for zero or more words

```
Binding keys of queues:
Q1 -> *.orange.*
Q2 -> *.*.rabbit
Q2 -> lazy.#

Messages with routing_keys:
quick.orange.rabbit -> Q1 and Q2
lazy.orange.elephant -> Q1 and Q2
lazy.brown.fox -> Q2
lazy.pink.rabbit -> Q2 (only once)
quick.brown.fox -> Discarded
```
