## Associations

The interaction between **modeling and implementation** is particularly tricky with the associations between objects. In real life, here are lots of many-to-many associations, and many are naturally bi-directional. However, these associations complicate implementation and maintenance, uncommunicative and difficult to implement.

Three ways of making associations more tractable are:

- Imposition of a traversal direction (one-to-many)
- Addition of a qualifier, effectively reducing multiplicity
- Elimination of non-essential associations

It is important to **constraint relationships as much as possible**. Adding a traversal direction reduces interdependence and simplifies the design.
