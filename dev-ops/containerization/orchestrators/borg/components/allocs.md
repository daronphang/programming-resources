## Allocs (Allocation)

A Borg alloc is a reserved set of resource on a machine (CPU, RAM) in which one or more tasks can be run. The resources remain assigned whether or not they are used. Multiple tasks running inside the same machine will share its resources.

Allocs can be used to set resources aside for future tasks, to retain resources between stopping a task and starting it again, and to gather tasks from different jobs onto the same machine. If an alloac must be relocated to another machine, its tasks are rescheduled with it.
