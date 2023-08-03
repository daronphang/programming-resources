## RegEx

The input of the matcher is an object of any class that implements the CharSequence interface i.e. String, StringBuilder, CharBuffer.

```java
Pattern pattern = Pattern.compile(patternString);
Pattern pattern = Pattern.compile(
    expression,
    Pattern.CASE_INSENSITIVE + Pattern.UNICODE_CASE
);
Matcher matcher = pattern.matcher(input);
if (matcher.matches()) . . .
```
