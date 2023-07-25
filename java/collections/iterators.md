## Iterator

### Iterator Interface

The lookup and position change are tightly coupled. The only way to look up an element is to call next, and that lookup advances the position.

```java
public interface Iterator<E> {
    E next();
    boolean hasNext();
    void remove();
    default void forEachRemaining(Consumer<? super E> action);
}
```

```java
Collection<String> c = . . .;
Iterator<String> iter = c.iterator();
while (iter.hasNext()) {
    String element = iter.next();
    do something with element
}
```

The remove method removes the element that was returned by the last call to next. There is a dependency between calls to next() and remove(). **It is illegal to call remove() if it wasn't preceded by a call to next()**.

```java
Iterator<String> it = c.iterator();
it.next(); // skip over the first element
it.remove(); // now remove it
```

### Interable Interface

The Collection interface extends the Iterable interface.

```java
public interface Iterable<E> {
    Iterator<E> iterator();
    ...
}
```

### for each

Compiler translates for each into a loop with an iterator. The 'for each' loop works with any object that implements the Iterable interface.

The order in which the elements are visited depends on the collection type. For an ArrayList, the iterator starts at index 0. For HashSet, you will get them in a random order.

```java
for (String element : c) {
    do something with element
}
```

### forEachRemaining

As of Java SE8, you can call forEachRemaining() with a lambda expression that consumes an element.

```java
iterator.forEachRemaining(element -> do something with element);
```
