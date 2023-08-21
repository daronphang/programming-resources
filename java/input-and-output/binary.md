## Reading and Writing Binary Data

### Input

Use the DataInput interface.

```
readInt
readShort
readLong
readFloat
readDouble
readChar
readBoolean
readUTF
```

### Output

The DataOutput interface defines the methods for writing a number, character, boolean value or string in binary format.

```
writeChars
writeByte
writeInt
writeShort
writeLong
writeFloat
writeDouble
writeChar
writeBoolean
writeUTF            Modified UTF-8 format
```

### Files

To read/write binary data from a file, use DataInputStream/DataOutputStream.

```java
FileInputStream fin = new FileInputStream("employee.dat");
DataInputStream din = new DataInputStream(fin);
double x = din.readDouble();
```

```java
DataOutputStream out = new DataOutputStream(
    new FileOutputStream("employee.dat")
);
```

## Random-Access Files

The RandomAccessFile class lets you read or write data anywhere in a file. Disk files are random-access, but input/output streams that communicate with a network socket are not. You can open a random-access file for reading or reading/writing.

```java
RandomAccessFile in = new RandomAccessFile("employee.dat", "r");
RandomAccessFile inOut = new RandomAccessFile("employee.dat", "rw");
```

A random-access file has a file pointer that indicates the position of the next byte to be read or written.

```
seek()              Set the file pointer to an arbitrary byte position
getFilePointer()    Returns the current position of the file pointer
```

### Example

```java
RandomAccessFile in = new RandomAccessFile("employee.dat", "r");
long n = 3;
in.seek((n - 1) * RECORD_SIZE);
Employee e = new Employee();
e.readData(in);
```
