## Core domain

In designing a large system, there are so many contributing components, all complicated and all absolutely necessary to success, that the essence of the business model, the real business asset, can be obscured and neglected.

A system that is **hard to understand is hard to change or extend**, and the effect of a change is hard to foresee. The consequences of this include:

- Forcing people to specialize; when developers confine their work to specific modules it further **reduces knowledge transfer**
- With compartmentalization of work, smooth integration of the system suffers, and flexibility of assigning work is lost
- Duplication crops up because a developer does not realize that some behavior already exists elsewhere, and so the system becomes even more complex

However, the harsh reality is that not all parts of the design are going to be equally refined. Priorities must be set.

Those parts of the model distinctive and central to the purposes of the intended applications make up the **core domain**. The core domain is where the **most value should be added in your system**.

### Domain vision

Many projects write “vision statements” for management. The best of these documents lay out the **specific value the application will bring to the organization**. Some of these describe the creation of the domain model as a strategic asset. Usually the vision statement document is abandoned after the project gets funding, and is never used in the actual development process or even read by the technical staff.

However, these documents can be used directly by the management and technical staff during all phases of development to **guide resource allocation, to guide modeling choices, and to educate team members**. If the domain model serves many masters, you can use this document to show how their interests are balanced.

#### Example

Airline booking system.

The model can represent passenger priorities and airline booking strategies and balance these based on flexible policies. The model of a passenger should reflect the “relationship” the airline is striving to develop with repeat customers. Therefore, it should represent the history of the passenger in useful condensed form, participation in special programs, affiliation with strategic corporate clients, etc.
Different roles of different users (e.g. passenger, agent, manager) are represented to enrich the model of relationships and to feed necessary information to the security framework.

Model should support efficient route/seat search and integration with other established flight booking systems.

### Highlighted core

A domain vision statement identifies the core model in broad terms, but leaves the identification of the specific core elements up to the vagaries of individual interpretation. **Unless there is exceptionally high communication on the team, the vision statement alone will have little impact**.

In order to translate the high-level view into a concrete view requires each developer to continually mentally filter the large model to identify the core domain. This constant sifting takes up a lot of concentration, and requires a complete knowledge of the model. Even then, there is no guarantee that two people will choose the same elements, or that the same person will be consistent from day to day. The core domain must be made easier to see.

Even though we may know broadly what constitutes an element of the core domain, we won’t come up with consistent choices from developer to developer or even from one day to the next. As we unravel the model for ourselves, we have no effective way of sharing our discoveries, or even of recording them for ourselves to aide memory. Significant structural changes to the code are the ideal way of identifying the core domain, but not always practical in the short-term.

Two techniques can help to make it easier for everyone to know the core domain.

#### Distillation document

You can create a separate **minimalist document** to describe and explain the core domain. It can include:

- List of the most essential conceptual objects
- Set of diagrams focused on essential objects, and showing the most critical relationships
- Walk through the fundamental interactions at an abstract level
- Use UML class of sequence diagrams
