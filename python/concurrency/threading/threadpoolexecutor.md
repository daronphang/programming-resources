## ThreadPoolExecutor

A class that is used to create and manage thread pools. Extends the Executor class and returns Future objects when it is called.

Using threading.Thread is manual as compared to concurrency.futures.ThreadPoolExecutor which is automatic.

https://superfastpython.com/threadpoolexecutor-in-python/#What_Are_Thread_Pools

### Executor

Defines three methods used to control our thread pool. For map(), each application of the function to an element happens async.

```
submit()        Dispatch a function to be executed and return a future object
map()           Apply a function to an iterable of elements
shutdown()      Shutdown the executor
```

### Worker

Workers are created as daemon threads. This is to allow the interpreter to exit when there are still idle threads in a ThreadPoolExecutor's thread pool. However, allowing workers to die has two undesirable properties:

- Workers would still be running during interpreter shutdown and would fail in unpredictable ways
- Workers could be killed while evaluating a work item, which could be bad if the callable has external side effects

This is workaround by installing an exit handler and calls join() to wait for threads to finish.

```py
_threads_queues = weakref.WeakKeyDictionary()
_shutdown = False

def _python_exit():
    global _shutdown
    _shutdown = True
    items = list(_threads_queues.items())
    for t, q in items:
        q.put(None)
    for t, q in items:
        t.join()

atexit.register(_python_exit)
```

### Future

We do not need to create Future objects; only receive them and call functions. A Future object is returned from submit().

There is always one Future object for each task sent via submit().

Both result() and exception() allow a timeout to be provided as an arg. If timeout expires, a TimeoutError will be raised.

Any exceptions raised in callback functions will not impact the task or thread pool.

```
cancelled()         Returns True if task was cancelled before executed
running()           Returns True if task is currently running, cannot be cancelled
done()              Returns True if task has completed/cancelled
result()            Access the result
exception()         Access any exception raised
add_done_callback() Adds a callback fn to the task to be executed after completion
```

### Wait

```py
done, not_done = wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
done, not_done = wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
done, not_done = wait(futures, return_when=concurrent.futures.FIRST_EXCEPTION)

# get results as soon as they become available
for future in as_completed(futures):
    result = future.result() # blocking
```

## Lifecycle

Can create ThreadPoolExecutor as a context manager. To pass both positional and named arguments instead of a list, use submit().

```py
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # can submit tasks and get futures by calling submit() or map()
    # async
    # map returns an iterable immediately rather than lazily
    for result in executor.map(thread_function, range(3), timeout=5):
        print(result)

    # sync
    # submit() submits one task to the thread pool for execution
    for index in range(3):
        # .submit(func, *args, **kwargs)
        future = executor.submit(thread_function, index)    # non-blocking
        result = future.result()    # blocking

    # dispatch tasks into the thread pool and create a list of futures
    futures = [executor.submit(my_task, my_data) for my_data in my_datalist]

    # wait for futures to complete
    done, not_done = wait(
        futures,
        return_when=concurrent.futures.FIRST_COMPLETED  # ALL_COMPLETED
        )
```

## Example

```py
from os import makedirs
from os.path import basename
from os.path import join
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor

# download a url and return the raw data, or None on error
def download_url(url):
    try:
        # open a connection to the server
        with urlopen(url, timeout=3) as connection:
            # read the contents of the html doc
            return connection.read()
    except:
        # bad url, socket timeout, http forbidden, etc.
        return None

# save data to a local file
def save_file(url, data, path):
    # get the name of the file from the url
    filename = basename(url)
    # construct a local path for saving the file
    outpath = join(path, filename)
    # save to file
    with open(outpath, 'wb') as file:
        file.write(data)
    return outpath

# download and save a url as a local file
def download_and_save(url, path):
    # download the url
    data = download_url(url)
    # check for no data
    if data is None:
        print(f'>Error downloading {url}')
        return
    # save the data to a local file
    outpath = save_file(url, data, path)
    # report progress
    print(f'>Saved {url} to {outpath}')

# download a list of URLs to local files
def download_docs(urls, path):
    # create the local directory, if needed
    makedirs(path, exist_ok=True)
    # create the thread pool
    n_threads = len(urls)
    with ThreadPoolExecutor(n_threads) as executor:
        # download each url and save as a local file
        _ = [executor.submit(download_and_save, url, path) for url in urls]

# python concurrency API docs
URLS = ['https://docs.python.org/3/library/concurrency.html',
        'https://docs.python.org/3/library/concurrent.html',
        'https://docs.python.org/3/library/concurrent.futures.html',
        'https://docs.python.org/3/library/threading.html',
        'https://docs.python.org/3/library/multiprocessing.html',
        'https://docs.python.org/3/library/multiprocessing.shared_memory.html',
        'https://docs.python.org/3/library/subprocess.html',
        'https://docs.python.org/3/library/queue.html',
        'https://docs.python.org/3/library/sched.html',
        'https://docs.python.org/3/library/contextvars.html']
# local path for saving the files
PATH = 'docs'
# download all docs
download_docs(URLS, PATH)
```
