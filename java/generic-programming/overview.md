## Generic Programming

Generic classes are desirable as they let you write code that is safer and easier to read than code littered with Object variables and casts i.e. they can be reused for objects of many different types. They are particularly useful for collection classes, such as ArrayList.

### Before Generic Classes

Generic programming was achieved with inheritance. However, this approach has problems:

- You need to cast whenever you retrieve a value
- There is no error checking

```java
public class ArrayList {
    private Object[] elementData;
    ...
    public Object get(int i) { . . . }
    public void add(Object o) { . . . }
}

ArrayList files = new ArrayList();
// problems
String filename = (String) files.get(0);
files.add(new File(". . ."));
```

### Who Wants to be a Generic Programmer

Application programmers probably won't write lots of generic code as the JDK developers have done the heavy lifting and supplied type parameters for all the collection classes.
