## Job Accomodations

When more work shows up than can be accomodated, the solutions are priority and quota.

### Priority

Every job has a priority (small positive integer). A high priority task can obtain resources at the expense of a lower priority one, even if that involves preempting (killing) the latter.

Borg defines non-overlapping priority bands for different uses, including monitoring, production, batch and best effort (testing/free).

Although a preempted task will often be rescheduled in the cell, preemption cascades could occur if a high-priority task bumped out a slightly lower-priority task, and so on. To eliminate this, tasks in the production priority are disallowed to preempt one another.

### Quota

Quota is used to decide which jobs to admit for scheduling. Quota is expressed as a vector of resource quantities (CPU, RAM, disk, etc.) at a given priority, for a period of time. The quantities specify the maximum amount of resources that a user's job requests can ask for at a time i.e. 20TB of RAM at prod priority from now until end of July in cell XX.

Quota-checking is part of admission control and not scheduling. Jobs with insufficient quota are immediately rejected upon submission.

Higher-priority quota costs more than lower-priority. Production-priority quota is limited to the actual resources available in the cell, so that a user who submits a production-priority job that fits in their quota can expect it to run, modulo fragmentation and constraints.

## Resource Reclamation

A job can specify a resource limit i.e. an upper bound on the resources that each task should be granted. This limit is used by Borg to determine if the user has enough quota to admit the job, and to determine if a particular machine has enough free resources to schedule the task.

There are users who will request more resources than their tasks will use, as Borg will normally kill a task that tries to use more RAM or disk space than it requested, or throttle CPU to what it asked for.

Rather than waste allocated resources that are not currently being consumed, Borg estimates how many resources a task will use and reclaim the rest for work that can tolerate lower-quality resources, such as batch jobs. The estimate is called the task's reservation, and is computed by the Borgmaster every few seconds, using fine-grained usage (resource consumption) information captured by the Borglet.

The Borg scheduler uses limits to calculate feasibility for prod tasks, so they never rely on reclaimed resources and aren't exposed to resource oversubscription. For non-prod tasks, it uses the reservations of existing tasks so the new tasks can be scheduled into reclaimed resources.

A machine may run out of resources at runtime if the predictions are wrong. If this happens, Borg kills or throttles non-prod tasks, never prod ones.
