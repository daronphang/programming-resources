## Setup for Publisher and Consumer

```py
import pika
import json
from abc import ABC, abstractmethod
from pydantic import BaseModel, StrictInt, StrictStr
from typing import Union
from enum import Enum, auto

'''
Pika is not threadsafe by default, and need to use one connection per thread as per docs.
'''


class RMQComponents(Enum):
    PRODUCER = auto()
    CONSUMER = auto()


class RabbitMQConfig(BaseModel):
    host: StrictStr
    port: StrictInt
    

class RabbitMQChannelConfig(BaseModel):
    queue: Union[StrictStr, None] = None
    exchange: Union[StrictStr, None] = None
    exchange_type: Union[StrictStr, None] = None


class RabbitMQChannel:
    def __init__(self, component: Enum, channel, config: RabbitMQChannelConfig):
        self._component = component
        self._channel = channel
        self.config = config

    @property
    def channel(self):
        return self._channel

    def publish(self, body, properties: pika.BasicProperties, *args, **kwargs):
        if self._component != RMQComponents.PRODUCER:
            raise AttributeError('only producers can publish messages')

        self.channel.basic_publish(
            exchange=self.config.exchange,
            routing_key=self.config.queue,
            body=json.dumps(body),
            properties=properties
        )
    
    def consume(self, callback, *args, **kwargs):
        if self._component != RMQComponents.CONSUMER:
            raise AttributeError('only consumers can consume messages')

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=self.config.queue,
            on_message_callback=callback,
            # auto_ack=True
        )
        print('[*] Waiting for messages. To exit, press CTRL+C')
        self.channel.start_consuming()  # blocking

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._channel.close()
    

class RabbitMQPublisher(ABC):
    '''
    Use context manager with creating new channels with Publisher().Channel()
    '''

    def __init__(self, config: RabbitMQConfig):
        # establishing a connection
        self._conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=config.host,
                port=config.port
            )
        )
    
    @property
    def conn(self):
        return self._conn
        
    def Channel(self, channel_config: RabbitMQChannelConfig):
        # returns a factory instance of RabbitMQChannel()
        channel = self.conn.channel()
        channel.exchange_declare(
            exchange=channel_config.exchange,
            exchange_type=channel_config.exchange_type
        )
        return RabbitMQChannel(RMQComponents.PRODUCER, channel, channel_config)


class RabbitMQConsumer:
    '''
    Use context manager with creating new channels with Consumer().Channel()
    '''
  
    def __init__(self, config: RabbitMQConfig):
        self.config = config
        self._conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=config.host,
                port=config.port
            )
        )
    
    @property
    def conn(self):
        return self._conn

    def Channel(self, channel_config: RabbitMQChannelConfig):
        # returns a factory instance of RabbitMQChannel()
        channel = self.conn.channel()

        # declare exchange, queue and binding between exchange and queue
        channel.exchange_declare(
            exchange=channel_config.exchange,
            exchange_type=channel_config.exchange_type
        )

        result = channel.queue_declare(
            queue=channel_config.queue,
            # exclusive=True # delete queue once consumer connection is closed
        )
        # self.queue = result.method.queue

        channel.queue_bind(
            exchange=channel_config.exchange,
            queue=channel_config.queue,
        )
        return RabbitMQChannel(RMQComponents.CONSUMER, channel, channel_config)
```

```py
import pytest
import unittest.mock as mock

from mutils.brokers import RabbitMQChannelConfig, RabbitMQConfig, RabbitMQConsumer, RabbitMQPublisher


class FakePikaChannel:

    channel = True

    def exchange_declare(self, *args, **kwargs):
        pass

    def queue_declare(self, *args, **kwargs):
        pass

    def queue_bind(self, *args, **kwargs):
        pass

    def basic_publish(self, *args, **kwargs):
        pass

    def basic_qos(self, *args, **kwargs):
        pass

    def basic_consume(self, *args, **kwargs):
        pass

    def start_consuming(self, *args, **kwargs):
        pass

    def close(self):
        self.channel = False
    

class FakePikaConn:

    conn = True

    def channel(self):
        return FakePikaChannel()

    def close(self):
        self.conn = False


class Publisher(RabbitMQPublisher):
    def __init__(self, config):
        super().__init__(config)


class Consumer(RabbitMQConsumer):
    def __init__(self, config):
        super().__init__(config)


@mock.patch('pika.BlockingConnection', return_value=FakePikaConn())
def test_rabbit_mq_publisher_can_call_publish_when_channel_method_is_called(mock_pika):
    conn_config = RabbitMQConfig(host='testhost', port=123)
    chnl_config = RabbitMQChannelConfig(
        queue='testqueue',
        exchange='testexchange',
        exchange_type='testexchangetype',
    )

    instance = Publisher(conn_config)
    with instance.Channel(chnl_config) as chnl:
        assert chnl.channel.channel
        chnl.publish('test body', None)

        with pytest.raises(AttributeError) as exc:
            chnl.consume('test callback')
        assert str(exc.value) == 'only consumers can consume messages'
        
    assert not chnl.channel.channel


@mock.patch('pika.BlockingConnection', return_value=FakePikaConn())
def test_rabbit_mq_consumer_can_call_consume_when_channel_method_is_called(mock_pika):
    conn_config = RabbitMQConfig(host='testhost', port=123)
    chnl_config = RabbitMQChannelConfig(
        queue='testqueue',
        exchange='testexchange',
        exchange_type='testexchangetype',
    )

    instance = Consumer(conn_config)
    with instance.Channel(chnl_config) as chnl:
        assert chnl.channel.channel
        chnl.consume('test callback')
        
        with pytest.raises(AttributeError) as exc:
            chnl.publish('test body', None)
        assert str(exc.value) == 'only producers can publish messages'
        
    assert not chnl.channel.channel
```
