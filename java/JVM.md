## JVM (Java Virtual Machine)

The JVM is an engine that provides runtime environment to drive the Java Code or applications. It converts Java bytecode into machine language. In other programming languages, the compiler produces machine code for a particular system. However, Java compiler produces code for JVM.

The JVM has three primary functions:

- To allow Java programs to run on any device or OS (Write Once Run Anywhere)
- To intepret and execute Java bytecode
- To manage and optimize program memory

### JVM languages

The JVM is flexible and powerful enough to support many other languages incudling Scala, Groovy and Kotlin.

### How does JVM work?

The JVM follows the following steps in order to intepret Java code and execute it:

1. Loading the bytecode
2. Verifying the bytecode
3. Preparing memory resources
4. Intepreting Java bytecode
5. JIT compilation
6. Garbage collection

#### Loading Java bytecode

This task is performed by the **class loader**, whose responsibility is to locate any necessary bytecode files and load them into system memory.

#### Verification

The JVM needs to verify its correctness, which it does by checking the Java bytecode for violations of the Java langauge specification.

#### Preparing bytecode

Once the bytecode is verified, the Java Virtual Machine prepares the memory and resources needed in order for the program to execute. This preparation includes memory allocation for any required objects and initializing static variables.

#### Intepreting bytecode

Next, the JVM has to interpret the bytecode and sequentially execute each instruction. While each instruction is executed, the JVM maintains a stack of values to be used by any following sets of instructions.

#### JIT compilation

Once the code has been interpreted, the JVM may use Just-In-Time (JIT) compilation to improve performance. During JIT compilation, the JVM compiles frequently executed bytecode into native machine language, which is executed with more efficiency than interpreted bytecode.

#### Garbage collection

As the application is executing, the JVM manages memory resources (allocating and deallocating) by performing automatic garbage collection. Garbage collection frees up memory resources that are no longer being used by the program or CPU, allowing the memory to be reclaimed by the JVM and put to other uses.
