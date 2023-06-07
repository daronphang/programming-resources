## Task-Based Build System

In a task-based build system, the fundamental unit of work is the task. Each task is a script that can execute any sort of logic, and tasks specify other tasks as dependencies that must run before them. Most major build systems are task-based including Ant, Maven, Gradle, Grunt and Rake.

## Drawbacks

### Too much power given to engineers

As the tools let engineers define any script as a task, they are extremely powerful. However, this becomes more difficult to work as build scripts grow more complex.

The problem with such systems is that they end up giving too much power to engineers and not enough power to the system. As the system has no idea what the scripts are doing, performance suffers, as it must be very conservative in how it schedules and executes build steps.

### Difficulty of parallelizing build steps

Task-based systems are often unable to paralleize task execution. If task A depends on tasks B and C, but B and C do not depend on each other, it may be safe to run them in parallel if they don't touch the same resources. However, there is no way for the system to know this and hence, restricts the entire build to running on a single thread in a single process.

### Difficulty of maintaing and debugging scripts

As tasks can do anything, there is no way to check whether each task is executed correctly. Also, tasks may perform side effects that may be dependencies for other tasks, which may introduce subtle bugs.

So long as engineers can write arbitary code that runs during the build, the system can't have enough information to always be able to run builds quickly and correctly.
