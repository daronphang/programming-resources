## Strategic design

As systems grow too complex to know completely at the level of individual objects, we need techniques for manipulating and comprehending large models.

Strategic design principles provide a guide to design decisions for the model that reduce interdependence of parts and improve clarity and ease of understanding and analysis without reducing their interoperability and synergy.

### Bounded context

A successful model, large or small, has to be logically consistent throughout, without any contradictory or overlapping definitions. Bounded contexts allow work to proceed in different parts without corrupting the model or unintentionally fragmenting it.

### Distillation

Distillation reduces the clutter and focuses the attention appropriately. The **overall domain model needs to make prominent the most value-adding** and special aspects of your system, and be structured to give that part as much power as possible. While some supporting components are critical, they must be put into their proper perspective. This helps to direct efforts towards vital parts of the system and keeps the vision from being lost.

### Large-scale structure

Large-scale structures allow system-wide design elements and patterns to be applied. It can bring consistency to the disparate parts to help those parts mesh.
