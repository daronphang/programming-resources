## Input/Output Streams

An object from which we can read a sequence of bytes is called an input stream. An object to which we can write a sequence of bytes is called an output stream. These sources and destinations of byte sequences can be files, network connections, and blocks of memory. The abstract classes InputStream and OutputStream form the basis for a hierarchy of input/output (I/O) classes.

Byte-oriented input/output streams are inconvenient for processing information stored in Unicode (uses multiple bytes per character). Hence, a separate hierarchy exists to provide classes for processing Unicode characters that inherit from the abstract **Reader and Writer classes** (not InputStream or OutputStream), and they are based on two-byte char values (UTF-16).

### Relative Directories

All classes in java.io interpret relative path names as starting from the user's working directory.

```java
System.getProperty("user.dir")
```

For portable programs, use the file separator character for the platform on which your program runs. It is available as a constant string java.io.File.separator.

## Reading and Writing Bytes

Both read() and write() block until the byte is read or written, and they operate one byte at a time. The designer of a concrete input stream class overrides them to provide useful functionality.

```java
public class InputStream {
    abstract int read()
}

public class OutputStream {
    abstract void write(int b)
}
```

When you have finished reading or writing, close it by calling close(). This call frees up the OS resources that are limited in supply. It also flushes the buffer used for the output stream; this can be called manually with flush().

Nonetheless, programmers rarely touch them, but use the concrete input/output stream classes derived from the abstract classes.

## Reading and Writing Unicode

The concrete classes inherit from the abstract **Reader and Writer** classes. They both operate one Unicode unit (UTF-16) at a time.

```java
abstract int read()
abstract void write(int c)
```

## Stream Zoo

There are more than 60 different input/output stream types in Java. There are separate hierarchies for classes that process bytes and characters.

```
DataInputStream     Used for reading/writing primitive Java types in binary
DataOutputStream
FileOutputStream
FileInputStream
FilterInputStream
FilterOutputStream
ZipInputStream
ZipOutputStream
```

### Interfaces

- InputStream implements Closeable
- OutputStream implements Closeable and Flushable
- Reader implements Closeable and Readable
- Writer implements Closeable, Flushable and Appendable

## Combining Stream Filters

As Java separates responsibilities, the programmer has to combine the two.

```java
// reading numbers from a file
FileInputStream fin = new FileInputStream("employee.dat");
DataInputStream din = new DataInputStream(fin);
double x = din.readDouble();
```

You can add multiple capabilities by nesting the filters. For instance, input streams are not buffered by default i.e. every call to read() asks the OS to dole out yet another byte. **It is more efficient to request blocks of data instead and store them in a buffer**.

```java
DataInputStream din = new DataInputStream(
    new BufferedInputStream(
        new FileInputStream("employee.dat")
    )
);
```

```java
// reading compressed zip files
ZipInputStream zin = new ZipInputStream(new FileInputStream("employee.zip"));
DataInputStream din = new DataInputStream(zin);
```
