## Event Loop (Infinite While Loop)

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

### asyncio.run()

Introduced in Python 3.7 and is responsible for getting the event loop, running tasks until they are marked as complete, and then closing the event loop.

```py
asyncio.run(main())
```

```py
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```
