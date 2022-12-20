## Dependencies

FastAPI has a powerful Dependency Injection system. DI is a way for your code to declare things that it requires to work and use. Useful when you need to:

- Have shared logic.
- Share database connections.
- Enforce security, authentication, role requirements, etc.

The class Depends take in a single parameter i.e. function, and that

```py
from typing import Union

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    # result is assigned to the parameter in path operation
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```

### Callables

FastAPI checks if the object provided in Depends is callable (functions, classes). If you pass a 'callable' as a dependency, FastAPI will analyze the parameters and process them in the same way as the parmeters for a path operation function.

```py
from typing import Union

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    # can declare as commons=Depends(CommonQueryParams)
    # class is declared twice for declaring the type
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
```

As a shortcut, can declare the dependency as the type of the parameter.

```py
async def read_items(commons: CommonQueryParams = Depends()):
    pass
```

### Global

```py
from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
```

### Yield

Code prior to and including the yield statement is executed before sending a response.

When using try with yield, you will receive any exception that was thrown. However, if you raise an exception after the yield, nothing will be caught as the exit code in dependencies is executed after the response is sent.

```py
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

### Sub Dependencies

FastAPI makes sure that each dependency with yield is run in the correct order.

```py
from fastapi import Depends


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
```

### Context Mananger

```py
class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db
```
