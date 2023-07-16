## Strings

Java strings are sequences of Unicode characters. Java does not have a built-in string type. Instead, the standard library contains a predefined class called String.

When testing for equality, use equals() method.

```java
String e = "hello";
e.equals(t);
"hello".equals("hello")

if (e.length() == 0 || e.equals("") || e == null) {
    // do something
    break
}
```

### Building Strings

It would be inefficient to use string concatenation as a new String object is constructed which is time consuming and wastes memory. The stringBuilder class avoids this problem.

```java
StringBuilder builder = new StringBuilder();
builder.append(ch); // appends a char
builder.append(str); // appends a str
String completed = builder.toString();
```
