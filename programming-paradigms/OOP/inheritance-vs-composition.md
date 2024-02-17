## Inheritance (Is-A-Relation)

Mechanism that allows us to inherit all the properties from another class. The class from which the properties and functionalities are utilized is called parent/base class. The class which inherits is called the child/derived class.

- Inheritance is defined statically at compile-time and straightforward to use.
- Easier to modify implementation being reused.
- However, can't change implementation inherited from parent class at run-time.
- Parent classes often define part of subclasses' physical representation i.e. inheritance breaks encapsulation as any changes in parent's implementation will force subclass to change.

## Composition (Has-A-Relation)

Describes a class that references to one or more objects of other classes as an Instance variable. Enables creating complex types by combining objects of different classes i.e. a class Composite can contain an object of another class component.

- Object composition is defined dynamically at run-time through objects acquiring references to other objects.
- Requires objects to respect each others' interfaces.
- Doesn't break encapsulation as objects are accessed solely through their interfaces.

```py
class A:
    # initialization of properties and methods

class B:
    obj_A = A()
    # initialization of properties and methods of class B
```

```py
class Salary:
    def __init__(self, monthly_income):
        self.monthly_income = monthly_income

    def get_total(self):
        return (self.monthly_income*12)


class Employee:
    def __init__(self, monthly_income, bonus):
        self.monthly_income = monthly_income
        self.bonus = bonus
        self.obj_salary = Salary(self.monthly_income)

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus) + ' €'


obj_emp = Employee(2600, 500)
print(obj_emp.annual_salary())
```

## Delegation

A way of making composition as powerful for reuse as inheritance. In delegation, a receiving object delegates operations to its delegate:

- Class Rectangle has methods Area().
- Instead of making class Window a subclass of Rectangle, Window reuses Rectangle's behavior by delegating to it i.e. Window has a Rectangle.
- Window must forward requests to its Rectangle instance explicitly.

## Inheritance vs Composition

- Inheritance is used when a class wants to derive the nature of parent class and then extend/modify the functionality of it.
- In Composition, the class cannot be modified or have its functionality extended.
- Composition is more flexible as it models a loosely coupled relationship.
