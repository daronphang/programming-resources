## Access Levels

### public

All members in a Python class are public by default.

### protected

The members of a class that are declared with an underscore are protected. They are only accessible to a class derived from it.

You can use property decorator to prevent direct modification of members from outside of the class. However, it can still be accessed outside.

### private

Python does not have any mechanism that effectively restricts access to any instance variable or method. Python prescribes a convention of prefixing the name/method with a double underscore.

This gives a strong suggestion not to touch it from outside the class. Any attempt to do so will result in an AttributeError.

Python performs name wrangling of private variables. Every member with a double underscore is changed to \_object.\_class\_\_variable. Hence, it can still be accessed but should be refrained.

```py
class Student:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')

std = Student("Bill", 25)
print(std.__schoolName) #AttributeError
print(std.__name)   #AttributeError
print(std.__display())  #AttributeError

print(std._Student.__name)  # Steve
```
