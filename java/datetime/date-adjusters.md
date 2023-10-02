## Date Adjusters

The TemporalAdjusters class provides a number of static methods for common adjustments. The with() returns a new LocalDate object without modifying the original.

| Method                                                                                            | Description                                           |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| next(weekday), previous(weekday)                                                                  | Next or previous date that falls on the given weekday |
| nextOrSame(weekday), previousOrSame(weekday)                                                      | Starting from the given date                          |
| dayOfWeekInMonth(n, weekday)                                                                      | The nth weekday in the month                          |
| lastInMonth(weekday)                                                                              | The last weekday in the month                         |
| firstDayOfMonth(), firstDayOfNextMonth(), firstDayOfNextYear(), lastDayOfMonth(), lastDayOfYear() |                                                       |

### Custom

You can also make ur own adjuster by implementing the TemporalAdjuster interface.

```java
TemporalAdjuster NEXT_WORKDAY = w -> {
    LocalDate result = (LocalDate) w;
    do {
        result = result.plusDays(1);
    }
    while (result.getDayOfWeek().getValue() >= 6);
    return result;
};

LocalDate backToWork = today.with(NEXT_WORKDAY);
```
