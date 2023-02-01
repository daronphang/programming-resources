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
