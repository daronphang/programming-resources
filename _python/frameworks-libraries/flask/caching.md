## Caching

Flask-Caching provides support for various backends to any Flask application.

```py
from flask import Flask
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# cache.init_app(app)
```

```py
@app.route('/')
@cache.cached(timeout=50)
def index():
    return 'Cached for 50s'
```
