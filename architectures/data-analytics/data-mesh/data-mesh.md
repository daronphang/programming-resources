## Data mesh

Data mesh is a sociotechnical approach to sharing, accessing, and managing analytical data in a decentralized fashion. It satisfies a wide range of analytical use cases, such as reporting, ML model training, and generating insights. Contrary to data lake and data warehouse, it aligns the architecture and ownership of the data with the business domains and enabling a peer-to-peer consumption of data.

## Characteristics

### Domain ownership of data

Data is owned and shared by the domains that are most intimately familiar with the data: domains that are either originating the data, or first-class consumers of the data.

### Data as a product

To prevent siloing of data and encourage domains to share their data, data mesh introduces the concept of data served as a product. It puts in place the organizational roles and success metrics necessary to ensure that domains provide their data in a way that delights the experience of data consumers across the organization.

This principle leads to the introduction of a new architectural quantum called **data product quantum**, to maintain and serve discoverable, understandable, timely, secure, and high-quality data to the consumers.

### Self-serve data platform

To empower the domain teams to build and maintain their data products, data mesh introduces a new set of self-serve platform capabilities. The capabilities focus on improving the experience of data product developers and consumers. It includes features such as declarative creation of data products, discoverability of data products across the mesh through search and browsing, and managing the emergence of other intelligent graphs, such as lineage of data and knowledge graphs.

### Computational federated governance

This principle assures that despite decentralized ownership of the data, organization-wide governance requirements (compliance, security, privacy) are met consistently across all domains.

Data mesh introduces a federated decision-making model composed of domain data product owners. The policies they formulate are automated and embedded as code in each and every data product. The architectural implication of this approach to governance is a platform-supplied embedded sidecar in each data product quantum to store and execute the policies at the point of access: data read or write.
