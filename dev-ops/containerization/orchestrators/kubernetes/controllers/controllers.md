## Workload Controllers

A Controller is a process that runs in the background and its job is to continously monitor the status of resources that it's supposed to manage. Examples of resources include ReplicaSet, Deployment, Job, CronJob, StatefulSet, Namespace, etc.

Controllers enable Pods to have self-healing, scaling, updates and rollbacks. Every controller has a PodTemplate defining the Pods it deploys and manages. You will almost always deploy Pods via controllers.

Pods deployed via controllers have all the benefits of being monitored and managed by a highly-available controller running on the control-plane.
