## Callable Provider

Callable provider calls a function, a method or another callable.

```py
some_function = Callable(
    some_function,
    "positional_arg1", "positional_arg2",
    keyword_argument1=3, keyword_argument=4)

# or

some_function = Callable(some_function) \
    .add_args("positional_arg1", "positional_arg2") \
    .add_kwargs(keyword_argument1=3, keyword_argument=4)

# or

some_function = Callable(some_function)
some_function.add_args("positional_arg1", "positional_arg2")
some_function.add_kwargs(keyword_argument1=3, keyword_argument=4)
```

```py
import passlib.hash

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):

    password_hasher = providers.Callable(
        passlib.hash.sha256_crypt.hash,
        salt_size=16,
        rounds=10000,
    )

    password_verifier = providers.Callable(passlib.hash.sha256_crypt.verify)


if __name__ == "__main__":
    container = Container()

    hashed_password = container.password_hasher("super secret")
    # or container.password_hasher.add_args('super secret')
    assert container.password_verifier("super secret", hashed_password)
```
