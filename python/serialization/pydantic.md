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

## Strict types

By default, strings are accepted as-is, and Pydantic will coerce conversion using str(v). To enforce strict types, define in the class.

```py
from pydantic import BaseModel, StrictStr

class Test(BaseModel):
    name: StrictStr
```

## Reading request body

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

## Passing nested models

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

## Validating and parsing

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

## Arbitrary field

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

## Validating multiple fields

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

## Root validator

Can be used to validate on the entire model's data. To skip validation if prior validators fail, set skip_on_failure to be True.

```py
from pydantic import BaseModel, ValidationError, root_validator


class UserModel(BaseModel):
    username: str
    password1: str
    password2: str

    @root_validator(pre=True)
    def check_card_number_omitted(cls, values):
        assert 'card_number' not in values, 'card_number should not be included'
        return values

    @root_validator
    def check_passwords_match(cls, values):
        pw1, pw2 = values.get('password1'), values.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return values
```

## Creating models without validation

https://docs.pydantic.dev/latest/usage/models/#creating-models-without-validation

```py
from pydantic import BaseModel


class User(BaseModel):
    FIRST_NAME: StrictStr
    LAST_AGE: StrictInt
    SET_FIELD: StrictStr = 'this field is set'

    @validator('FIRST_NAME')
    def validate_name(cls, v):
        if v == 'John':
            return 'Hello World!'
        return v


payload = {'firstName': 'John', 'lastAge': 5, 'userId': 100}
test = User.construct(**payload)
print(test.dict())

# {'FIRST_NAME': 'John', 'LAST_AGE': 5, 'SET_FIELD': 'this field is set'}
```

## Aliases

```py
class TMDB_Category(BaseModel):
    name: str = Field(alias="strCategory")
    description: str = Field(alias="strCategoryDescription")
```

```py
from pydantic import BaseModel, StrictStr, StrictInt


def convert_snake_to_camel_case(v: str):
    strings = v.split("_")
    return strings[0].lower() + "".join(word.lower().capitalize() for word in strings[1:])

def convert_camel_to_snake_case(v: str):
    return ''.join(['_' + i.lower() if i.isupper() else i for i in v]).lstrip('_')


class Testing(BaseModel):
    FIRST_NAME: StrictStr
    LAST_AGE: StrictInt

    class Config:
        alias_generator = convert_snake_to_camel_case


class Testing2(Testing):
    USER_ID: StrictInt

payload = {'firstName': 'John', 'lastAge': 5, 'userId': 100}

test = Testing2(**payload)
print(test)
print(test.dict(by_alias=True))

# FIRST_NAME='John' LAST_AGE=5 USER_ID=100
# {'firstName': 'John', 'lastAge': 5, 'userId': 100}
```
