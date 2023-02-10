## Parallelism

Threading can be used if program has alot of I/O or Network usage, or multiprocessing if it is CPU-bound.

https://cs.wellesley.edu/~cs304/lectures/threads/  
https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python#:~:text=What's%20the%20difference%20between%20Python,child%20processes%20bypassing%20the%20GIL.

## Threading vs Async vs Multiprocessing

- Multiprocessing is effectively running multiple tasks simultaneously and useful for CPU-bound tasks (true parallelism)
- Threading is useful for I/O-bound and from time to time, 'freezes' the execution of one thread and jumps to executing another one (context switching that happens constantly at non-deterministic intervals or randomly)
- asyncio is a method to effectively handle many I/O operations for an application within a single thread using event loop i.e. you decide when the context switch happens and have better control of when the execution is given to the other block of code
- Asynchronous is about tasks, while multi-threading is about workers
- In threading, one line of code is executed at a time but we constantly change which line to run whereas asyncio runs one block of code at a time
- asyncio is preferred over threading as code is cleaner and race conditions are harder to manage which may cause hard-to-debug problems
- All three are capable of doing concurrent (non-blocking) tasks
