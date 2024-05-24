## Content Delivery Network (CDN)

A globally-distributed network of caching (edge) servers that are deployed to efficiently deliver content to users worldwide. Objective is to **reduce latency and increase availability** of website or application.

A properly configured CDN can also help to protect websites against common malicious attacks by integrating with AWS Shield i.e. DDoS.

## Amazon CloudFront

A globally-distributed network (CDN) offered by AWS, which securely transfers content to clients, with high transfer speed e.g. software, SDKs, static sites, videos, etc.

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
4. If not found, CloudFront compares the requirements with the specifications and shares it with the respective server
5. Web server responds by sending the files back to the CloudFront edge location
6. CloudFront shares it with the client and caches the file

### How it works

If you want to cache an object, you need to configure a **distribution** which is a configuration unit/block in CloudFront. The distribution tells CloudFront where it can find the origin/source files.

A domain name will also be provided from the distribution, and the distribution will be pushed to the edge locations.

### Cache skipping

- Dynamic content with specific headers
- Proxy methods PUT/POST/PATCH/OPTIONS/DELETE

### Time to Live (TTL)

Cached content at an edge locations remains for a set time. TTL value decides the content validity before an edge location requests the origin (default is 24 hours).

**Cache invalidation** allows you to invalidate content cached at edge locations (manual process). Invalidations are performed on a distribution.

```
/*          Invalidate entire distribution
/file.txt   Invalidate an individual file
```

### SSL/TLS

A default domain name will be provided from the distribution created e.g. https://xyz.cloudfront.net. If you want to use custom domain names, you can utilize AWS certificate manager.

## Functions

Running code at edge locations. Can be used to manipulate requests/responses that flow through CloudFront.

### CloudFront

Use cases include cache key normalization, HTTP header manipulation, URL redirects or rewrites, and request authorization.

CloudFront functions are executed:

- When it receives a request from a viewer
- Before it returns the response to the viewer

### Lambda@Edge

Use cases include long-running functions, configurable CPU and memory functions, dependencies on third-party libraries, network dependent functions, and file system or HTTP request access functions.

Lambda@Edge functions are executed:

- When CloudFront receives a request from a viewer
- Before CloudFront forwards a request to the origin
- When CloudFront receives a response from the origin
- Before CloudFront returns the response to the viewer
