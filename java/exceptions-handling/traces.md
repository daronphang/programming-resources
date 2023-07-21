## Stack Traces

A stack trace is a listing of all pending method calls at a particular point in the execution of a program.

```java
Throwable t  = new Throwable();
StackTraceElement[] frames = t.getStackTrace();
for (StackTraceElement frame : frames) {
    // anaylze frame
}
```
