## Poetry

Poetry is a tool for dependency management and packing in Python that uses pip behind the scenes. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

Poetry requires Python 3.7+.

### venv

```console
$ poetry config virtualenvs.in-project true
$ poetry init
```

For installing dependencies in a docker container, requires some configuration.

```dockerfile
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev --no-interaction --no-ansi
```

### pyproject.toml

Similar to npm package.json config file that packs similiar functionalities.

```toml
[tool.poetry]
name = "unbiased-coder-project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
python-dotenv = "^0.20.0"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```
