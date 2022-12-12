## Mixin

A Mixin is a class that provides methods to other classes (a utility class) but not considered as a base class itself i.e. not instantiated by itself. Mixins provide a safe form of multiple inheritance as they enforce a new constraint on classes and can't fall prey to diamond inheritance problems. No limit on number of mixins that can be used to compose a new class. Subclasses that inherit from Mixin only inherit that feature and nothing else. Useful when:

- Want to provide alot of optional features for a class.
- Want to use one particular feature in alot of different classes.

When inheriting multiple classes/Mixins, order is important. Recommended and logical way to structure order is to make highest to lowest from left to right.

```py
# Mixins should come in first if they override a method defined in base class
# base class has to be last so that it catches any attribute lookups that
# were not on any mixins
class UltimateBase(object):
    def dispatch(self, *args, **kwargs):
        print 'base dispatch'

class FooMixin(object):
    def dispatch(self, *args, **kwargs):
        print 'perform check A'
        return super(FooMixin, self).dispatch(*args, **kwargs)

class BarMixin(object):
    def dispatch(self, *args, **kwargs):
        print 'perform check B'
        return super(BarMixin, self).dispatch(*args, **kwargs)

class FooBar(FooMixin, BarMixin, UltimateBase):
    pass

FooBar().dispatch()
# perform check A
# perform check B
# base dispatch
```

```python
from .views import View
from .models import Product, Category, Customer, Order

class SingleObjectMixin(object):
    model = None
    def get_object(self, request):
        if self.model is None:
            raise Exception("Model must be set.")
        return self.model.get(id=request.kwargs.get("id"))

class ProductView(SingleObjectMixin, View):
    model = Product

class CategoryView(SingleObjectMixin, View):
    model = Category

class CustomerView(SingleObjectMixin, View):
    model = Customer

class OrderView(SingleObjectMixin, View):
    model = Order
```
