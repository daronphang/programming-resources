## Bits, Bytes (Base2)

A bit is a single binary digit that is atomic and is smallest unit of storage, either 0 or 1. It is the most basic system needed for all logical operations.

**Byte is the basic unit of information in computer storage and processing**. Data is typically stored in a disk/in-memory in bytes. A single byte has 8 bits (2^8) and hence, can have 256 different combinations of binary i.e. 256 possible values.

The string of bits making up a byte is processed as a unit by a computer i.e. bytes are smallest operable units of storage in computer technology.

## Decimal (Base10)

Number system that is represented with 10 unique digits.

## Hexadecimal (Base16)

Uses a set of 16 unique digits. Uses standard 0-9 and A-F. Provides a human-friendly representation of binary-coded values. Each hexadecimal digit represents 4 bits.

Hexadecimals are prefixed with "0x" to indicate that the number is in hexadecimal rather than in some other base.

```
Dec     Hex     Binary
0       0       0
2       2       10
10      A       1010
15      F       1111
17      11      10001
37      25      100101
```

### The need for hexadecimals

In computing systems, the binary string equivalents of large decimal numbers can become quite long. This problem can be overcomed by arranging the binary numbers into groups of 4 bits. Hence, it can be used to represent large numbers with fewer digits.

The reason programmers like to use hexadecimal notation is because it is convenient. As each hexadecimal digit corresponds to 4 bits, it fits nicely into 8-bit bytes i.e. two hex digits can represent every value of a byte.

### Examples

1. Given binary 1011010101100001
2. Split binary into groups of four: 1011, 0101, 0110, 0001
3. Replace each set with a hexadecimal: B, 5, 6, 1
4. In hexadecimal is 0xB561
