## Response Model

Can declare the model used for response. FastAPI will use the response_model to:

- Convert the outputa data to its type declaration.
- Validate the data.
- Limit the output data to that of the model.

```py
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    # although path operation returns the same input user that contains password
    # FastAPI will take care of filtering by declaring output model
    return user
```

### Return JSON Responses Directly

Gives you flexibility in returning any data type.

```py
from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)
```

### Excluding Attributes in Responses

For NoSQL databases, sometimes you may have models with many optional attributes, but you don't want to send a very long JSON response full of default values. Use the response_model_exclude_unset parameter.

```py
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

'''
/items/foo
{
    "name": "Foo",
    "price": 50.2
}

/item/bar
{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
}
'''
```
