## Final Classes

Final classes are those that cannot be extended.

```java
public final class Executive extends Manager {}
```

## Final Methods

You can make a specific method in a class final. If you do this, no subclass can override that method.

```java

public class Employee {
    public final String getName(){}
}
```

## Reasons for Using Final

One reason to make a method or class final is to make sure its semantics cannot be changed in a subclass.

Another reason is to avoid the overhead of dynamic binding. If a method is not overriden, and it is short, then a compiler can optimize the method call away: this process is called **inlining** i.e. the call e.getName() will be replaced with field acess e.name. CPUs hate branching as it interferes with their strategy of prefetching instructions while processing the current one. If the method can be overriden, the CPU can inline it as it has no way of knowing what the overriding code may do.

Fortunately, the JIT compiler in the VM can do a better job than a traditional compiler. It knows exactly which classes extend a given class, and it can check whether any class actually overrides a given method. If a method is short, frequently called, and not actually overridden, the JIT compiler can inline the method.
