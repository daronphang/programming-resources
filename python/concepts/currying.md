## Currying

```py
def curry(fn, arg_count: int):
    # tuple of arguments must match with arg_count
    # concern of memory leak if not cleared
    closure_args = []

    def curried(*args):
        nonlocal closure_args
        if len(closure_args)+len(args) >= arg_count:
            return fn(*closure_args,*args)
        elif args[0] == 'GARBAGE_COLLECT':
            # garbage collect
            del closure_args
            return
        closure_args += args
        return curried
    return curried
```
