## Algorithms

Generic collection interfaces have a great advantage: you only need to implement your algorithms once.

To find the max of different classes, you need to implement the following:

```java
static <T extends Coparable> T max (T[] v) {}
static <T extends Comparable> T max (ArrayList<T> v) {}
static <T extends Comparable> T max (LinkedList<T> v)
```

Using the Collection interface:

```java
public static <T extends Comparable> T max(Collection<T> c) {
    if (c.isEmpty()) throw new NoSuchElementException();
    Iterator<T> iter = c.iterator();
    T largest = iter.next();
    while (iter.hasNext()) {
        T next = iter.next();
        if (largest.compareto(next) < 0) largest = next; 
    }
    return largest;
}
```

## Custom Algorithms

### Writing

If you want to write your own algorithms, you should work with interfaces, not concrete implementations as you will constrain the caller of your method to the type.

```java
void fillMenu(Jmenu menu, ArrayList<JMenuItem> items) {
    for (JMenuItem item : items) {
        menu.add(item);
    }
}
```
```java
void fillMenu(JMenu menu, Colelction<JMenuItem> items) 
```

### Returning Collections

If you want to return a collection, you also want to return an interface instead of a class as you can then change your mind and reimplement the method later with a different collection.

```java
List<JMenuItem> getAllItems(JMenu menu) {
    List<JMenuItem> items = new ArrayList<>();
    for (int i = 0; i < menu.getItemCount(); i++) {
        items.add(menu.getItem(i));
    }
    return items;
}
```

```java
List<JMenuItem> getAllItems(final JMenu menu) {
    return new AbstractList<>() {
        public JMenuItem get(int i) {
            return menu.getItem(i);
        }

        public int size() {
            return menu.getItemCount();
        }
    }
}
```