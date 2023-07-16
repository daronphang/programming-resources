## Jobs and Tasks

A borg job's properties include its name, owner and the number of tasks it has. Jobs can have constraints to force its tasks to run on machines with particular attributes such as processor architecture, OS version, or an external IP address.

A task has properties such as its resource requirements and the task's index within the job. Most task properties are the same across all tasks in a job, but can be overriden.

Users operate on jobs by issuing RPCs to Borg, most commonly from a command-line tool, other Borg jobs, or on monitoring systems.
