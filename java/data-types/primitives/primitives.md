## Primitives

Java is a strongly typed language and every variable must have a declared type. There are eight primitive types and they are **stored directly on the stack**:

| Type    | Size (bits) | Minimum | Maximum               |
| ------- | ----------- | ------- | --------------------- |
| byte    | 8           | -2^7    | 2^7 - 1               |
| short   | 16          | -2^15   | 2^15 - 1              |
| int     | 32          | -2^31   | 2^31 - 1              |
| long    | 64          | -2^63   | 2^63 - 1              |
| float   | 32          | -2^-149 | (2 - 2^-23) \* 2^127  |
| double  | 64          | -2^1074 | (2 - 2^-52) \* 2^1023 |
| char    | 16          | 0       | 2^16 - 1              |
| boolean | 1           | -       | -                     |

The most practical is int. Float has suffix F or f i.e. 3.14F. Double has twice the precision of float.

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
