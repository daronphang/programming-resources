## Mocking Functions

If mocking a method or class in a module that imports directly, need to mock that module.

```py
from unittest.mock import Mock
import pytest


@mock.patch('package.module.Class.function')
def test_mock_function(mock_func):
    assert package.module.Class.function is mock_func
```
