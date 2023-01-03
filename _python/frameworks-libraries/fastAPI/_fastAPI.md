## FastAPI

FastAPI stands on the shoulders of giants: Starlette and Pydantic. Requires an ASGI server.

Provides OpenAPI and automatic data model documentation with JSON schema.

```console
$ pip install uvicorn[standard]

$ # reload is the same as flask debug mode
$ uvicorn python.module:object_instance
$ uvicorn main:app --reload
```

```py
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/async")
async def read_root_async():
    return {"Hello": "World"}

# order matters for path operations
@app.get("/items")
async def read_items():
    return {"item_ids": "hello world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

### API Docs

```
http://localhost:8000/docs      Swagger UI
http://localhost:8000/redoc     ReDoc (alternative)
```
