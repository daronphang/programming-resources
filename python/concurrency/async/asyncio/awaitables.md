## Awaitables

An object is an awaitable object if it can be used in an await expression. Many asyncioAPIs are designed to accept awaitables. It can also be an object that defines an **await**() method that returns an iterator. Three types of awaitable objects are Coroutines, Tasks and Futures.

## Coroutines

A coroutine is a function that can be suspended and resumed. It is often defined as a generalized subroutine. Coroutines have **control over when exactly they suspend their execution**.

A subroutine is a module of instructions that can be executed on demand, and may take arguments and return a value. A subroutine can be executed, starting at one point and finishing at another point. Coroutines can be entered, exited, and resumed at many different points.

### Definition

Coroutines can be defined via the 'async def' expression.

```py
async def another_coroutine():
    print('running another coroutine B')
    await asyncio.sleep(3)
    print('completed coroutine B')
```

### Running Coroutines

Coroutines can only be executed within an event loop i.e. it can only run when the event loop is running. The typical way to start an event loop is via the asyncio.run().

```py
if __name__ == '__main__':
    asyncio.run(another_coroutine())
```

### Example

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

### Coroutines vs Generator

A generator is a function that returns a generator iterator and can suspend its execution. Contains yield expressions that produces a series of values usable in a for-loop that can be retrieved one at a time with next().

Using this paradigm, an await statement is similar to yield statement: the execution of the current function gets paused while other code is run. Once the await or yield resolves with data, the function is resumed.

Generators are a subset of coroutines. However, this required technical knowledge of generators and the development of custom task schedulers.

## Tasks

Tasks are used to schedule coroutines concurrently. A coroutine can be wrapped in an asyncio.Task object and executed independently, as opposed to being executed directly within a coroutine.

## Futures

A future is a special low-level awaitable object that represents an eventual result of an asynchronous operation. When a Future object is awaited, the coroutine will wait until the Future is resolved. Can be an exception.

Future objects in asyncio are needed to allow callback-based code to be used with async/await.

Normally, **there is no need to create Future objects** at the application level code.

```py
from asyncio import Future

future = Future()
future.cancel()
print(future.done())
print(future.cancelled())

# False
# True
```
