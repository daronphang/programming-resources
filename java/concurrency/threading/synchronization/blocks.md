## Synchronized Blocks

A second mechanism for acquiring the lock is by entering a synchronized block. The lock object is created only to use the lock that every Java object possesses. 

Programmers use this to implement additional atomic operations i.e. client-side locking. However, this is very fragile and generally not recommended.

```java
public class Bank {
    private double[] accounts;

    public void transfer(Vector<Double> accounts, int from, int to, int amount) {
        // private Object lock = new Object();
        synchronized (accounts) // ad-hoc lock on Vector object
        ...
    }
}
```