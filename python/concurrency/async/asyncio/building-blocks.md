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
