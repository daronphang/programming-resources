## Collections

As is common with modern data structure libraries, the Java collection library separates interfaces and implementations.

In the API documentation, you will find a set of classes whose name begins with Abstract i.e. AbstractQueue. These classes are intended for library implementors. In the event that you want to implement your own queue class, you will find it easier to extend AbstractQueue than to implement all the methods of the Queue interface.

### Collection Interface

The Collection interface is the fundamental interface for collection classes. It has two fundamental methods: add() and iterator().

```java
public interface Collection<E> {
    boolean add(E element);
    Iterator<E> iterator();
    int size()
    boolean isEmpty()
    boolean contains(Object obj)
    boolean containsAll(Collection<?> c)
    boolean equals(Object other)
    boolean addAll(Collection<? extends E> from)
    boolean remove(Object obj)
    boolean removeAll(Collection<?> c)
    void clear()
    boolean retainAll(Collection<?> c)
    Object[] toArray()
    <T> T[] toArray(T[] arrayToFill)
}
```

To make life easier for implementors, the library supplies a class AbstractCollection taht leaves the fundamental methods size() and iterator() abstract but implements the routine methods in terms of them.

```java
public abstract class AbstractCollection<E> implements Collection<E> {
    ...
    public abstract Iterator<E> iterator();
    public boolean contains(Object obj) {
        for (E element : this) // calls iterator()
            if (element.equals(obj)) return true;
            return false;
    }
    ...
}
```

### Concrete Collections

| Collection Type | Description                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------- |
| ArrayList       | An indexed sequence that grows and shrinks dynamically                                         |
| LinkedList      | An ordered sequence that allows efficient insertion and removal at any location                |
| ArrayDeque      | A double-ended queue that is implemented as a circular array                                   |
| HashSet         | An unordered collection that rejects duplicates                                                |
| TreeSet         | A sorted set                                                                                   |
| EnumSet         | A set of enumerated type values                                                                |
| LinkedHashSet   | A set that remembers the order in which elements were inserted                                 |
| PriorityQueue   | A collection that allows efficient removal of the smallest element                             |
| HashMap         | A data structure that stores key/value associations                                            |
| TreeMap         | A map in which the keys are sorted                                                             |
| EnumMap         | A map in which the keys belong to an enumerated type                                           |
| LinkedHashMap   | A map that remembers the order in which entries were added                                     |
| WeakHashMap     | A map with values that can be reclaimed by the garbage collector if they are no used elsewhere |
| IdentityHashMap | A map with keys that are compared by ==, not equals                                            |
