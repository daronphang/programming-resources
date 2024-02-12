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
