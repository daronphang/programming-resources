## Bitmask

Mask in Bitmask means hiding something. Bitmasking is the act of applying a mask over a value to keep, change or modify a piece of given information. A mask determines which bits to take and which bits to clear off a binary number.

Bitmasking allows us to store multiple values inside one numerical variable. They are used when you want to **encode multiple layers of information in a single number**.

Bitmask provides an efficient way to manipulate a small set of Booleans (0 or 1) that is stored as a 32/64-bit signed integer in base-10. Binary is read from right to left.

By using bitwise operations, each bit of the integer can be checked, turned on or turned off easily and quickly. Bitmasking can be used to mask a value to represent the subsets of a set using various bitwise operations.

### Constraints

When using bitmask to solve a problem, it must have **small constraints**, as solutions take up exponential time and memory.

### Representing subsets

Given a set S consisting of N items numbered from 1 to N, given the ith bit in the mask:

- If set or equal to 1, the ith item is included in the subset
- If unset or equal to 0, the ith item is not included in the subset

```
N = 7
1010110 -> subset includes {2,3,5,7} items (1-based indexing)
```

A set of size N can have a maximum of **2^N** subsets.

```
N = 2
[00,01,10,11]
```

## Operations

### AND Operator &

The bitwise & of two bits is equal to 1 if the corresponding bits of both the operands are equal to 1. If either bit of an operand is 0, the result is 0.

```
12 = 00001100
25 = 00011001

Bit Operation of 12 and 25:
00001100
&
00011001
= 00001000 = 8
```

### OR Operator |

The bitwise of two operands is equal to 1 if at least one corresponding bit of both the operands is equal to 1.

```
12 = 00001100
25 = 00011001

Bit Operation of 12 and 25:
00001100
|
00011001
= 00011101 = 29
```

### Left Shift Operator <<

The left shift operator shifts **all the bits** of a particular number left by a specified number of bits. All the bits vacated by the left shift operation are filled with 0.

```
212 = 11010100
212 << 0 = 11010100
212 << 1 = 110101000
212 << 4 = 110101000000 = 3392
```

### Power of 2 using << operator

One useful application of the left-shift operator is to find the power of 2. If we left-shift 1 by k places we will get the result 2^k in decimal.

```
1 << 2 = 2
1 << 3 = 8
```

### Setting the kth bit of a number

```
b | (1 << i)

i = 0
01010 | 00001 = 01011
```

### Unsetting the kth bit of a number

```
b &! (1 << i)

i = 1
01010 & !00010 = 01000
```

### Checking if ith bit is set

If a non zero integer is returned, the ith bit is set.

```
b & (1 << i)

i = 3
01010 & 01000 = 01000
```
