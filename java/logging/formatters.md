## Formatters

The ConsoleHandler and FileHandler classes emit the log records in text and XML formats. Need to call setFormatter() to install the formatter into the handler.

In format(), may want to call formatMessage().

```java
class CustomFormatter extends Formatter {
    String format(LogRecord record){
        String formatMessage(LogRecord record) {}
    }
}
```

Many file formats require a head and tail parts that surround the formatted records.

```java
String getHead(Handler h) {}
String getTail(Handler h) {}
```
