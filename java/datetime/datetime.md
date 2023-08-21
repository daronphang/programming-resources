## Date

The Date class represents time in UTC.

## Local Date

No constructor is needed. Instead, use static factory methods that call constructors on your behalf.

The difference between two local dates is a Period, whereas for two time instants is a Duration.

```java
LocalDate today = LocalDate.now();
LocalDate newYearsEve = LocalDate.of(1999,12,31);
int year = newYearsEve.getYear(); // 1999
int month = newYearsEve.getMonthValue(); // 12
int day = newYearsEve.getDayOfMonth(); // 31
LocalDate programmersDay = LocalDate.of(2014, 1, 1).plusDays(255);
independenceDay.until(christmas, ChronoUnit.DAYS) // 174 days
```

### Methods

|                                                                             |                                                |
| --------------------------------------------------------------------------- | ---------------------------------------------- |
|                                                                             |                                                |
| Method                                                                      | Description                                    |
| now, of                                                                     | Constructs a LocalDate                         |
| plusDays, plusWeeks, plusMonths, plusYears                                  | Adds to LocalDate                              |
| minusDays, minusWeeks, minusMonths, minusYears                              | Subtracts from LocalDate                       |
| plus, minus                                                                 | Adds/subtracts a Duration or Period            |
| withDayOfMonth, withDayOfYear, withMonth, withYear                          | Returns a new LocalDate with the value changed |
| getDayOfMonth, getDayOfYear, getDayOfWeek, getMonth, getMonthValue, getYear |                                                |
| until                                                                       | Gets the Period between two dates              |
| isBefore, isAfter                                                           | Compares this LocalDate with another           |
| isLeapYear                                                                  | Returns true                                   |
|                                                                             |

## Zoned Date

Should not use zoned time unless you really want to represent absolute time instances.

## Local Time

```java
LocalTime rightNow = LocalTime.now();
LocalTime bedtime = LocalTime.of(22, 30); // or LocalTime.of(22, 30, 0)
```

## Local DateTime

The LocalDateTime class represents a date and time. However, if you need to make calculations that span the daylight savings time, or if you need to deal with users in different time zones, you should use ZonedDateTime class.

## Zoned Time

The zoned datetime gives a specific instant in time. Given a timezone ID, the static method of ZoneId.of(id) yields a ZoneId object. You can use that object to turn a LocalDateTime object into a ZoneDateTime object.

```java
ZoneId zoneId = ZoneId.of("America/New_York");
LocalDateTime today = LocalDateTime.now();
ZonedDateTime zonedt = today.atZone(zoneId);

ZonedDateTime apollo11launch = ZonedDateTime.of(
    1969,
    7,
    16,
    9,
    32,
    0,
    0,
    ZoneId.of("America/New_York")
);
// 1969-07-16T09:32-04:00[America/New_York]
```

### Daylight Savings

When adjusting a date across daylight savings time boundaries, use Period class.

```java
ZonedDateTime nextMeeting = meeting.plus(Duration.ofDays(7));
// Caution! Won't work with daylight savings time
ZonedDateTime nextMeeting = meeting.plus(Period.ofDays(7)); // OK
```
