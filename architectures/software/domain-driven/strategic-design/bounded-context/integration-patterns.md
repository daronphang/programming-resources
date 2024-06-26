## Relationships between bounded contexts

If two sets of functionalities have no significant relationship, or call upon each other's functionality, they should be completely cut loose from each other. Even if the features are related in a use-case, does not mean they must be integrated.

**Integration is always expensive, and sometimes the benefit is small**. In addition to the usual expense of coordinating teams, there are compromises that have to be made.

Nonetheless, the following patterns cover a range of strategies for relating two models that can be composed to encompass an entire enterprise. These served the dual purpose of providing targets for successfully organizing development work, and providing vocabulary for describing the existing organization.

### Context map

<img src="../../../assets/ddd-context-map.png">

## Shared kernel

Uncoordinated teams working on closely related applications can produce contexts that may not fit together. They can end up spending more on translation layers and retrofitting than they would have on continuous integration. Nonetheless, it may be too much overhead to fully synchronize the entire model and codebase across teams.

Instead, designate some subset of the domain model that the **two teams agree to share** (shared kernel). This includes the subset of code and database design associated with that part of the model. The goal is to reduce duplication (but not eliminate it), and make integration between two subsystems relatively easy.

The shared kernel **cannot be changed as freely as other stuff**. Decisions involve consultation with another team. Automated test suites must be integrated because all tests from both teams must pass when changes are made.

## Conformist

In some cases the balance of power is in favor of the upstream team, which has no real motivation to support its clients’ needs. Instead, it just provides the integration contract, defined according to its own model: take it or leave it. Such power imbalances can be caused by integration with service providers that are external to the organization, or simply by organizational politics.

If the downstream team can accept the upstream team’s model, the relationship between the bounded contexts is called conformist i.e. the **downstream team conforms to the upstream team’s model**.

## Customer/Supplier development teams

For upstream and downstream subsystems, where the downstream component takes the output from the upstream component, should have translation in a single direction. Yet, problems can emerge in this situation.

If the downstream component has veto power over changes, the upstream team may be cramped and inhibited by worries of breaking the downstream system. Meanwhile, the downstream team can be helpless, at the mercy of upstream priorities.

Downstream needs things from upstream, but upstream is not responsible for downstream deliverables. It takes a lot of extra effort to anticipate what will affect the other team.

Hence, establish a clear customer/supplier relationship between both teams. In planning sessions, the downstream team play the customer role to the upstream team. Negotiate and budget tasks for downstream requirements so that everyone understands the commitment and schedule.

There needs to be an automated test suite that can give the upstream team the ability to change their code without fear of breaking the downstream, and lets the downstream team concentrate on their own work without constantly monitoring the upstream team.

## Anti-corruption layer (ACL)

New systems almost always have to be integrated with legacy systems that will have their own models. When control or communication is not adequate to pull off a shared kernel or customer/supplier development teams, the interface can become complex.

When a new system is being built that must have a large interface with another, the **difficulty of relating the two models can eventually overwhelm the intent of the new model altogether**, causing it to be modified to resemble the other system’s mode, in an adhoc fashion. The models of legacy systems are usually weak, and even the exception that is well developed may not fit the needs of the current project. Yet there may be a lot of value in the integration, and sometimes it is an absolute requirement.

On a large project, one subsystem will often have to interface with several other, independently developed subsystems. These will reflect the problem domain differently. When systems based on different models are combined, **the need for the new system to adapt to the semantics of the other system can lead to a corruption of the new system’s own model**.

If you take some data from one system and misinterpret it in another. You may even corrupt the database. Yet, this problem tends to sneak up on us because we think that what we are transporting between systems is primitive data whose meaning is unambiguous and must be the same on both sides. **This is usually wrong**. Subtle yet important differences in meaning arise from the way the data are associated in each system.

Combining systems with different models has pitfalls, but it is nonetheless unavoidable. A means is needed to provide a **translation between the parts that adhere to different models**, so that the models are not corrupted with undigested elements of foreign models.

An anti-corruption layer (translation layer) is a mechanism that translates conceptual objects and actions from one model and protocol to another. **It is not a mechanism for transporting data from one program to another**.

### How to implement

An anti-corruption layer can be implemented using a facade or adapter layer between different subsystems that don't share the same semantics. The layer can be implemented as a **component within the application** or as an **independent service**.

## Open host service

When a subsystem has to be integrated with many others, customizing a translator for each can bog down the team. There is more to maintain, and more to worry about when changes are made.

Hence, you should define a protocol that gives access to your subsystem as a **set of services**. Open the protocol so that all who need to integrate with you can use it. Enhance and expand the protocol to handle new integration requirements, except when a single team has idiosyncratic needs. Then, use a one-off translator to augment the open protocol so that the protocol can stay simple and coherent.

In a sense, the open-host service pattern is a reversal of the ACL pattern: instead of the consumer, the supplier implements the translation of its internal model.

It is a lot harder to design a protocol clean enough to be understood and used by multiple teams, so it only pays off when the subsystem’s resources can be described as a cohesive set of services and when there are a significant number of integrations.

### Published language

The translation between the models of two bounded contexts requires a common language.

When businesses want to exchange information with one another, it is unrealistic to expect one to adopt the domain model of the other. Also, it may be undesirable for both parties.

**Direct translation to and from the existing domain models may not be a good solution**. Those models may be overly complex or poorly factored.

The open host service is a basic use of a standardized protocol for multiparty integration. It employs a model of the domain for interchange between systems, even though that model may not be used internally by those systems. It is important to use a well-documented shared language that **can express the necessary domain information as a common medium of communication**, translating as necessary into and out of that language.
