## Distribution service

Due to significant differences in content types, user behavior, content updates, and other aspects of caching, different technical routes and implementation methods are needed for performance optimization for different types of content and services. Generally, the distribution service system will be divided into multiple sub-service systems.

Each sub-service system is a distributed service cluster composed of a group of cache or cache clusters with similar functions and distributed deployment in geographical locations, which are independent of each other. The number of devices in each sub-service system cluster varies depending on business development and market needs, ranging from a few dozen to tens of thousands of units, forming a whole to jointly undertake the distribution service work.

### Web acceleration

Web acceleration has gradually expanded from static content acceleration to dynamic content acceleration.

### Streaming Media acceleration

The application focus of CDN technology has gradually shifted to Streaming Media acceleration, focusing on full-network caching and scheduling of video files, and user player action response.

Services can be divided into two categories:

- **Live**: Programs can be synchronized and transmitted on the Internet in the form of Streaming Media
- **On-demand**: Streaming Media is indexed by content category, version, etc. and stores them in segments. Users are not limited by the TV station's broadcast time and content, and can watch the content they want to watch at their own suitable time

### File transfer acceleration

By using distributed PoP points of CDN to provide download services, websites can share the performance pressure and bandwidth pressure of large-scale file downloads with CDN, improving users' download speed.

Currently, CDN technology can support various download methods such as HTTP download, FTP download, and P2P download. It is mainly used for software vendor patch release, antivirus software vendor virus database update, game client download for online game operators, and other websites that provide file download services, such as Yingle website.

### Application protocol acceleration

Application protocol acceleration does not target specific content types, but improves and accelerates the content transmission speed of users on the network by optimizing transmission protocols such as TCP/IP, or accelerates some specific protocols, such as SSL protocol, to solve the performance and response speed problems during secure transmission. Services include:

- **Wide Area Network (WAN)**: Goal is to make the WAN perform like LAN, especially for CIFS and NFS protocols that are greatly affected in WAN. Another goal is to handle various applications and protocols in a variety of distributed enterprise network environments
- **SSL**: SSL applications consume significant resources on the server side. CDN's dedicated SSL acceleration hardware instead completes the encryption and decryption operations. The user's site only needs to trust the CDN
- **Web compression**: Data compression is performed by the server, and decompressed on the user's browser. This method reduces data transmission time and speed up web display speed

## Caching and replication mechanism for different content

Websites can achieve better scalability and high performance with the help of CDN technology. The key lies in the caching and replication mechanisms used by CDN, where caching copies the content owned by the recently accessed source server to the edge server.

There are mainly two types of content: static and dynamic content. Website systems are typically divided logically into three levels: presentation layer, business logic layer, and data access layer. The presentation layer interacts with users directly to provide most of the static content. For dynamic content, it needs to be provided by the collaboration between business logic layer and data access layer.

CDN mainly relies on two mechanisms: **content edge caching** and **function replication** to achieve web content acceleration. Essentially, it transfers the functions at various levels of the web system to the CDN edge cache.

Static content can be accelerated by copying the presentation layer on the edge cache. In implementation, the CDN cache will accept connection requests from users in reverse proxy format, and search for data that meets the user's needs.

For dynamic content acceleration, it is necessary to copy and cache the business logic layer and backend data access layer on the CDN. Among them, the replication of the business logic layer on the CDN cache enables it to undertake tasks such as user request processing, application data calculation, and dynamic content generation. This method is also known as **edge computing**. Installing web applications or application components directly in the CDN cache aims to complete application processing closest to the user, while also sharing the computational pressure of the source site.

However, in some applications, the generation of dynamic content requires a large amount of data support, such as recording services, transaction data, etc. Simply copying business logic to edge servers is not enough to solve the transmission performance bottleneck caused by obtaining the data required to generate dynamic content from the source site. Therefore, **necessary replication of the data access layer is also required** i.e. data access layer is replicated. The key to this process is to reasonably solve the consistency problem between multiple data copies in the system. In addition, some dynamic content of websites is customized and generated based on personalized data of specific users, and special attention needs to be paid to user data at the data access layer.
