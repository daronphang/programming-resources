## Enumerations

Data type that allows you to create sets of named constants, which are considered members of the containing enum. You can access the members through the enumeration itself.

Examples include days of the week, seasons of the year, HTTP status codes, etc.

Each member must have a value, which needs to be a constant. Often, the values mapped to members are consecutive integers.

Python doesn't have a dedicated syntax for enums, but has an enum module that supports enumerations through the Enum class.

### Benefits

- Helps to express characteristics of a category/list by modelling
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

### Enumerations

```
Enum
IntEnum     Provide ordered comparisons of members
IntFlag     Similar to IntEnum and supports bitwise operations i.e. |
Flag        Supports bitwise operations but does not inherit from int
```

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

print(Day.MONDAY)       # Day.MONDAY, an object of type <enum 'Day'>
print(type(Day.MONDAY)) # <enum 'Day'>
print(Day('MONDAY'))    # Day.MONDAY
print(Day['MONDAY'])    # Day.MONDAY
print(Day.MONDAY.value) # 1

for day in Day:
    print(f'{day.name}, {day.value}')
```

```py
from enum import Enum

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"

def move(direction):

    # Type checking
    if not isinstance(direction, Direction):
        raise TypeError('direction must be an instance of Direction Enum')

    print direction.value

move(Direction.LEFT)    # left
move("right")   # TypeError: direction must be an instance of Direction Enum
```

### Checking Members

```py
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    really_blue = 3

    @classmethod
    def has_member(cls, key):
        return key in cls.__members__
```

### Aliases

```py
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    really_blue = 3

print(Color.blue is Color.really_blue)  # True
```

### Comparisons

Use is keyword as members are singleton instance objects of the enumeration class. Equality works, but testing by identity is optimal.

```py
print(Color.red is Color.red)
```
