## Blocking

Do not call regular functions blindly from a coroutine (async def) as they may block your event loop.

```py
import asyncio


async def some_coroutine():
    print('running some coroutine A')
    count = 0
    # this is blocking! Does not work
    for i in range(10000000):
        count += i
    print(count)
    print('above statement is blocking in current func!')


async def another_coroutine():
    print('running another coroutine B')
    await asyncio.sleep(3)
    print('completed coroutine B')


async def main():
    await asyncio.gather(some_coroutine(), another_coroutine())



if __name__ == '__main__':
    asyncio.run(main())

# running some coroutine A
# 49999995000000
# above statement is blocking in current func!
# running another coroutine B
#completed coroutine B
```

## Solutions

### Asyncio default executor

The solution to avoid event loop blockage is executing our blocking code elsewhere. We can use threads or other processes to accomplish this. Asyncio has a very convenient loop method, run_in_executor. This method uses the concurrent.futures threading and multiprocessing interface.

```py
import asyncio

async def executor_mat_heavy_lifting(mat_size: int = 10_000) -> None:
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, do_mat_heavy_lifting, mat_size)
```
