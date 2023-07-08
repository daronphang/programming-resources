## array

An array is a data structure that stores a collection of values of the same type.

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

Java has no multidimensional arrays, and they are fked as "arrays of arrays".

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
