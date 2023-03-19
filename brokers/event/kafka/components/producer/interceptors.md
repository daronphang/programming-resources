## Interceptors

Used to modify the behavior of Kafka client application without modifying its code. Kafka's ProducerInterceptor includes two key methods.

### ProducerRecord

This method will be called before the produced record is serialized and sent to Kafka. Requires a valid ProducerRecord to be returned.

### onAcknowledgement

This method does not allow modifying the response from Kafka, but you can capture information about the response.
