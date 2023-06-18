## Choosing a Compute Service

Modern compute offerings are available in both the open source world (Kubernetes, Mesos, OpenWhisk, Knative), or as public cloud managed offerings (GCP, AWS EC2, AKS, GKE).

The choice of a compute service is difficult to change over time is because eventually it will become surrounded by a large ecosystem of helper services i.e. tools for logging, monitoring, debugging, alerting, visualization, on-the-fly analysis, configuration langauges and meta-languages, user interfaces, etc. These tools will need to be rewritten as a part of a compute service change.

### Centralization vs Customization

From the point of view of management overhead of the compute stack and resource efficiency, the best an organization can do is adopt a single CaaS solution to manage its entire fleet of machines and use only the tools available there for everybody. This ensures that as the organization grows, the cost of managing the fleet remains manageable.

However, a growing organization will have increasingly diverse needs. Nonetheless, there are ways to invest effort and get some of the benefits of customization while not suffering the worse downsides.

### Level of Abstraction: Serverless

Serverless offerings provide an even higher level of abstraction and provides inversion of control. The user will only be responsible for writing an 'Action' or 'Handler' function in the chosen language that takes the request parameters and returns the response. Examples include AWS Lambda and Google Cloud Run.

If multiple teams are using the same framework, instead of making the machines multi-tenant, we can also make the framework servers themselves multi-tenant. In this approach, we end up running a larger number of framework servers, dynamically loading/unloading the action code on different servers as needed, and dynamically directing requests to those servers that have the relevant action code loaded.

#### Pros and cons

Firstly, a serverless architecture requires your code to be truly **stateless**. There is no local state that is truly persisted across requests; everythign that you want to use, you should set up in the request-scope.

The managed serverless model is attractive for **adaptable scaling of the resource cost**, especially at the low-traffic end. For instance, in Kubernetes, your replicated container cannot scale down to zero containers (as the assumption that spinning up both a container and a node is too slow to be done at request-serving time). Hence, there is a minimum cost of having an application available in the persistent cluster model. On the other hand, a **serverless application can easily scale down to zero**.

Finally, adopting a serverless solution implies a certain **loss of control over your environment**. More control means more management overhead; however, this also means that if you need some extra functionality that is not available in the framework you use, it will become a problem for you.

### Public vs Private

An organization using a public cloud is effectively **outsourcing the management overhead** to a public cloud provider. For many, this is an attractive proposition as they can focus on providing value in their specific area of expertise, and do not need to grow significant infrastructure expertise.

Also, a public cloud is a way to scale the infrastructure more easily. As the level of abstraction grows (colocations, buying VM time, managed containers, serverless offerings), the ease of scaling up increases. For smaller organizations, **predicting resource requirements is challenging**, and hence, the advantages of not having to provision resources up front are significant.

However, one significant concern is the fear of lock-in i.e. the provider might suddenly increase their prices or maybe just fail, leaving an organization in a very difficult position.

Two strategies are possible. One is to use a lower-level public cloud solution (EC2) and run a higher-level open source solution (OpenWhisk, KNative) on top of it. This tries to ensure that if you want to migrate out, you can take whatever tweaks you did to the higher-level solution, tooling you built on top of it, and implicit dependencies you have along with you.

Another strategy for managing lock-in is to run in a hybrid cloud i.e. have part of your overall workload on your private infrastructure, and part of it run on a public cloud provider.

Both multicloud and hybrid cloud stragies require the multiple environments to be connected well, through direct network connectivity between machines in different environments and common APIs that are available in both.
