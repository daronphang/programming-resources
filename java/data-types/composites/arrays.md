## array

An array is a data structure that stores a collection of values of the same type. Unlike C++, you can set the size of an array at runtime instead of compile time.

```java
int[] a = new int[100]; // initializes an array of 100 integers of value null
for (int i = 0; i < 100; i++) {
    a[i] = i; // fills the array with numbers 0 to 99
}
// returns a string containing the array elements
System.out.println(Arrays.toString(a)); // "[2, 3, 5, 7, 11, 13]"
```

### Initializers

```java
int[] smallPrimes = { 2, 3, 5, 7, 11, 13 };

new int[] { 17, 19, 23, 29, 31, 37 } // anonymous array

// reinitialize an array without creating a new variable
smallPrimes = new int[] { 17, 19, 23, 29, 31, 37 };
```

### for each

```java
// for (variable: collection) statement

for (int element : a) {
    System.out.println(element);
}
```

### Deep Copy

```java
int[] copiedLuckyNumbers = Arrays.copyOf(luckyNumbers, luckyNumbers.length);
```

### Sorting

Uses QuickSort algorithm.

```java
int[] a = new int[10000];
Arrays.sort(a)
```

## Multidimensional Arrays

Java has no multidimensional arrays, and they are implemented as "arrays of arrays".

```java
double[][] balances;
balances = new double[NYEARS][NRATES];

int[][] magicSquare =
{
{16, 3, 2, 13},
{5, 10, 11, 8},
{9, 6, 7, 12},
{4, 15, 14, 1}
};
```

## ArrayList

When using arrays, once you set the size, you cannot change it easily. However, this can be dealt with using ArrayList, which automatically adjusts its capacity as you add/remove elements.

If the array runs out of space, the array list automatically creates a bigger array and copies all the objects from the smaller to the bigger array.

There is an important distinction between the **capacity and size**. If you allocate an array with 100 entries, then the array has 100 slots, ready for use. An array with a capacity of 100 elements means it has the potential of holding 100 elements, but holds no elements at the beginning.

```java
ArrayList<Employee> staff = new ArrayList<Employee>(100);
staff.ensureCapacity(200);
staff.add(new Employee());
staff.size()
staff.trimToSize() // adjusts the size of memory block to use exactly as much storage space as is required, garbage collector reclaims any excess memory

// to access or change an element, need to use get() and set()
staff.get(i);
staff.set(i, harry);
```

### Operations

```java
ArrayList<Integer> nums = new ArrayList();
nums.add(Integer.valueOf(5));
nums.get(4); // pass index
nums.remove(nums.size() - 1);   // pop
```

### Shallow Copy

```java
ArrayList<Integer> nums = new ArrayList();
ArrayList<Integer> copy = new ArrayList(nums);
```

### Sorting

```java
Collections.sort(nums);
Collections.reverse(nums);
```

## Object Wrappers and Autoboxing

Unfortunately, the type parameter inside the angle brackets cannot be a primitive type. Instead, we can wrap the primitive inside an object i.e. Integer.

When an element of type primitive is added to the array, it will be automatically translated to the object type. This is called **autoboxing**. Boxing and unboxing is a courtesy of the compiler, which inserts the necessary calls when it generates the bytecodes of a class. The VM simply executes those bytecodes.

```java
ArrayList<Integer> list = new ArrayList<>();

list.add(3); // auto translated to as below
list.add(Integer.valueOf(3));   // boxing

int n = list.get(i);
int n = list.get(i).intValue(); // unboxing
```
