## Message

The AMQP protocol pre-defines a set of 14 properties that go with a message (pika.BasicProperties).

### delivery_mode

Determines if the message will be stored on disk after broker restarts. Marks a message as persistent (value of 2) or transient (any other value).

### content_type

Used to describe the mime-type of the encoding. For JSON encoding, it is a good practice to set this property to 'application/json'.

### reply_to

Commonly used to name a callback queue.

### correlation_id

Useful to correlate RPC responses with requests.
