## Mocking Functions

If mocking a method or class in a module that imports directly, need to mock that module.

```py
from unittest.mock import Mock
import pytest


@mock.patch('package.module.Class.function')
def test_mock_function(mock_func):
    assert package.module.Class.function is mock_func
```

## Mocking Libraries

If you import a class directly, mocking will not work.

```py
import redis
# from redis import Redis   -> this will not work!

class Cache:
    def __init__(self):
        r = redis.Redis()
```

```py
import unittest.mock as mock

@mock.patch('redis.Redis', FakeRedis())
def test_redis(mock_redis):
    # write tests
    pass

```
