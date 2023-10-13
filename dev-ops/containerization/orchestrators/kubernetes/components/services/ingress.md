## Ingress

Ingresses are closely related objects and are used to set up HTTP routes to Services via a load balancer i.e. operates at Layer 7 of OSI model. Also support HTTPS traffic secured by TLS certificates.

For LoadBalancer Services, a cluster with 25 internet-facing apps will need 25 cloud load balancers (1-to-1 mapping). Ingress fixes this by providing access to **multiple web applications through a single LoadBalancer Service**.

Ingress and service mesh have overlapping functionalities i.e. if you plan to run a service mesh, you may not need Ingress.

<img src="../../assets/ingress.png">

## Components

The **object spec** defines rules that govern traffic routing, and the **controller** implements the rules.

However, a lot of Kubernetes clusters don't ship with a built-in Ingress controller i.e. you have to install one. Once you have an Ingress controller, you deploy Ingress objects with rules that govern how traffic hitting the Ingress is routed.
