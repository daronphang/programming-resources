## while

A while loop tests at the top. Hence, the code in the block might never be executed. If you want to make sure a block is executed at least once, you need to move the test to the bottom using do/while loop.

```java
do {
    balance += payment;
    double interest = balance * interestRate / 100;
    balance += interest;
    year++;
    // print current balance
    ...
    // ask if ready to retire and get input
    ...
    break;
    continue;
}
while (input.equals("N"));
```

## for

```java
for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}
```

```java
for (int element : a) {
    System.out.println(element);
}
```
