## Semaphore

Semaphore is an integer variable that is shared between threads, and is never allowed to go negative. Attempting to decrement will block the running thread until another thread increments the count.

Semaphores are used to implement critical sections, which are regions of code that must be executed by only one process at a time. By using semaphores, processes can coordinate access to shared resources i.e. shared memory or I/O devices.

Semaphores support the following interfaces:

- V(): Increments the semaphore (release/signal)
- P(): Block until the semaphore has a positive value, then decrement it (acquire/wait)

### Binary

Binary Semaphore is also known as a mutex lock. It can only have two values: 0 and 1. However, limitations include:

- Priority inversion
- Deadlock
- OS has to keep track of all calls to wait and signal the semaphore (busy waiting)

```py

from enum import Enum
from queue import Queue

class Semaphore:
    class Value(Enum):
        Zero = 0
        One = 1

    def __init__(self):
        self.q = Queue()
        self.value = Semaphore.Value.One

    def P(self, s, p):
        if s.value == Semaphore.Value.One:
            s.value = Semaphore.Value.Zero
        else:
            # add the process to the waiting queue
            s.q.put(p)
            p.Sleep()

    def V(self, s):
        if s.q.qsize() == 0:
            s.value = Semaphore.Value.One
        else:
            # select a process from waiting queue
            p = s.q.queue[0]
            # remove the process from waiting as it has
            # been sent for CS
            s.q.get()
            p.Wakeup()
```

### Couting

Its value can range over an unrestricted domain. It is used to control access to a resource that has multiple instances.

```py
import heapq
# Global Variable to track the Processes going into Critical Section
COUNTER=1

class Semaphore:
	def __init__(self,value):
		# Value of the Semaphore passed to the Constructor
		self.value=value
		# The Waiting queue which will be using the heapq module of Python
		self.q=list()

	def getSemaphore(self):
		''' Function to print the Value of the Semaphore Variable '''
		print(f"Semaphore Value: {self.value}")

def block(process):
	print(f"Process {process} Blocked.")

def wakeup(process):
	print(f"Process {process} Waked Up and Completed it's work.")

def P(s):
	global COUNTER
	s.value=s.value-1
	if(s.value<0):
		heapq.heappush(s.q,COUNTER)
		block(COUNTER)
	else:
		print(f'Process {COUNTER} gone inside the Critical Section.')
		COUNTER+=1
		return

def V(s):
	global COUNTER
	s.value=s.value+1
	if(s.value<=0):
		p=heapq.heappop(s.q)
		wakeup(p)
		COUNTER-=1
	else:
		print(f"Process {COUNTER} completed it's work.")
		COUNTER-=1
		return

# Can Pass the Value of the Counting Semaphore to the Class Constructor

# Example for Counting Semaphore value as 2
s1=Semaphore(2)
s1.getSemaphore()

P(s1)
s1.getSemaphore()

P(s1)
s1.getSemaphore()

P(s1)
s1.getSemaphore()

V(s1)
s1.getSemaphore()

V(s1)
s1.getSemaphore()

V(s1)
s1.getSemaphore()
```
