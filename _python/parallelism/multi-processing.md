## Multiprocessing

Multiprocessing is useful for performing multiple CPU intensive operations. Processes are completely separate and protected from one another. Allows you to create programs that can run concurrently and bypassing GIL, and use entirety of CPU core.

### Highlights

- Separates memory space; however, as a consequence, sending data between processes require pickling/unpickling and putting data into low-level formats.
- Code is straightforward.
- Takes advantage of multiple CPUs and cores.
- Avoids GIL limitations for cPython.
- Eliminates most needs for synchronization primitives unless shared memory is used.
- Child processes are interruptible/killable.
- Has larger memory footprint.
- Much more expensive to create and destroy.
