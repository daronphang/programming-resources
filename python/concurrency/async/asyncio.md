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

### asyncio.sleep vs time.sleep

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

## Building Blocks

### Event Loop (Infinite While Loop)

Event loop is the core of every asyncio application. Event loop runs async tasks and callbacks, performs network IO operations, and run subprocesses.

A programming construct that waits for and dispatches events/messages in a program i.e. when A happens, do B. Similar to JS event loops with onclick callback. It is called a loop as it is constantly collecting events and loops over them to find what to do with the event.

Main task that is responsible for managing the asynchronous tasks and distributing them for execution. Keyword 'await' waits for the result and passes the control to the event loop i.e. suspends the execution of the surrounding coroutine.

```py
import asyncio

# if there is no running event loop set,
# fn will return get_event_loop_policy().get_event_loop()
loop = asyncio.get_event_loop()

# preferred method to get event loop as get_event_loop() has complex behavior
loop = asyncio.get_running_loop()

# set loop as current event loop for the current OS thread
asyncio.set_event_loop(loop)

asyncio.new_event_loop()
```

```py
loop.run_until_complete(future)
loop.run_forever()  # runs until stop() is called
loop.stop()
loop.is_running() # true/false
loop.is_closed()

# loop must NOT be running when called
# any pending callbacks will be discarded
loop.close()
```

### Coroutines

Functions that schedule the execution of the events and whose execution you can pause, similar to generators. Any function defined as async is a coroutine. To run coroutines, three mechanisms are provided.

Coroutines don't do much on their own until they are tied to the event loop.

```py
# does nothing but returns the function's address
main()

# starts event loop and runs the coroutine
asyncio.run(main())

# make coroutine to run concurrently
asyncio.create_task()

# another way to run multiple coroutines concurrently, allows chaining
# runs awaitable objects in the aws sequence concurrently
# neatly puts a collection of routines (futures) into a single future i.e. waits for all of them to be completed
asyncio.gather()
```

```py
import asyncio
import time

async def say_something(delay, words):
  print(f'before {words}')
  await asyncio.delay(delay)
  print(f'after {words}')

async def main():
  print('start')
  # tasks are run concurrently
  task1 = asyncio.create_task(say_something(1, 'task1'))
  task2 = asyncio.create_task(say_something(1, 'task2'))
  await task1
  await task2
  print('end')

async def main2():
  start = time.time()
  await asyncio.gather(say_something(1, 'task1'), say_something(1, 'task1'))
  elapsed = time.time() - start
  print(f'{elapsed:0.2f} seconds')

asyncio.run(main())
```

### Futures

Result of the execution of the coroutine. Can be an exception.

```py
from asyncio import Future

future = Future()
future.cancel()
print(future.done())
print(future.cancelled())

# False
# True
```

### Timeouts

Used to set timeout for an awaitable object to complete. Useful if you want to raise an exception if it takes too long to complete.

```py
import asyncio

async def slow_op():
  await asyncio.sleep(400)
  print('completed')

async def main():
  try:
    await asyncio.wait_for(slow_op(), timeout=1.0)
  except asyncio.TimeoutError:
    print('timeout')
```

### wait

When using wait(), asyncio does not cancel futures/tasks if FIRST_EXCEPTION or FIRST_COMPLETED is used. Need to explicitly cancel the futures.

```py
while tasks:
    finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for x in finished:
        result = x.result()

        if result:
            # cancel the other tasks, we have a result. We need to wait for the cancellations
            # to propagate.
            for task in unfinished:
                task.cancel()
            await asyncio.wait(unfinished)
            return result

    tasks = unfinished
```

## Example

```py
class QuotaAggregator:
    RESOURCES = [
        'DEVICE_CATEGORY',
        'METRO_QUOTA',
        'RDA_QUOTA',
    ]

    def __init__(self, userinfo: UserInfo, endpoint: str):
        self.userinfo = userinfo
        self.endpoint = endpoint
        self.agg_quota = {}

    async def fetch_resource_task(self, client, resource: str):
        async with client.post(
            urljoin(self.endpoint, resource),
            json={
                'userinfo': json.loads(self.userinfo.json()),
                'payload': {}
            }
        ) as resp:
            payload = await resp.json()
            if resp.status >= 400:
                logger.error(f'unable to fetch resource {resource}: {payload}')
                resp.raise_for_status()
        return (resource, payload)

    async def execute(self):
        async with aiohttp.ClientSession() as client:
            tasks = []
            for r in self.RESOURCES:
                task = asyncio.create_task(self.fetch_resource_task(client, r))
                tasks.append(task)

            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
            for task in done:
                if task.exception():
                    # cancel pending tasks, need to wait for cancellations to propagate
                    for pt in pending:
                        pt.cancel()
                    await asyncio.wait(pending)
                    raise AggQuotaException('unable to fetch quota resources')
                else:
                    (resource, payload) = task.result()
                    self.agg_quota[resource.lower()] = payload

            return self.agg_quota

```
