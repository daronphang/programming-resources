## Generic subdomains

**Some parts of the model add complexity without capturing or communicating specialized knowledge**. Anything extraneous makes the core domain harder to discern and understand. The model clogs up with details of general principles everyone knows or that belong to specialties that are not your primary focus but play a supporting role. Yet, however generic, these other elements are essential to the functioning of the system and the full expression of the model.

Identify **cohesive subdomains** that are not the motivation for your project. Factor them into general models of the generic subdomains that have no trace of your specialties, and place them in separate packages. Consider off-the-shelf solutions or published models for these subdomains i.e. purchase options, open-source code.

Once they have been separated, give their continuing development **lower priority** than the core domain, and avoid assigning your core developers to the tasks (since they will gain little domain knowledge).

Generic subdomains are the place to **try to apply outside design expertise**, since they do not require deep understanding of your specialized core domain, and do not present a major opportunity to learn that domain. **Confidentiality is less of a concern**, since little proprietary information or business practice will be involved in these modules. A generic subdomain lessens the training burden for those not committed to deep knowledge of the domain.

### Generic doesn't mean reusable

You should specifically **not concern yourself with the reusability of that code**. This would go against the basic motivation of distillation – that you should be applying as much of your effort to the core domain as possible and investing only as necessary in supporting generic subdomains.
