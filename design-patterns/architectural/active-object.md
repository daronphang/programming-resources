## Active Object Pattern

The Active Object pattern is a concurrency design pattern that decouples method execution from method invocation in multi-threaded applications. When a thread in a multithreaded program waits for an event, it usually invokes some operating system call that blocks the thread until the event has occurred. It is particularly useful for managing concurrency in systems that use asynchronous method calls and require a high level of responsiveness.

The pattern allows objects to process requests concurrently, with each request being encapsulated in a separate command object and executed by a dedicated thread. Each object has its own thread of control, and interactions between objects are managed through a scheduler.

A nice example could be a restaurant kitchen, where chefs (active objects) work independently, and orders are placed asynchronously without blocking the entire kitchen. Each chef operates on their set of tasks without directly coordinating with others.

### When to use?

The active object pattern is typically used when:

- You want to decouple method invocation from execution to improve responsiveness and simplify concurrency management
- You need to manage concurrency in a system with asynchronous method calls
- You want to provide a simple interface for clients while hiding the complexity of concurrent execution

### Implementation

1. Define an interface for the active object that includes the methods to be executed asynchronously
2. Create a command object for each method in the interface, encapsulating the method call and its arguments
3. Implement a scheduler that maintains a queue of command objects and manages their execution by a separate thread or a pool of threads.
4. Implement the active object by providing an implementation of the interface, which submits command objects to the scheduler for execution

```java
// Active Object interface
interface ActiveObject {
    Future<Integer> calculateSum(int a, int b);
}

// Command object
class SumCommand implements Callable<Integer> {
    private int a;
    private int b;

    public SumCommand(int a, int b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public Integer call() {
        return a + b;
    }
}

// Active Object implementation
class ActiveObjectImpl implements ActiveObject {
    private final ExecutorService executor = Executors.newSingleThreadExecutor();

    @Override
    public Future<Integer> calculateSum(int a, int b) {
        return executor.submit(new SumCommand(a, b));
    }
}

// Client code
public class Client {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ActiveObject activeObject = new ActiveObjectImpl();
        Future<Integer> result = activeObject.calculateSum(1, 2);
        // Perform other tasks...
        System.out.println("Sum: " + result.get()); // Outputs: Sum: 3
    }
}
```

```java
class Kitchen
{
    private Queue<string> orderQueue = new Queue<string>();
    private object lockObject = new object();

    public void PlaceOrder(string item)
    {
        lock (lockObject)
        {
            orderQueue.Enqueue(item);
            Console.WriteLine($"Order placed: {item}");
        }
        // Schedule the order processing asynchronously
        Task.Run(() => ProcessOrders());
    }

    private void ProcessOrders()
    {
        string order;
        lock (lockObject)
        {
            // Dequeue the next order if available
            order = orderQueue.Count > 0 ? orderQueue.Dequeue() : null;
        }
        if (order != null)
        {
            // Simulate order processing time
            Thread.Sleep(2000);
            Console.WriteLine($"Order completed: {order}");
        }
    }
}

internal class Active_Object_Pattern_sample_1
{
    static void Main()
    {
        Kitchen kitchen = new Kitchen();

        // Place orders asynchronously
        Task.Run(() => kitchen.PlaceOrder("Pasta"));
        Task.Run(() => kitchen.PlaceOrder("Burger"));
        Task.Run(() => kitchen.PlaceOrder("Salad"));
        Console.ReadLine(); // Keep the application running for the asynchronous orders to complete
    }
}
```
