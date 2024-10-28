## Persistence

### Don't fear the filesystem

Kafka relies heavily on the filesystem for storing and caching messages. Kafka logs are write-only structures, meaning data gets appended to the end of the log, and sequential reads and writes are fast, predictable, and heavily optimized by operating systems.

There is a general perception that "disks are slow" which makes people skeptical that a persistent structure can offer competitive performance. However, a properly designed disk structure can often be as fast as the network.

Modern operating systems have become increasingly aggressive in their use of main memory for disk caching. A modern OS will happily divert all free memory to disk caching with little performance penalty when the memory is reclaimed. All disk reads and writes will go through this unified cache. However, as this feature cannot be turned off without using direct I/O, the data will most likely be duplicated.

Moreover, JVM memory usage has the following caveats:

- Memory overhead of objects is very high, often doubling the size of the data stored
- Java garbage collection becomes increasingly fiddly and slow as the in-heap data increases

This suggests a design which is very simple: rather than maintain as much as possible in-memory and flush it all out to the filesystem in a panic when we run out of space, we invert that. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel's pagecache.

### Log-structured storage

Kafka, like other modern messaging systems such as Cassandra, LevelDB, and RocksDB, utilizes a log-structured storage and compaction approach instead of an on-disk mutable BTree.

This method favors long sequential disk access for reads and writes, which is highly efficient for modern disks that have unlimited space and are incredibly fast. This allows Kafka to provide features not typically found in messaging systems, such as the ability to hold onto old messages for a long time. This flexibility opens up a world of possibilities for Kafka, making it an ideal choice for tech-oriented audiences looking to build innovative applications.

The log-structured storage engine used by Kafka has several advantages over traditional databases. For example, it is highly optimized for write-heavy applications, allowing for fast and efficient writes to disk.
