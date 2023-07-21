## Throwing Exceptions

You can only throw objects of subclasses of Throwable. Once a method throws an exception, it does not return to its caller. This means you do not have to worry about cooking up a default return value or an error code.

```java
String readData(Scanner in) throws EOFException {
    while () {
        if (!in.hasNext()) {
            if (n < len) throw new EOFException("hello world");
        }
    }
    return s;
}
```

## Custom Exception Classes

```java
class FileFormatException extends IOException {
    public FileFormatException() {}
    public FileFormatException(String s) {
        super(s);
    }
}
```

## Catching Exceptions

If an exception is not caught anywhere, the program will terminate and print a message to the console.

As a general rule, **you should catch those exceptions that you know how to handle and propagate those that you do not know how to handle**.

When you catch multiple exceptions, the exception variable is implicitly final. You cannot assign a different value in the body of the catch clause.

```java
try {
    // some code
} catch (ExceptionType e) {
    // some code
} catch (FileNotFoundException | UnknownHostException e) {
    e.getMessage();
    e.getClass().getName();
} catch (IOException e) {

}
```

### Rethrowing

You can throw an exception in the catch clause. You should use wrapping technique as it allows you to throw high level exceptions in subsystems without losing the details of the original failure.

```java
try {
    // access database
} catch (SQLException e) {
    Throwable se = new ServletException("database error");
    se.initCause(e);
    throw se;
} catch (ServletException e) {
    Throwable e = se.getCause();
}
```

## Finally

When your code throws an exception, it stops processing the remaining code in your method and exits the method. This is a problem if the method has acquired some local resource, and must be cleaned up.

Following are the possible situations in which the program will execute the finally clause:

- Code executes try block successfully
- code throws an exception and is caught in catch block
- Code throws an exception that is not caught in catch block

You should decouple try/catch and try/finally blocks to make code less confusing.

```java
try {
    try {

    } finally {
        in.close();
    }
} catch (IOException e) {

}
```

## Try-with-Resources Statement

For closing of resources, if the resource belongs to a class that implements the AutoCloseable interface, you do not need to use finally clause. When the block exits normally or when there was an exception, the close() method is called, as if you had used a finally block.

```java
Scanner in = new Scanner(new FileInputStream("/path/to/file", "UTF-8"));
try {
    while (in.hasNext()) {
        System.out.println(in.next());
    }
}
```
