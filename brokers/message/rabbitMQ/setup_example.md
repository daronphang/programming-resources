## Setup for Publisher and Consumer

```py
import pika
import json
from abc import ABC, abstractmethod
from pydantic import BaseModel, StrictInt, StrictStr
from typing import Union


class RabbitMQConfig(BaseModel):
    host: StrictStr
    port: StrictInt
    

class RabbitMQChannelConfig(BaseModel):
    queue: Union[StrictStr, None] = None
    exchange: Union[StrictStr, None] = None
    exchange_type: Union[StrictStr, None] = None


class RabbitMQPublisher(ABC):
    '''
    As creating connections are expensive, and connection should be kept open per 
    application instance.

    When publishing messages, create a new channel per thread using context mananger:
    with rmq.Channel() as chnl:
        rmq.execute()
    '''

    def __init__(self, config: RabbitMQConfig):
        # establishing a connection
        self._conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=config.host,
                port=config.port
            )
        )
        
    def Channel(self, channel_config: RabbitMQChannelConfig):
        self.channel_config = channel_config
        self.channel = self._conn.channel()
        self.channel.exchange_declare(
            exchange=channel_config.exchange,
            exchange_type=channel_config.exchange_type
        )
        return self

    @abstractmethod
    def execute(self, *args, **kwargs):
        # example
        self.channel.basic_publish(
            exchange=self.channel_config.exchange,
            routing_key=self.channel_config.queue,
            body=json.dumps({'hello': 'world'}),
            properties=pika.BasicProperties(
                content_encoding='application/json',
                priority=1,
                correlation_id='ABC123'
            )
        )
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.channel.close()


class RabbitMQConsumer:
    '''
    As creating connections are expensive, and connection should be kept open per 
    application instance.

    When publishing messages, create a new channel per thread using context manager:
    with rmq.Channel() as chnl:
        rmq.execute()
    '''
  
    def __init__(self, config: RabbitMQConfig):
        self.config = config
        self._conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=config.host,
                port=config.port
            )
        )

    def Channel(self, channel_config: RabbitMQChannelConfig):
        self.channel_config = channel_config
        self.channel = self._conn.channel()

        # declare exchange, queue and binding between exchange and queue

        self.channel.exchange_declare(
            exchange=channel_config.exchange,
            exchange_type=channel_config.exchange_type
        )

        result = self.channel.queue_declare(
            queue=channel_config.queue,
            # exclusive=True # delete queue once consumer connection is closed
        )
        # self.queue = result.method.queue

        self.channel.queue_bind(
            exchange=channel_config.exchange,
            queue=channel_config.queue,
        )

    def consume(self, callback, *args, **kwargs):
        global logger

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=self.channel_config.queue,
            on_message_callback=callback,
            # auto_ack=True
        )
        msg = '[*] Waiting for messages. To exit, press CTRL+C'
        logger.info(msg)
        self.channel.start_consuming()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.channel.close()

```
