## Open host service

When a subsystem has to be integrated with many others, customizing a translator for each can bog down the team. There is more to maintain, and more to worry about when changes are made.

Hence, you should define a protocol that gives access to your subsystem as a **set of services**. Open the protocol so that all who need to integrate with you can use it. Enhance and expand the protocol to handle new integration requirements, except when a single team has idiosyncratic needs. Then, use a one-off translator to augment the open protocol so that the protocol can stay simple and coherent.

It is a lot harder to design a protocol clean enough to be understood and used by multiple teams, so it only pays off when the subsystem’s resources can be described as a cohesive set of services and when there are a significant number of integrations.

### Published language

The translation between the models of two bounded contexts requires a common language.

When businesses want to exchange information with one another, it is unrealistic to expect one to adopt the domain model of the other. Also, it may be undesirable for both parties.

**Direct translation to and from the existing domain models may not be a good solution**. Those models may be overly complex or poorly factored.

The open host service is a basic use of a standardized protocol for multiparty integration. It employs a model of the domain for interchange between systems, even though that model may not be used internally by those systems. It is important to use a well-documented shared language that **can express the necessary domain information as a common medium of communication**, translating as necessary into and out of that language.
