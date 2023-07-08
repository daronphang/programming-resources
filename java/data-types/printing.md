## Formatting Output

```java
double x = 10000.0 / 3.0;
System.out.print(x); // 3333.3333333333333335
System.out.printf("%8.2f", x);  // 3333.33
System.out.printf("Hello, %s. Next year, you'll be %d", name, age);
System.out.printf("%tc", new Date()); // outdated, use java.time class
```

## Conversions for printf

```
d   Decimal integer                 123
x   Hexadecimal integer             9f
o   Octal integer                   237
f   Fixed-point floating-point      15.9
e   Exponential floating-point      1.59e+01
g   General floating-point          -
a   Hexadecimal floating-point      0x1.fccdp3
s   String                          Hello
c   char
b   boolean
h   Hash code
tx  Date and time
```
