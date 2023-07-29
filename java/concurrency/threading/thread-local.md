## Thread-Local

Sharing variables between threads will incur risks. However, we can avoid sharing by giving each thread its own instance, using the ThreadLocal helper class.

The first time you call get() in a given thread, the lambda in the constructor gets called. From then on, the get() returns the instance belonging to the current thread.

```java
public static final SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-mm-dd");
String dateStamp = dateFormat.format(new Date());   // not thread safe!
```

```java
// constructing one instance per thread
public static final ThreadLocal <SimpleDateFormat> dateFormat =
    ThreadLocal.withInitial(() -> new SimpleDateFormat("yyyy-mm-dd"));

// to access the actual formatter
String dateStamp = dateFormat.get().format(new Date());
```
