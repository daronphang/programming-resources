## pyproject.toml

Similar to npm package.json config file that packs similiar functionalities.

### packages

A list of packages and modules to include in the final distribution. Poetry is clever enough to detect Python subpackages. Hence, only need to specify the directory where your root package resides.

```toml
[tool.poetry]
# ...
packages = [
    { include = "my_package" },
    { include = "extra_package/**/*.py" },
    { include = "my_package", from = "lib" },
]
```

### dependencies

```toml
[tool.poetry.dependencies]
python = ">=3.7.9,<4.0"
asyncio = "3.4.3"
click = "8.1.3"
mutils = {path = "../mutils", develop = false}
```

### include and exclude

A list of patterns that will be included/excluded in the final package. If a VCS is used, the exclude field will be seeded with the VCS' ignore settings i.e. gitignore.

```toml
[tool.poetry]
# ...
include = [
    { path = "tests", format = "sdist" },
    { path = "for_wheel.txt", format = ["sdist", "wheel"] }
]
exclude = ["my_package/excluded.py"]
```

### dependencies and groups

Poetry is configured to look for dependencies on PyPI by default. If you have multiple repositories configured, can explicitly tell Poetry where to look for a specific package.

```toml
[tool.poetry.dependencies]
requests = "^2.13.0"
requests = { version = "^2.13.0", source = "private" }

[[tool.poetry.source]]
name = "private"
url = "http://example.com/simple"
```

Can organize your dependencies in groups to manage them in a more granular way.

```toml
[tool.poetry.group.test.dependencies]
pytest = "*"

[tool.poetry.group.docs.dependencies]
mkdocs = "*"
```

### scripts

Scripts or executables that will be installed when installing the package. When a script is added or updated, run 'poetry install' to make them available in the project's virtualenv.

```toml
[tool.poetry.scripts]
my_package_cli = 'my_package.console:run'
```

## Example

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
