## Architecture

The streaming media CDN system generally conforms to the general architecture of CDN systems.

## Subsystems

### Management support

The management support system is the network management and business management system of the CDN system.

The network management provides topology management, node management, facility management, configuration management, fault management, performance management, and network security management. This module is not only responsible for providing the daily operation and maintenance, but also for **collecting real-time statistical data** required to execute business policies e.g. scheduling policy execution for GSLB, configuring business attributes throughout the network, and allocating network and capability resources.

The operations management is responsible for customer management, customer self-service implementation, product/business capability management, order management, certification management, billing and settlement management, etc. These functions make it possible for the CDN system to provide services and sales to the outside world, and also provide a friendly business operation interface for CDN customers.

Statistical analysis includes daily management functions, data filtering, analysis functions, and report generation performance. The statistical analysis function should conduct statistical analysis on the operation and service of the CDN network according to different indicators, and present it to customers in a flexible and targeted way. For example, website customers may be more concerned about where their website users are distributed, what content people in these areas like and dislike, and the planning of content procurement. These data can only be extracted from the CDN, and it is difficult for the website itself to obtain them. Therefore, the statistical analysis results of the CDN system have very important reference value for customers.

The business interface is responsible for interface adaptation with other systems, including interfaces with external BOSS systems, interfaces with portal systems, and providing self-service interfaces to SP.

### Load balancing

The load balancing subsystem is responsible for user access scheduling. It executes a pre-set load balancing strategy based on the user's location, device load, content location, etc.

**Content hits** is placed as higher priority compared to other heuristics, as the volume of streaming media content files is large and business quality requirements are high. If content is pulled from other nodes, it may bring additional delays and affect user experience. To improve hit rate, CDN systems generally adopt pre-PUSH strategy for hot content. Hence, there will be **more frequent interactive queries** between the load-balancing subsystem and content management subsystem.

As streaming media CDN systems are usually larger in scale and have more nodes, the scheduling accuracy is required to be higher than that of traditional Web CDN, which puts **higher requirements on the performance, algorithm, and flexibility of the load balancing sub-system**.

### Streaming media service

The streaming media service subsystem is composed of various devices that provide services to users, such as cache devices and peripheral network devices that perform resource statistics on clusters and devices, and communicate with load-balancing and operation management subsystems. The main focus of this module is to adapt to different streaming media protocols, encoding formats, players, and business quality requirements.

Generally, CDN providers adopt a vertical deployment of business capabilities i.e. **uniformly deploying separate business capabilities from the central cache, to the regional cache, and edge cache**. Vertical deployment is more conducive to system function expansion and daily operation and maintenance. The business capabilities can be subdivided according to the adaptation of different streaming media protocols, the ability to provide services to users, as well as according to large business categories such as live and on-demand. As business capabilities often have significant differences in implementation methods, equipment requirements, network organization methods, they **cannot cross-communicate with each other**.

### Content management

The content management subsystem is responsible for managing the content distribution of the entire CDN network i.e. ensures reasonable distribution of hot and cold content throughout the CDN network. From the moment content enters the CDN network, this module is responsible for preprocessing the content to meet the internal distribution and business requirements of the CDN. It also manages the **content location** for content positioning during user access scheduling.
