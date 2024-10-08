## Modules

In Python, a module is a single file containing Python definitions and statements. Modules can be imported and used in other Python files using the import statement.

## Packages

Python Packages are collections of modules that provide a set of related functionalities, and these modules are organized in a directory hierarchy. In simple terms, packages in Python are a way of organizing related modules in a single namespace.

Each Python package must contain a file named `**init**.py``. Init files are used to mark directories on disk as Python package directories and not modules. In its absence, Python will not look for submodules inside that directory and attempts to import will fail. Can be declared as an empty file.

Python defines two types of packages, regular and namespace. Regular package is typically implemented as a directory containing init file. When it is imported, the init file is implicitly executed i.e. importing parent.one will implicitly execute parent/**init**.py and parent/one/**init**.py.

https://docs.python.org/3/reference/import.html#regular-packages

## Relative and absolute imports

Absolute import uses the full part from project's root folder to the desired module. Relative import uses the relative path (starting from the path of current module). Module is a single Python file. Package is a collection of modules.

```python
└── project
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── package2
        ├── __init__.py
        ├── module3.py
        ├── module4.py
        └── subpackage1
            └── module5.py

# in module5.py:
from project.package1.module1 import class1
from ..module3 import class2

# need to have __init__.py in packages for absolute import, else will be read as 'module' by Python
```

## Best practices

- Do not import a module that imports from another module as it may cause circular dependencies and lead to unexpected errors if imported module is changed i.e. module A importing module B, C, D but module C imports module B.
- Do not cross-import from different folders.

## Import errors

- CD one directory higher than base directory and run python script.
- Remove any unused imports (prevent circular imports).
- Move run file into another folder.

## `__all__`

It declares the semantically 'public' names from a module. Users are expected to use it, and they can have the expectation that it will not change.

`__all__` affects when module is imported with \* behavior. Members that are not mentioned in `__all__` are still accessible from outside the module and can be imported with from <module> import <member>. Also, it overrides the default of hiding everything that begins with an underscore.

```py
# foo.py
__all__ = ['foo', 'bar']

foo = 'hello'
bar = 'world'
baz = 'yo'
```

```py
# bar.py

from foo import *   # imports foo and bar only
```
