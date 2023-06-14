## AsyncIO

Python3 has native support for async programming which provides a simple way to execute concurrent tasks. AsyncIO is a single-threaded, single-process design that uses **cooperative multitasking** i.e. gives a feeling of concurrency despite using a single thread/process. Coroutines can be scheduled concurrently, but they are not inherently concurrent.

Consider using **aiohttp** for asynchronous HTTP calls if you are blocked because of requests library as it is built on top of urllib3 which uses Python's http/socket modules (blocking). Also, use **moto** to access MongoDB asynchronously instead of relying on synchronous drivers like mongo-python.

https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

```py
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)  # non-blocking, gives execution back to async engine
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# One
# One
# One
# Two
# Two
# Two
# countasync.py executed in 1.01 seconds.
```

## Async/Await

Async/await was introduced in Python 3.5.

### Async

Async refers to a suite of expressions for working with coroutines. This includes:

- 'async def' for defining a coroutine
- 'async for' for traversing an asynchronous iterable
- 'async with' for using an asynchronous context manager

### Await

Await refers to the 'await' expression used with coroutines. It can only be used within a coroutine and is used to yield execution to an awaitable.

## asyncio.sleep vs time.sleep

time.sleep is blocking while asyncio.sleep is non-blocking i.e. it will ask the event loop to run something else while the await statement finishes its execution.

```py
import asyncio

async def hello():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

async def main():
    await asyncio.gather(hello(), hello())

asyncio.run(main())

# Hello ...
# Hello ...
# ... World!
# ... World!
```
