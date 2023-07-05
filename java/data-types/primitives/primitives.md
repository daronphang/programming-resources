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

### char

The char type was originally intended to describe individual characters. However, nowadays, some Unicode characters can be described with one char value, while others require two char values.

Literal values of type char are enclosed in single quotes i.e. 'A' is a char constant with value 65. Values of type char can be expressed as hexadecimal values.

In Java, the char type describes a code unit (16-bit) in the UTF-16 encoding. It has a minimum value of `\u0000` and maximum of `\uffff`. Default size is 2 bytes. **It is strongly recommended not to use the char type** unless you are manipulating UTF-16 code units.

```java
public class example {
    public static void main(String[] args) {
        // integers converted into ASCII equivalent
        char value = 65;
        System.out.println(value);  // A

        String test = "hello world";
        char[] chars = test.toCharArray();
        System.out.println(chars);  // hello world

        char chars1 = '\u0058';
        char chars2 = '\u0059';
        char chars3 = '\u005A';
        System.out.println("Chars: " + chars1 + chars2 + chars3);
        // Chars: XYZ
    }
}
```

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
