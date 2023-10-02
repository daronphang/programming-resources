## synchronized

Lock and Condition interfaces give programmers a high degree of control over locking. However, in most situations, you don't need that control. You can use a mechanism that is built into the Java language.

Every object in Java has an intrinsic lock, and that lock has an intrinsic condition. If a method is declared with the synchronized keyword, the object's lock protects the entire method. The lock manages the threads that try to enter a synchronized keyword, and the condition manages the threads that have called wait().

If a **static method** is declared as synchronized, it acquires the intrinsic lock of the associated **class object**.

The intrinsic locks and conditions have some limitations:
- You cannot interrupt a thread that is trying to acquire a lock
- You cannot specify a timeout when trying to acquire a lock
- Having a single condition per lock can be inefficient


```java
public synchronized void method(){
    // body
}

// equivalent
public void method() {
    this.intrinsicLock.lock();
    try {
        // body
    } finally {
        this.intrinsicLock.unlock();
    }
}
```

### wait(), notifyAll()

The wait() adds a thread to the wait set, and notify()/notifyAll() unblock waiting threads.

``` 
wait()          intrinsicCondition.await()
notifyall()     intrinsicCondition.signalAll()
```
```java
class Bank {
    private double[] accounts;
    public synchronized void transfer(int from, int to, int amount) {
        while (accounts[from] < amount) {
            wait();
        }
        accounts[from] -= amount;
        accounts[to] += amount;
        notifyAll();
    }
}
```