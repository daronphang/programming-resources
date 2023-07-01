## Injector

Instance methods are not thread safe except for:

- Injector.get()
- Injection provided by inject() decorator

## Binding

Bind an interface to an implementation.

```py
binder.bind(A, to=A('some', 'thing'))
binder.bind(A, to=InstanceProvider(A('some', 'thing')))
binder.bind(interface=A, to=some_callable)
```

### Install

Install a module into the binder.

#### Function

```py
# function taking Binder as it's only parameter
def configure(binder):
    bind(str, to='s')

binder.install(configure)
```

#### Module

```py
class MyModule(Module):
    def configure(self, binder):
        binder.bind(str, to='s')

binder.install(MyModule())
```

#### Subclass

```py
binder.install(MyModule)
```

## Scopes

### Singletons

Singletons are delcared by binding them in the SingletonScope.

```py
@singleton
class Thing: pass   # first way

class ThingModule(Module):
    def configure(self, binder):
        binder.bind(Thing, scope=singleton) # second way

    @singleton  # third way
    @provider
    def provide_thing(self) -> Thing:
        return Thing()
```
