## Workload Controllers

Controllers enable Pods to have self-healing, scaling, updates and rollbacks. Every controller has a PodTemplate defining the Pods it deploys and manages. You will almost always deploy Pods via controllers.

Pods deployed via controllers have all the benefits of being monitored and managed by a highly-available controller running on the control-plane.
