## Stack Traces

A stack trace is a listing of all pending method calls at a particular point in the execution of a program. **Stack traces are displayed on System.err.**

```java
Throwable t  = new Throwable();
t.printStackTrace();
StackTraceElement[] frames = t.getStackTrace();
for (StackTraceElement frame : frames) {
    // anaylze frame
}
```

If you do not want to catch an exception to generate a stack trace, insert the statement:

```java
Thread.dumpStack();
```

### Displaying Stack Traces

Need to capture it into a string.

```java
StringWriter out = new StringWriter();
new Throwable().printStackTrace(new PrintWriter(out));
String description = out.toString();
```

### Trapping Program Errors in File

```sh
$ java MyProgram 2> errors.txt  # capture error stream
$ java MyProgram 1> errors.txt 2>&1 # capture System.err and System.out in same file
```

### Appending Stack Traces to Log File

Having the stack traces of uncaught exceptions show up in System.err is not ideal. It will be conflusing to end users if they happen to see them, and they are not available for diagnostic purposes when you need them. A better approach is to log them to a file.

```java
Thread.setDefaultUncaughtExceptionHandler(
    new Thread.UncaughtExceptionHandler() {
        public void uncaughtException(Thread t, Throwable e) {
            // save information in log file
        };
    }
);
```
