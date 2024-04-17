## Logging

When logging messages, Java will autocast the variable to the type as string. If it is a number, Java converts to its string equivalent. If it is an object, Java calls its toString().

Most of the classes in Java library are very **conscientious/diligent about overriding toString()** to give you useful information about the class. This is a real boon/help for debugging. You should make the same effort in your classes.

```java
Logger.getGlobal().info("hello world!");
Logger.getGlobal().info("x=" + x);
logger.setLevel(Level.FINE);
logger.warning(message);
logger.fine(message);
```

### Levels

```
SEVERE
WARNING
INFO
CONFIG
FINE
FINER
FINEST
```

### Logging Signature

The default log record shows the name of the class and method that contain the logging call, as inferred from the call stack. However, if the VM is optimized for execution, accurate call information may not be available.

```java
void logp(Level l, String className, String methodName, String message)

int read(String file, String pattern) {
    logger.entering("com.mycompany.mylib.Reader", "read",
    new Object[] { file, pattern });
    ...
    logger.exiting("com.mycompany.mylib.Reader", "read", count);
    return count;
}
```

### Loggers

In a professional application, you wouldn't want to log all records to a single global logger. Instead, you can define your own loggers.

```java
private static final Logger myLogger = Logger.getLogger("com.mycompany.myapp");
```

### Exceptions

```java
void throwing(String className, String methodName, Throwable t)
void log(Level l, String message, Throwable t)
```

```java
if (. . .) {
    IOException exception = new IOException(". . .");
    logger.throwing("com.mycompany.mylib.Reader", "read", exception);
    throw exception;
}

try {
    ...
}
catch (IOException e) {
    Logger.getLogger("com.mycompany.myapp").log(Level.WARNING, "Reading image", e);
}
```

### Log Manager Configuration

Default config file is located at `jre/lib/logging.properties`. To use another file, set the java.util.logging.config.file property to the file location.

```sh
$ java -Djava.util.logging.config.file=configFile MainClass
```

As the log manager is initialized during VM startup before main executes, if you change the config file in main, you need to call LogManager.readConfiguration() to reinitialize the log manager.

```java
public static void main() {
    file = "/path/to/config";
    System.setProperty("java.util.logging.config.file", file);
    LogManager.readConfiguration();
}
```

```java
if (
    System.getProperty("java.util.logging.config.class") == null &&
    System.getProperty("java.util.logging.config.file") == null
    ) {
    try {
        Logger.getLogger("").setLevel(Level.ALL);
        final int LOG_ROTATION_COUNT = 10;
        Handler handler = new FileHandler("%h/myapp.log", 0, LOG_ROTATION_COUNT);
        Logger.getLogger("").addHandler(handler);
    }
    catch (IOException e) {
        logger.log(Level.SEVERE, "Can't create log file handler", e);
    }
}
```

The logging properties file is processed by the java.util.logging.LogManager
class. It is possible to specify a different log manager by setting the
java.util.logging.manager system property to the name of a subclass. Alternatively,
you can keep the standard log manager and still bypass the initialization from
the logging properties file. Set the java.util.logging.config.class system property
to the name of a class that sets log manager properties in some other way.
