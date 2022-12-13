## Starting

When creating a thread, you pass to it a function and a list containing the arguments.

```py
x = threading.Thread(target=thread_function, args=(1,))
x.start()
```

```py
import threading

def do_first():
    print("Running do_first line 1")
    print("Running do_first line 2")
    print("Running do_first line 3")
    ...

def do_second():
    print("Running do_second line 1")
    print("Running do_second line 2")
    print("Running do_second line 3")
    ...

def main():
    t1 = threading.Thread(target=do_first)
    t2 = threading.Thread(target=do_second)

    # Start threads
    t1.start(), t2.start()

    # Wait threads to complete
    t1.join(), t2.join()

if __name__ == "__main__":
    main()

'''
# one line of code is executed at a time at non-deterministic intervals

Running do_first line 1
Running do_second line 1
Running do_first line 2
Running do_second line 2
Running do_second line 3
Running do_first line 3
'''
```

## Daemon Threads

A daemon thread will shutdown immediately when the program exits. If a program is running Threads that are not daemons, it will wait for those threads to complete before it terminates. Python threading will walk through all running threads and calls .join() on every one that does not have the daemon flag set.

Alternatively, can call .join() to tell one thread to wait for another thread to finish.

```py
x = threading.Thread(target=thread_function, args=(1,), daemon=True)
x.join()
```

## Multiple Threads

Create a context manager with ThreadPoolExecutor.

### Subthread within Thread

## Sub-threads within a Thread

```py
import concurrent.futures as c

def sub_thread(main_idx, idx):
    print(f'sub thread running in main thread {main_idx}: {idx}')


def main_thread(idx):
    print(f'main thread running: {idx}')

    with c.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):
            executor.submit(sub_thread, idx, i)


if __name__ == '__main__':
    with c.ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(3):
            executor.submit(main_thread, i)

'''
main thread running: 0
main thread running: 1
main thread running: 2
sub thread running in main thread 1: 0
sub thread running in main thread 1: 1
sub thread running in main thread 2: 0
sub thread running in main thread 2: 1
sub thread running in main thread 1: 2
sub thread running in main thread 0: 0
sub thread running in main thread 0: 1
sub thread running in main thread 2: 2
sub thread running in main thread 0: 2
'''
```

## Race Conditions

Race conditions can occur when two or more threads access a shared piece of data or resource. Can also arise when one thread frees memory or closes a file handle before the other thread has finished accessing it.

When the first thread frees up after calling time.sleep(), the second thread retrieves the shared value that has not been updated.

```py
class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)

'''
Testing unlocked update. Starting value is 0.
Thread 0: starting update
Thread 1: starting update
Thread 0: finishing update
Thread 1: finishing update
Testing unlocked update. Ending value is 1.
'''
```

### Basic Synchronization (Lock/Mutex)

To avoid race conditions, can use Lock. Only one thread at a time can have the Lock. Need to ensure Lock is released, else your program will be **Deadlock**.

```py
class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

'''
Testing locked update. Starting value is 0.
Thread 0: starting update
Thread 0 about to lock
Thread 0 has lock
Thread 1: starting update
Thread 1 about to lock
Thread 0 about to release lock
Thread 0 after release
Thread 0: finishing update
Thread 1 has lock
Thread 1 about to release lock
Thread 1 after release
Thread 1: finishing update
Testing locked update. Ending value is 2.
'''
```
