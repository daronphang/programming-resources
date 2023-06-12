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

### Starting Programatically

```py
app, _ = create_app(standalone_mode=False) # to return app from click wrapper

if __name__ == "__main__":
    uvicorn.run("instacap.main:app", port=5000, host="0.0.0.0", log_level="info")
```

```py
@click.command()
@click.option('--configenv', default='DEVELOPMENT', help="config environment: TESTING, DEVLEOPMENT or PRODUCTION")
def create_app(configenv: str):
    # factory method
    configenv = ConfigEnvs[configenv]
    app = FastAPI()
    return app
```

```py
app, container = create_app(['--configenv', 'TESTING'], standalone_mode=False)
```
