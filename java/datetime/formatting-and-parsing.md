## Formatting

The DateTimeFormatter class provides three kinds of formatters to print a date/time value:

- Predefined standard formatters (intended for machine-readable timestamps)
- Locale-specific formatters (intended for human readers)
- Formatters with custom patterns

```java
String formatted = DateTimeFormatter.ISO_OFFSET_DATE_TIME.format(apollo11launch);
// 1969-07-16T09:32:00-04:00"

DateTimeFormatter formatter = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.LONG);
String formatted = formatter.format(apollo11launch);
// July 16, 1969 9:32:00 AM EDT
formatted = formatter.withLocale(Locale.FRENCH).format(apollo11launch);
// 16 juillet 1969 09:32:00 EDT

formatter = DateTimeFormatter.ofPattern("E yyyy-MM-dd HH:mm");
```

### Locale-Specific Formatting Styles

| Style  | Date                     | Time           |
| ------ | ------------------------ | -------------- |
| SHORT  | 7/16/69                  | 9:32 AM        |
| MEDIUM | Jul 16, 1969             | 9:32:00 AM     |
| LONG   | July 16, 1969            | 9:32:00 AM EDT |
| FULL   | Wednesday, July 16, 1969 | 9:32:00 AM EDT |

## Parsing

To parse a date/time value from a string, use one of the static parse methods.

```java
LocalDate churchsBirthday = LocalDate.parse("1903-06-14");
ZonedDateTime apollo11launch = ZonedDateTime.parse(
    "1969-07-16 03:32:00-0400",
    DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ssxx")
);
```
