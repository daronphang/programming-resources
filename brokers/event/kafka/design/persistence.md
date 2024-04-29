## Persistence

### Don't fear the filesystem

Kafka relies heavily on the filesystem for storing and caching messages. There is a general perception that "disks are slow" which makes people skeptical that a persistent structure can offer competitive performance. However, a properly designed disk structure can often be as fast as the network.

Modern operating systems have become increasingly aggressive in their use of main memory for disk caching. A modern OS will happily divert all free memory to disk caching with little performance penalty when the memory is reclaimed. All disk reads and writes will go through this unified cache. However, as this feature cannot be turned off without using direct I/O, the data will most likely be duplicated.

Moreover, JVM memory usage has the following caveats:

- Memory overhead of objects is very high, often doubling the size of the data stored
- Java garbage collection becomes increasingly fiddly and slow as the in-heap data increases

This suggests a design which is very simple: rather than maintain as much as possible in-memory and flush it all out to the filesystem in a panic when we run out of space, we invert that. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel's pagecache.
