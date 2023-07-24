## Handlers

For a record to be logged, its logging level must be above the threshold of both the logger and the handler.

```
java.util.logging.ConsoleHandler.level=INFO
```

```java
Logger logger = Logger.getLogger("com.mycompany.myapp");
logger.setLevel(Level.FINE);

// by default, a logger sends records to its own and parent's handlers
// to not see the record twice, disable useParantHandlers
logger.setUseParentHandlers(false);
Handler handler = new ConsoleHandler();
handler.setLevel(Level.FINE);
logger.addHandler(handler);
```

To send records elsewhere, you can add another handler. The logging API provides two useful handlers: FileHandler and SocketHandler (to a specified host and port).

By default, the records are formatted in XML.

```java
FileHandler handler = new FileHandler();
logger.addHandler(handler);
```

### Stream Handler

The handler buffers the records and only writes them to the stream when the buffer is full. Can override the publish() method to flush the buffer after each record.

```java
class WindowHandler extends StreamHandler {
    public WindowHandler() {
        ...
        final JTextArea output = new JTextArea();
        setOutputStream(
            new OutputStream() {
                public void write(int b) {} // not called
                public void write(byte[] b, int off, int len) {
                    output.append(new String(b, off, len));
                }
        });
    }
    ...
    public void publish(LogRecord record) {
        super.publish(record);
        flush();
    }

}


```

## Configuration Parameters

| Configuration Property                  | Description                                                                                                                                                                           | Default                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| java.util.logging.FileHandler.level     | The handler level                                                                                                                                                                     | Level.ALL                                                              |
| java.util.logging.FileHandler.append    | Controls whether the handler should append to an existing file, or open a new file for each program to run. If multiple applications are using the same log file, should turn this on | false                                                                  |
| java.util.logging.FileHandler.limit     | The maximum number of bytes to write in a file before opening another                                                                                                                 | 0 (no limit) in the FileHandler class, 50000 in the default log config |
| java.util.logging.FileHandler.pattern   | The pattern for the log file name                                                                                                                                                     | %h/java%u.log                                                          |
| java.util.logging.FileHandler.count     | The number of logs in a rotation sequence                                                                                                                                             | 1 (no rotation)                                                        |
| java.util.logging.FileHandler.filter    | The filter class to use                                                                                                                                                               | No filtering                                                           |
| java.util.logging.FileHandler.encoding  | The character encoding to use                                                                                                                                                         | The platform encoding                                                  |
| java.util.logging.FileHandler.formatter | The record formatter                                                                                                                                                                  | java.util.logging.XMLFormatter                                         |

### Pattern Variables

```
%h      The value of the user.home system property
%t      The system temporary directory
%u      A unique number to resolve conflicts
%g      The generation number for rotated logs
%%      The % character
```
