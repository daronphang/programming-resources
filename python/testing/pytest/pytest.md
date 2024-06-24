## Fixtures

Pytest fixtures are functions that can be used to manage our apps states and dependencies. Can also use mock data that fixtures create across multiple tests.

Pytest fixtures allow writing pieces of code that are reusable across tests. A simple fixture returns a value, but can also do setup, yield a value, and teardown i.e. provides a fixed baseline so that tests execute reliably and produce consistent, repeatable results.

```py
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
```

Fixture system is reusable, flexible and can request other fixtures. Allows us to boil down complex requirements tests into more simple and organized functions.

```py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]
```

## Scope

Fixtures requiring network access depend on connectivity and are usually time-expensive to create. This can be reduced by specifying the scope.

To share fixtures across classes, modules, packages or session, place them in conftest.py.

```
function (default)
class
module
package
session
```

## Delay

```py
@patch('time.sleep', return_value=None)
def test_exponential_backoff(patched_time_sleep):
    nr = network_request()
    with pytest.raises(BadRequest) as exc:
        exponential_backoff(BadRequest)(nr)(4)
    assert str(exc.value) == 'network request failed'
```

## Monkeypatch

Monkeypatching is dynamically changing a piece of software (module, object, method) at runtime. It is often used for bug fixes or prototyping software, especially when using external APIs or libraries. Can greatly decrease the amount of time your tests take to execute.

Pytest uses this feature to allow you to test out interfaces that you don't want to actually execute i.e. Requests module for HTTP.

```py
def getcwd():
    current_path = os.getcwd()
    return current_path


def test_get_current_directory(monkeypatch):
    def mock_getcwd():
        return '/data/user/directory123'

    monkeypatch.setattr(os, 'getcwd', mock_getcwd)
    assert getcwd() == '/data/user/directory123'
```

```py
def http_get():
    r = requests.get(BASE_URL + 'get')
    if r.status_code == 200:
        response_data = r.json()
        return r.status_code, response_data["url"]


def test_get_response_success(monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = 'http://httpbin.org/get'
            self.headers = {'blaa': '1234'}

        def json(self):
            return {'account': '5678',
                    'url': 'http://www.testurl.com'
                    }

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    assert http_get() == (200, 'http://www.testurl.com')
```

## Async support

Can use plugins such as pytest-asyncio, aioresponses.

```py
@pytest.mark.asyncio
async def test_some_asyncio_code():
    res = await library.do_something()
    assert b"expected result" == res
```

```py
import aiohttp
import asyncio
from aioresponses import aioresponses

@aioresponses()
def test_request(mocked):
    loop = asyncio.get_event_loop()
    mocked.get('http://example.com', status=200, body='test')
    session = aiohttp.ClientSession()
    resp = loop.run_until_complete(session.get('http://example.com'))

    assert resp.status == 200
```

```py
@pytest.mark.asyncio
async def test_fetch_definition_async():
    s = aiohttp.ClientSession()
    kw = 'hello'
    payload = 'hello world'

    with aioresponses() as m:
        m.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{kw}', payload=payload)
        resp = await Paragraph().fetch_definition(s, kw)
        assert resp == payload
```

## Running

```console
$ pytest
```
