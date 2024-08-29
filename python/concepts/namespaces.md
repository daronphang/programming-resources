## Namespaces and scope

A namespace is a system that has a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary in which keys are the object names and values are objects themselves.

A lifetime of a namespace depends upon the scope of objects; if the scope of an object ends, the lifetime of that namespace ends. Not possible to access inner namespace's objects from an outer namespace.

Python has four namespaces including Local, Enclosing, Global and Built-in (LEGB).

## Built-In

Contains the names of all Python's built-in objects i.e. AttributeError, callable, dict, dir,list, zip.

```py
print(dir(__builtins__))
```

## Global

Contains any names defined at the level of the main program.

```py
print(type(globals()))
print(globals())
```

### \_\_name\_\_

Special variable that determines if the module is being run directly when executed, or if it is imported. The interpreter will set the current module to \_\_main\_\_ if it is executed as the main program, else it will set it to the parent's module name. Module's name is available as \_\_name\_\_.

```py
# file2.py
import File1

print ("File2 __name__ = %s" %__name__)

if __name__ == "__main__":
    print ("File2 is being run directly")
else:
    print ("File2 is being imported")
'''
File1 __name__ = File1
File1 is being imported
File2 __name__ = __main__
File2 is being run directly
'''
```

## Troubleshooting namespaces

1. ModuleNotFoundError: No module named testing

Whenever you encounter an import error, print \_\_name\_\_ of the module to check how it is being called.

2. ImportError: attempted relative import with no known parent package

Occurs when you are using dot notation. Run script with -m flag. Do not append .py suffix as -m flag only requires module names.

```sh
$ py -m src.main # instead of src/main    # declare path as module
```

## Enclosing and local

Interpreter creates a new namespace whenever a function executes. That namespace is local to the function and remains in existence until the function terminates.

Enclosing is similar to closures in Javascript.

```py
def f():
    x = 'hi' # enclosing scope
    def g():
        x = 'hello' # local scope
        print(x)
    g()
    return
```

```py
# closures

def closure():
    a = 1
    def inner():
        nonlocal a
        a += 1
        return a
    return inner

test = closure()
print(test()) # 2
print(test()) # 3
print(test()) # 4
print(test()) # 5
```
