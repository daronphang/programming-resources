## Memory-Mapped Files

Most OS can take advantage of a VM implementation to map a file into memory. The file can then be accessed as if it were an in-memory array, **which is much faster than the traditional file operations**.

### Procedure

1. Get a channel for the file. A channel is an abstraction for a disk file that lets you access OS features such as memory mapping, file locking, and fast data transfers between files

```java
FileChannel channel = FileChannel.open(path, options);
```

2. Get a ByteBuffer from the channel by calling map() and provide a mapping mode (read, read/write, private)

```java
MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0, length);
```

3. Once you have the buffer, you can read/write data using methods of the ByteBuffer class and superclass. Buffers support both sequential and random data access

```java
// sequentially
while (buffer.hasRemaining()) {
    byte b = buffer.get();
    ...
}
// random access
for (int i = 0; i < buffer.limit(); i++) {
    byte b = buffer.get(i);
    ...
}
```

### Locking

```java
FileChannel = FileChannel.open(path);
FileLock lock = channel.lock();

// alternative
FileLock lock = channel.tryLock();
```

### Example

```java
public static long checksumMappedFile(Path filename) throws IOException {
    try (FileChannel channel = FileChannel.open(filename)) {
        CRC32 crc = new CRC32(); // details of CRC not important
        int length = (int) channel.size();
        MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_ONLY, 0, length);

        for (int p = 0; p < length; p++) {
            int c = buffer.get(p);
            crc.update(c);
        }
        return crc.getValue();
    }
}
```

## Buffer Data Structure

When you use memory mapping, you make a single buffer that spans the entire file or the area of the file that you are interested in. You can also use buffers to read and write more modest chunks of information.

A buffer is an array of values of the same type. The Buffer class is an abstract class with concrete subclasses. The StringBuffer class is not related to them. The principal purpose of a buffer is a “write, then read” cycle. When you run out of data or reach the capacity, it is time to switch to reading.

```
BytesBuffer
CharBuffer
DoubleBuffer
FloatBuffer
IntBuffer
LongBuffer
ShortBuffer
```

A buffer has the following properties:

- Capacity that never changes
- Position at which the next value is read or written
- Limit beyond which reading and writing is meaningless
- Mark for repeating a read/write operation (optional)

```java
ByteBuffer buffer = ByteBuffer.allocate(RECORD_SIZE);
channel.read(buffer);
channel.position(newpos);
buffer.flip(); // prepares buffer for reading after writing
channel.write(buffer);
```
