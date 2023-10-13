## LoadBalancer

Standard way to expose a Service to the internet. Creates an external load balancer in the current cloud (only available when infrastructure/cloud provider gives LB) and assigns a fixed, external IP to the Service. Superset of NodePort i.e. creates NodePort and ClusterIP Services.

Requires 1-to-1 mapping between an internal Service and a cloud load balancer.
