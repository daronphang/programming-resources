## Pydantic

```py
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
print(user.id)
#> 123
print(repr(user.signup_ts))
#> datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
#> [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
```

## Strict Types

By default, strings are accepted as-is, and Pydantic will coerce conversion using str(v). To enforce strict types, define in the class.

```py
from pydantic import BaseModel, StrictStr

class Test(BaseModel):
    name: StrictStr
```

## Reading Request Body

Access attributes by dot notation. Else, can explicitly convert to dict using .dict() after parsing the class.

```py
from pydantinc import BaseModel

class Test(BaseModel):
    hello: str


payload = {'hello': 'world'}
c = Test(payload)
print(c.hello)

c = c.dict()
print(c['hello'])
```

## Passing Models to Mdoels

```py
from pydantic import BaseModel

class Worker(BaseModel):
    name: str


class Student(BaseModel):
    name: str
    school: str = None

    def __init__(self, worker: Worker):
        super().__init__(**worker.dict())


w = Worker(name="john")
s = Student(**w.dict())
s = Student(w)  # if init is modified
```

## Validating and Parsing

```py
from enum import Enum
from pydantic import BaseModel


class Colors(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

class Test(BaseModel):
    color: Colors

p = {'color': 'red'}
v = Test(**p)
print(v.color)  # Colors.RED of type Enum
```

## Arbitrary Field

```py
from pydantic import (
    BaseModel,
    Field,
    StrictStr,
    validator,
    StrictBytes,
    StrictFloat,
    StrictInt,
)
from typing import Any, Dict, Union, Optional


class SqlOperator(Enum):
    EQUAL = '='
    GT = '>'
    GTE = '>='
    LT = '<'
    LTE = '<='
    IN = 'IN'
    OR = 'OR'   # composite
    BETWEEN = 'BETWEEN'
    LIKE = 'LIKE'


class SomeDict(BaseModel):
    __root__: Dict[StrictStr, Union[StrictStr, StrictFloat, StrictBytes]]


class Test(BaseModel):
    EQUAL: SomeDict = Field(alias=SqlOperator.EQUAL.value)
    GT: Optional[SomeDict] = Field(alias=SqlOperator.GT.value)

payload = {
    "=": {
        "test1": "hello"
    }
}

print(Test(**payload).EQUAL)
```

## Validating Multiple Fields

```py
class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    # values is a dict containing the name-to-value mapping of any previously validated fields
    # field ordering is important i.e. password2 has access to password1 but not vice versa
    # if validation fails on another field, it will not be included in values; hence if 'password1' in values
    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v
```
