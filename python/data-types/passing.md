## Pass by assignment

Python’s behavior is neither purely pass-by-value nor pass-by-reference. Instead, it employs a mechanism called “pass by assignment” or “call by object.”

The essence of this mechanism lies in understanding how objects and references work in Python.

### Variable assignment

Variable assignment in Python involves associating a name (variable) with a value. However, rather than storing the value directly, **variables act as references to the assigned value**. This concept empowers the flexibility of dynamically typed Python, allowing variables to be reassigned with different types of values as needed.

```py
x = 20
x = "hello world"
print(x) # hello world
```

```py
fruits = ["Apple", "Banana", "Melon"]
gifts = fruits
fruits = ["Kiwi", "Charry"]
print(fruits) # ["Kiwi", "Charry"]
print(gifts) # ["Apple", "Banana", "Melon"]
```

### Parameter argument relationship in functions

Function parameters in Python are local variables and when we provide arguments to the functions we provide values to the parameter.

For immutable objects, the behavior is akin to the “pass-by-value” behavior observed in other programming languages, where a copy of the variable is passed into a function, and any modifications made inside the function do not affect the original variable.

```py
def multiply(value, times):
  value *= times

number = 5
multiplier = 2

multiply(number, multiplier)
print(number) # 5
```

For mutable objects, the behavior has dual nature. If we reassign the variable with a new value, it will produce the expected result of modifying the object independently of other references.

```py
def listChanger(v):
  v = ["Mango", "Kiwi", "Apple"]
  print("Changed List :", v) # Changed List : ['Mango', 'Kiwi', 'Apple']

fruits = ["Melon", "Orange", "Cherry"]

listChanger(fruits)
print("Original List :", fruits) # Original List : ['Melon', 'Orange', 'Cherry']
```

However, if we modify the object directly without reassigning the variable, the changes will be reflected in all references to that object i.e. pass-by-reference behavior.

```py
def addLemon(v):
  v.append("Lemon")
  print("Inner List :", v) # ['Melon', 'Orange', 'Cherry', 'Lemon']

fruits = ['Melon', 'Orange', 'Cherry']
addLemon(fruits)

print("Original List:", fruits) # ['Melon', 'Orange', 'Cherry', 'Lemon']
```
