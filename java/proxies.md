## Proxies

You can use a proxy to create, at runtime, new classes that implement a given set of interfaces. Proxies are only necessary when you don't know at compile time which interfaces you need to implement.

The proxy class has the following methods:

- All methods required by the specified interfaces
- All methods defined in the Object class

However, you cannot define new code for these methods at runtime. Instead, you must supply an invocation handler. An invocation handler is an object of any class that implements the InvocationHandler interface. The interface has a single method:

```java
Object invoke(Object proxy, Method method, Object[] args)
```

Whenever a method is called on the proxy object, the invoke method of the invocation handler gets called, with the Method object and parameters of the original call.

### Creating Proxies

The newProxyInstance method of the Proxy class has three parameters:

- Class loader
- An array of Class objects, one for each interface to be implemented
- An invocation handler

```java
class TraceHandler implements InvocationHandler {
    private Object target;
    public TraceHandler(Object t) {
        target = t;
    }
    public Object invoke(Object proxy, Method m, Object[] args) throws Throwable {
        // prints the name and parameters of the method
        System.out.print(target);
        System.out.print(m.getName());
        ...
        // calls the actual method with the wrapped object as the implicit parameter
        return m.invoke(target, args);
    }
}

public class ProxyTest {
    public static void main() {
        Object[] elements = new Object[1000];

        for (int i = 0; i < elements.length; i++) {
            Integer value = i + 1;
            InvocationHandler handler = new TraceHandler(value);
            Class[] interfaces = new Class[] { Comparable.class };
            Object proxy = Proxy.newProxyInstance(null, interfaces, handler);
            elements[i] = proxy;
        }

        Integer key = new Random().nextInt(elements.length) + 1;
        int result = Arrays.binarySearch(elements, key);
        if (result >= 0) System.out.println(elements[result]);
    }
}
// trace
// 500.compareTo(288)
// 250.compareTo(288)
// 375.compareTo(288)
// 288.toString()
```

### Properties

- All proxy classes extend the class Proxy
- A proxy class has only one instance field, the invocation handler
- All proxy classes override the toString, equals, and hashCode methods of the Object class
- Names of proxy classes are not defined
