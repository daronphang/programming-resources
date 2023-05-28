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

### install

If there is a poetry.lock file, it will use the exact versions from there instead of resolving them. This ensures that everyone using the library will get the same versions of the dependencies. If there is no lock file, Poetry will create one after dependency resolution.

```console
$ poetry install
```

### run

The run command executes the given command inside the project's virtualenv.

If you have a script defined in pyproject.toml, you can execute it from this command.

```console
$ poetry run python -V
$ poetry run my-script
```
