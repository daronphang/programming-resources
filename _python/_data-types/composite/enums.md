## Enumerations

Data type that allows you to create sets of named constants, which are considered members of the containing enum. You can access the members through the enumeration itself.

Examples include days of the week, seasons of the year, HTTP status codes, etc.

Each member must have a value, which needs to be a constant. Often, the values mapped to members are consecutive integers.

Python doesn't have a dedicated syntax for enums, but has an enum module that supports enumerations through the Enum class.

### Benefits

- Allows for convenient grouping of related constants in a sort of namespace
- Allows for additional behavior with custom methods that operate on enum
- Provides quick and flexible access to enum members
- Enable direct iteration over members, including their names and values
- Ensuring constant values can't be changed during runtime
- Provides a single source of truth and consistency throughout the code

### Enum Features

- Cannot be instantiated.
- Cannot be subclassed.
- Are iterable, returning their members in a sequence.
- Provide hashable members that can be used as dictionary keys.
- Do not allow member reassignments.

## Example

```py
from enum import Enum

class Day(Enum):
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7

class Season(Enum):
WINTER, SPRING, SUMMER, FALL = range(1, 5)


class Grade(Enum):
    A = 90
    B = 80
    C = 70
    F = 0


class Size(Enum):
    S = "small"
    M = "medium"
    L = "large"
```

```py
Day.MONDAY = 0  # error, cannot reassign members as they are constants

print(Day.MONDAY)
print(Day('MONDAY'))
print(Day['MONDAY'])

for day in Day:
    print(f'{day.name}, {day.value}')
```
