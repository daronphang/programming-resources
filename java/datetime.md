## Date

The Date class represents time in UTC.

```java

```

### LocalDate

No constructor is needed. Instead, use static factory methods that call constructors on your behalf.

```java
LocalDate.now()
LocalDate newYearsEve = LocalDate.of(1999,12,31)
int year = newYearsEve.getYear(); // 1999
int month = newYearsEve.getMonthValue(); // 12
int day = newYearsEve.getDayOfMonth(); // 31
```
