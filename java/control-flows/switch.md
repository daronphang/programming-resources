## switch

If you don't add a break at the end of an alternative, multiple alternatives may be triggered. Execution falls through to the next alternative.

A case label can be a constant expression of type (char, byte, short, int), an enumerated constant, or a string literal.

```java
Scanner in = new Scanner(System.in);
System.out.print("Select an option (1, 2, 3, 4) ");
int choice = in.nextInt();
switch (choice) {
    case 1:
    ...
    break;
    case 2:
    ...
    break;
    case 3:
    ...
    break;
    case 4:
    ...
    break;
    default:
    // bad input
    ...
    break;
}
```
