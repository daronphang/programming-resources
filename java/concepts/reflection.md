## Reflection

The reflection library gives you a rich toolset to write programs that manipulate Java code dynamically. This feature is heavily used in JavaBeans. You can use reflection to:

- Analyze the capabilities of classes at runtime
- Inspect objects at runtime
- Implement generic array manipulation code
- Take advantage of Method objects that work like function pointers in C++

Although reflection is a powerful mechanism, it is of interest to tool builders, and not application programmers.

```java
Employee e;
Class cl = e.getClass();

e.getClass().newInstance();
String s = "java.util.Random";
Object m = Class.forName(s).newInstance();
```

### Analyzing Objects

Reflection lets you look at fields of objects that were not known at compile time.

```java
Employee harry = new Employee("Harry Hacker", 35000, 10, 1, 1989);
Class cl = harry.getClass();
// the class object representing Employee
Field f = cl.getDeclaredField("name");
// the name field of the Employee class
Object v = f.get(harry);
// the value of the name field of the harry object, i.e., the String object "Harry Hacker"
```
