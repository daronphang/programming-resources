## Memory

Everything in Python is an object i.e. primitive values, variables, functions, dictionaries, lists, tuples, etc. When an object is created, it is stored in memory. The variables/references point to the memory address of an object.

At run time, computer memory gets divided into different parts: Code, Stack and Heap.

### Code

Code/Text/Instruction section of the memory stores binary code. Machine follows instructions in the code section.

### Stack

Python interpreter loads functions and local variables in the Stack memory according to the instructions. Stack memory is static and temporary i.e. as soon as the function/variable is called, it gets popped from the stack. The variables only store memory addresses of objects.

### Heap

To store objects, need memory with dynamic memory allocation i.e. size of memory and objects can change. Python interpreter actively allocates and deallocates the memory on the Heap using garbage collection algorithm that removes unused objects.

Memory addresses are shown in hexadecimals. Similar objects will point to the same address. This is a process optimization by Python called 'interning'. This applies to integers, strings and boolean, but not large primitive and composite values.

```py
x = 1
y = 1
print(id(x))    # 140710407579424
print(hex(id(x)))   # '0x7ff9b1dc2720'

print(hex(id(y)))   # '0x7ff9b1dc2720', same as x
```

```py
lst = [1, 2, 3, 257]
print(hex(id(lst))) # '0x236330edf88'
print(id(lst[0]))   # '0x7ffdf176a190'

a = 1
print(hex(id(a)))   # '0x7ffdf176a190', same as lst[0]
```
