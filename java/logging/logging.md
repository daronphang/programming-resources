## Logging

```java
Logger.getGlobal().info("hello world!");
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

## Advanced Logging

In a professional application, you wouldn't want to log all records to a single global logger. Instead, you can define your own loggers.

```java
private static final Logger myLogger = Logger.getLogger("com.mycompany.myapp");
```
