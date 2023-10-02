## CDN (Content Delivery Network)

A globally-distributed network of caching (edge) servers that are deployed to efficiently deliver content to users worldwide. Objective is to **reduce latency and increase availability** of website or application.

A properly configured CDN can also help to protect websites against common malicious attacks by integrating with AWS Shield i.e. DDoS.

## Amazon CloudFront

A globally-distributed network (CDN) offered by AWS, which securely transfers content including software, SDKs, videos, etc. to clients, with high transfer speed.

### Benefits

- Caches your content in edge locations and decreases workload (high availability)
- Simple to use and ensures productivity enhancement
- Provides high security with 'Content Privacy' feature
- Facilitates GEO targeting service for content delivery to specific end-users
- Uses HTTP/HTTPS protocols for quick delivery of content
- Less expensive and charges only for data transfer
- Reduces file sizes using tactics including minification and file compression

### Steps

1. Client accesses a website and downloads a file
2. DNS routes client's request to the nearest edge location through CloudFront to serve the user's request
3. At edge location, CloudFront looks for the requested cache file
4. If not found,CloudFront compares the requirements with the specifications and shares it with the respective server
5. Web server responds by sending the files back to the CloudFront edge location
6. CloudFront shares it with the client and caches the file
