## Synchronization

In multithreaded applications, two or more threads may need to share and access to the same data but may result in a **race condition** which can cause unexpected bugs and make tests brittle and non-deterministic. To avoid corruption of shared data, you can synchronize the access.