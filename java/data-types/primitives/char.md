## char

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
