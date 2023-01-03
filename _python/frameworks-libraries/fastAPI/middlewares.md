## Middlewares

A function that works with every request before it is processed, and with every response before returning it.

### Decorator

```py
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### Function

```py
from starlette.middleware.base import BaseHTTPMiddleware

async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware,dispatch=add_process_time_header)
```

### CORS

Refers to situations when a frontend communicates with a backend, but the backend is in a different origin.

```py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
```

### Multiple

```py
def test1(request: Request, call_next):
    print('test1 before')
    resp = await call_next(request)
    print('test1 after')

def test2(request: Request, call_next):
    print('test2 before')
    resp = await call_next(request)
    print('test2 after')

def test3(request: Request, call_next):
    print('test3 before')
    resp = await call_next(request)
    print('test3 after')


app.add_middleware(BaseHTTPMiddleware,dispatch=test3)
app.add_middleware(BaseHTTPMiddleware,dispatch=test2)
app.add_middleware(BaseHTTPMiddleware,dispatch=test1)

'''
test1 before
test2 before
test3 before
test3 after
test2 after
test1 after
'''
```
