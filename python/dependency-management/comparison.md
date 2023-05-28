## poetry vs pip

Recommended to use poetry over pip for the following reasons.

### Better handling of dependency conflicts (complete constraint satisfaction)

When installing a different version of dependency that has a conflict in the venv, pip will complain but still goes ahead to install that version. This could cause bugs to occur during runtime.

Before installing or updating any libraries, poetry will check the dependency requirements of all the existing libraries that are installed, and any dependency conflict that is discovered would raise an error in the installation process.

### Easier to organize dependencies for dev and prod

Two requirements files are required for pip (requirements.txt and requirements-dev.txt) while poetry makes it easier by organizing them in pyproject.toml file.

```console
$ poetry add numpy
$ poetry add pytest --dev
```

### Reproducible library installations

When using requirements.txt file, pip requires manual updating of dependencies with freeze to persist the metadata of installed dependencies. With poetry, it uses poetry.lock file which stores only the metadata of dependencies that do no have conflicts with one another. Hence, we can be sure that we are always installing the same versions of libraries whenever we run poetry install.

### Better support for installing libraries from private repos

When installing from private repos, it would cause issues when installing the dependencies using requirements.txt file.

```console
$ pip install --index-url url-of-private-repo library-name
$ pip freeze > requirements.txt # will throw error when installing
```

For poetry, you simply have to define in the pyproject.toml file. The secondary parameter tells poetry to install libraries from PyPI first, and only go to the private repository if the libraries cannot be found.

```toml
[[tool.poetry.source]]
name = "name-of-private-repo"
url = "url-of-private-repo"
secondary = true
```
