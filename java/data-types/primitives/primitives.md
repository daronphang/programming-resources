## Primitives

Java is a strongly typed language and every variable must have a declared type. There are eight primitive types:

1. int (most practical)
2. short
3. long
4. byte
5. char
6. boolean
7. float (has suffix F of f i.e. 3.14F)
8. double (twice the precision of float type)

All floating-point computations follow the IEEE 754 specification. There are three special floating-point values to denote overflows and errors:

- Double.POSITIVE_INFINITY
- Double.NEGATIVE_INFINITY
- Double.NaN

## Constants

Use the keyword final to denote a constant. It indicates that you can assign to the variable once, and then its value is set once and for all. It is customary to name constants in all uppercase.

```java
final double CM_PER_INCH = 2.54;
```

## Casts

Conversions in which loss of information is possible are done by means of casts. The syntax is to give the target type in parentheses, followed by the variable name.

```java
double x = 9.997;
int nx = (int) x;
```

## Bitwise Operators

When working with any of the integer types, you have operators that can work directly with the bits that make up the integers.

When applied to boolean values, the & and | yield a boolean value. These operators are similar to && and || operators, but are not evaluated in 'short circuit' fashion. Instead, both arguments are evaluated before the result is computed.

```
& (and)
| (or)
^ (xor)
~ (not)
```
