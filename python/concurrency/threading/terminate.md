## Terminating Threads

Generally it is a bad pattern to kill thread abruptly:

- Thread may be holding a critical resource that must be closed properly
- Thread has created several other threads that must be killed as well

### Event (ExitFlag)

A threading.Event is a thread-safe boolean variable flag that can be either set or not set. It can be shared between threads, checked, and set without fear of a race condition.

```py
import random
import signal
import threading
import time

exit_event = threading.Event()


def bg_thread():
    for i in range(1, 30):
        print(f'{i} of 30 iterations...')
        time.sleep(random.random())  # do some work...

        if exit_event.is_set():
            break

    print(f'{i} iterations completed before exiting.')


def signal_handler(signum, frame):
    exit_event.set()


signal.signal(signal.SIGINT, signal_handler)
th = threading.Thread(target=bg_thread)
th.start()
th.join()
```

### Daemons

```py
import threading
import time

def run_forever():
    while True:
        print('hello')


if __name__ == '__main__':
    try:
        t = threading.Thread(target=run_forever, daemon=True)
        t.start()
        while True:
            # once the main thread has started, there's nothing else for it to do
            # so it exits and threads are destroyed instantly
            # need to keep main thread alive
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print('interrupted!')
```
