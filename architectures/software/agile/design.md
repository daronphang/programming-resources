## Agile design

In non-agile environments, designs degrade because requirements change in ways that the initial design did not anticipate. Often, these changes need to be made quickly, and they may be made by developers who are not familiar with the original design philosophy.

However, we cannot blame the drifting of the requirements for the degradation of the design. As software engineers, we know that requirements change. If our designs are failing due to the constant rain of changing requirements, it is our designs and practices that are at fault. We must somehow find a way to make our designs resilient to such changes and employ practices that protect them from rotting.

### Symptoms of poor design

- Rigidity: The design is hard to change
- Fragility: The design is easy to break
- Immobility: The design is hard to reuse
- Viscosity: It is hard to do the right thing
- Needless complexity: Overdesign
- Needless repetition: Design contains repeating structures that could be unified under a single abstraction
- Opacity: Hard to read and understand, does not express its intent well
