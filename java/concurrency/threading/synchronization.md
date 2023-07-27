## Synchronization

In multithreaded applications, two or more threads may need to share and access to the same data but may result in a **race condition** which can cause unexpected bugs and make tests brittle and non-deterministic. To avoid corruption of shared data, you can synchronize the access.

## Lock

### ReentrantLock

When other threads call lock, they are deactivated until the first thread unlocks the lock object. when using locks, you cannot use try-with-resources.

```java
private Lock myLock = new ReentrantLock();

myLock.lock();
try {
    // some code to modify a resource
} finally {
    myLock.unlock();
}
```

The lock is called reentrant because **a thread can repeatedly acquire a lock that it already owns**. The lock has a hold count that keeps track of the nested calls to lock(). The thread has to call unlock() for every call to lock in order to relinquish the lock. Because of this feature, code protected by a lock can call another method that uses the same locks i.e. during nested calls.

```java
public Lock myLock = new ReentrantLock();
public static void hello() {
    try {
        myLock.lock();
        world();
    } finally {
        myLock.unlock();
    }
}

public static void world() {
    try{
        myLock.lock(); // works
    } finally {
        myLock.unlock(); // need to unlock twice before it is fully unlocked
    }
}
```

## Condition

Often, a thread enters a critical section only to discover that it cannot proceed until a condition is fulfilled. Use a condition object to manage threads that have acquired a lock but cannot do useful work. 

You cannot use code with if statement as it is entirely possible that the current thread will be deactivated between the successful outcome of the test and the subsequent call.

```java
if (bank.getBalance(from) >= amount) {
    bank.transfer(from, to, amount); // this may be prempted and pause while another thread executes
}
```

A lock object can have one or more associated condition objects. You obtain a condition object with newCondition(). It is customary to give each condition object a name that evokes the condition that it represents.

```java
class Bank {
    private Condition sufficientFunds;

    public Bank() {
        sufficientFunds = bankLock.newCondition();
    }
}
```

If the condition is not met, it calls **await()**. The current thread will be deactivated and gives up the lock. When the method is called, the thread enters a **wait set** for that condition. It stays deactivated until another thread has called **signalAll()** on the same condition. 

The signalAll() call reactivates all threads waiting for the condition. The method signals to the waiting threads that it may be fulfilled at this time and that it is worth checking for the condition again. When the threads are removed from the wait set, they are again runnable and the scheduler will eventually activate them again. As soon as the lock is available, one of them will acquire the lock and **continue where it left off**, returning from the call to await().

**It is crucially important that some other thread calls signalAll() eventually**. When a thread calls wait(), it has no way of reactivating itself. If none of them bother to reactivate, it can lead to **deadlock** situations. The rule of thumb to call signalAll() is when the state of an object changes that might be advantageous to waiting threads.

Another method signal() unblocks only a single thread from the wait set, but chosen at random. Though it is more efficient than unblocking all threads, it can still lead to system deadlocks.

```java
public void transfer(int from, int to, double amount) throws InterruptedException {
    bankLock.lock();
    try {
        while (accounts[from] < amount) sufficientFunds.await();
        accounts[from] -= amount;
        accounts[to] += amount;
        sufficientFunds.signalAll();
    }
    finally {
        bankLock.unlock();
    }
}
```