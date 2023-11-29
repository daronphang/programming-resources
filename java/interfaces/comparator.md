## Sorting

The sort() internally calls compare() of the classes it is sorting. The implementation of compare() should return an integer:

- Negative, if the first < second
- Zero, if the first == second
- Positive, if the first > second

### Multiple Fields Custom Sort Function

```java
import java.util.*;

public class CustomSort {
  public static void main(String[] args) {
    List<int[]> dummies = new ArrayList<>() {
      {
        add(new int[] { 1, 2 });
        add(new int[] { 1, 5 });
        add(new int[] { 1, 4 });
        add(new int[] { 7, 3 });
        add(new int[] { 5, 4 });
        add(new int[] { 3, 6 });
        add(new int[] { 5, 10 });
      }
    };
    dummies.sort((int[] x, int[] y) -> {
      if (x[0] == y[0]) {
        return x[1] - y[1];
      }
      return x[0] - y[0];
    });
    for (int[] x : dummies) {
      System.out.println(Arrays.toString(x));
    }
  }
}
```

## Comparator Interface

Comparator is a comparison function, which imposes a total ordering on some collection of objects. Comparators can be passed to sort() to allow precise control over the sort order. A comparator is capable of comparing two objects of the same class.

### Static Methods

The interface has a number of static methods for creating comparators. These methods are intended to be used with lambda expressions or method references. You can also chain methods.

```
comparing()
thenComparing()
reversed()
comparingInt()
thenComparingInt()
comparingLong()
comparingDouble()
```

### Comparing, thenComparing

The thenComparing() lets us set up lexicographical ordering of values by provisioning multiple sort keys in a particular sequence.

```java
static <T,U extends Comparable<? super U>> Comparator<T> comparing(
   Function<? super T,? extends U> keyExtractor
)

static <T,U> Comparator<T> comparing(
    Function<? super T,? extends U> keyExtractor,
    Comparator<? super U> keyComparator
)
```

```java
// sort by last name, first name
Arrays.sort(
    people,
    Comparator\
    .comparing(Person::getLastName))\
    .thenComparing(Person::getFirstName)
```

```java
// specifying name as key to be used in comparing method
Arrays.sort(
    people,
    Comparator.comparing(
        Person::getName,
        (s,t) => Integer.compare(s.length(), t.length()),
    )
)

// sorting 2D arrays by one field
Arrays.sort(
  flowers,
  Comparator.comparingInt((x) -> x[0])
);
```
