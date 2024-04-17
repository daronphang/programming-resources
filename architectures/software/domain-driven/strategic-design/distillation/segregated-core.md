## Segregated core

Elements in the model may partially serve the core and partially play supporting roles. Core elements may be tightly coupled to generic ones. The conceptual cohesion of the core may not be strong or visible. All this clutter and entanglement chokes the core. Designers can’t clearly see the most important relationships, leading to a weak design.

By factoring out generic subdomains, you clear away some of the obscuring detail from the domain, making the core more visible. But it is hard work identifying and clarifying all these subdomains, and some of them don’t seem worth the trouble. Meanwhile, the all important core domain is left entangled with the residue.

**Refactor the model to separate the core concepts from supporting players** (including ill-defined ones) and strengthen the cohesion of the core while reducing its coupling to other code. Factor all generic or supporting elements into other objects and place them into other packages, even if this means refactoring the model in ways that separate highly coupled elements.

The steps to refactor to segregated core typically are something like this:

1. Identify a core subdomain (possibly drawing from the Distillation Document)
2. Move related classes to a new package, named for the concept that relates them
3. Refactor code to sever data and functionality that are not directly expressions of the concept. Put the removed aspects into (possibly new) classes in other packages. Try to place them with conceptually related tasks, but don’t waste too much time being perfect. Keep focused on scrubbing the core subdomain and making the references from it to other packages explicit and self-explanatory
4. Refactor the remaining core to make its relationships and interactions simpler and more communicative, and to minimize and clarify its relationships with other packages
