## Memory

Everything in Python is an object i.e. primitive values, variables, functions, dictionaries, lists, tuples, etc. When an object is created, it is stored in memory. The variables/references point to the memory address of an object.

At run time, computer memory gets divided into different parts: Code, Stack and Heap.

### Code

Code/Text/Instruction section of the memory stores binary code. Machine follows instructions in the code section.

### Stack

Python interpreter loads functions and local variables in the Stack memory according to the instructions. Stack memory is static and temporary i.e. as soon as the function/variable is called, it gets popped from the stack. The variables only store memory addresses of objects.

### Heap

To store objects, need memory with dynamic memory allocation i.e. size of memory and objects can change. Python interpreter actively allocates and de-allocates the memory on the Heap using garbage collection algorithm that removes unused objects.

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

## Memory management

Values of objects are stored in memory for quick access. In early programming languages, developers were responsible for managing memory in their programs i.e. to allocate memory for a variable before creating an object, and deallocating it to free that memory for other objects. However, this leads to memory leaks and freeing up of memory too soon.

Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the **Python memory manager**.

With automatic memory management, runtime handles this for programmers. Python uses two strategies for memory allocation: reference counting and garbage collection.

### Reference counting

Reference counting works by counting the number of times an object is referenced by other objects. When the count becomes zero, it is unusable by program code and is deallocated.

An object's reference count changes as the number of aliases that point to it changes. It decreases when it is deleted with del, reference is reassigned, or its reference goes out of scope.

### Garbage Collection

However, automatic memory management comes at a cost, whereby it requires to use additional memory and computation to track all of its references. Moreover, reference counting does not work for cyclic references i.e. a situation when an object refers to itself.

As reference cycles take computational work to discover, garbage collection must be a **scheduled activity**. Python schedules garbage collection based upon a threshold of object allocations and deallocations. When the number of allocations is greater than the number of deallocations, garbage collector is executed.

Can be invoked manually during the execution of a program. Never disable garbage collector unless you have a good reason to do so.

```py
import gc

print("Garbage collection thresholds:", gc.get_threshold())

# invoking manually
collected = gc.collect()
print "Garbage collector: collected %d objects." % (collected)
```
