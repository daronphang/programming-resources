## Model integrity

The most fundamental requirement of a model is that it be **internally consistent** (unification); that every term always have the same meaning, and it contains no contradictory rules.

In an ideal world, we would have a single model spanning the whole domain of the enterprise. However, in a world of large systems development, it is not feasible nor cost-effective, and is necessary to allow multiple models to develop in different parts of the system.

To maintain that level of unification, careful choices about which parts of the system will be allowed to diverge and what their relationship to each other will be like need to be made. **We need to make the boundaries and relationships between different models clear**.

### Risks of unified model for a large system

- Too many legacy replacements may be attempted at once
- Large projects may bog down as the coordination overhead exceeds their abilities
- Application with specialized needs may have to use models that don't fully satisfy their needs, forcing them to put behavior elsewhere
- Attempting to satisfy everyone with a single model may lead to complex options that make the model difficult to use

## Bounded context

A model applies in a context. To begin to solve the problems of multiple models, we need to **explicitly define the scope of a particular model** as a bounded part of a software system.

Within the context, work to keep the model logically unified, and do not worry about applicability outside those bounds.

Combining elements of distinct models causes two categories of problems: duplicate concepts and false cognates. **Duplication of concepts** means that there are two model elements that actually represent the same concept. Every time this information changes, it has to be updated in two places with conversions. **False cognates** is the case when two people who are using the same term think they are talking about the same thing, but really are not.

## Context map

An individual bounded context leaves some problems in the absence of a global view. The context of other models may still be vague and in flux. As people on other teams won't be very aware of the context bounds, they may unknowingly make changes that **blur the edges or complicate the interconnections**.

Code reuse between bounded contexts is a hazard to be avoided. Instead, integration of functionality and data **must go through a translation** that defines the relationship between different contexts.

A context map is in the overlap between project management and software design. Both managers and team members need a clear view into of the ongoing conceptual subdivision of the software model and design.

Whatever form the context map takes (textual description, graphical representation, conceptual diagrams, etc.), it must be shared and understood by everyone on the project.

## Relationships between bounded contexts

The following patterns cover a range of strategies for relating two models that can be composed to encompass an entire enterprise. These served the dual purpose of providing targets for successfully organizing development work, and providing vocabulary for describing the existing organization.

### Shared kernel

Uncoordinated teams working on closely related applications can produce contexts that may not fit together. They can end up spending more on translation layers and retrofitting than they would have on continuous integration. Nonetheless, it may be too much overhead to fully synchronize the entire model and codebase across teams.

Instead, designate some subset of the domain model that the **two teams agree to share** (shared kernel). This includes the subset of code and database design associated with that part of the model. The goal is to reduce duplication (but not eliminate it), and make integration between two subsystems relatively easy.

The shared kernel **cannot be changed as freely as other stuff**. Decisions involve consultation with another team. Automated test suites must be integrated because all tests from both teams must pass when changes are made.

### Customer/Supplier development teams

For upstream and downstream subsystems, where the downstream component takes the output from the upstream component, should have translation in a single direction. Yet, problems can emerge in this situation.

If the downstream component has veto power over changes, the upstream team may be cramped and inhibited by worries of breaking the downstream system. Meanwhile, the downstream team can be helpless, at the mercy of upstream priorities.

Downstream needs things from upstream, but upstream is not responsible for downstream deliverables. It takes a lot of extra effort to anticipate what will affect the other team.

Hence, establish a clear customer/supplier relationship between both teams. In planning sessions, the downstream team play the customer role to the upstream team. Negotiate and budget tasks for downstream requirements so that everyone understands the commitment and schedule.

There needs to be an automated test suite that can give the upstream team the ability to change their code without fear of breaking the downstream, and lets the downstream team concentrate on their own work without constantly monitoring the upstream team.

### Anti-corruption layer

New systems almost always have to be integrated with legacy systems that will have their own models. When control or communication is not adequate to pull off a shared kernel or customer/supplier development teams, the interface can become complex.

When a new system is being built that must have a large interface with another, the **difficulty of relating the two models can eventually overwhelm the intent of the new model altogether**, causing it to be modified to resemble the other system’s mode, in an adhoc fashion. The models of legacy systems are usually weak, and even the exception that is well developed may not fit the needs of the current project. Yet there may be a lot of value in the integration, and sometimes it is an absolute requirement.

On a large project, one subsystem will often have to interface with several other, independently developed subsystems. These will reflect the problem domain differently. When systems based on different models are combined, **the need for the new system to adapt to the semantics of the other system can lead to a corruption of the new system’s own model**.

If you take some data from one system and misinterpret it in another. You may even corrupt the database. Yet, this problem tends to sneak up on us because we think that what we are transporting between systems is primitive data whose meaning is unambiguous and must be the same on both sides. **This is usually wrong**. Subtle yet important differences in meaning arise from the way the data are associated in each system.

Combining systems with different models has pitfalls, but it is nonetheless unavoidable. A means is needed to provide a **translation between the parts that adhere to different models**, so that the models are not corrupted with undigested elements of foreign models.

An anti-corruption layer is a mechanism that translates conceptual objects and actions from one model and protocol to another. **It is not a mechanism for transporting data from one program to another**.
