## Webhooks (HTTP push API)

A webhook is an HTTP-based callback function that allows lightweight, event-driven communication between 2 APIs. It is a way for an app to provide other applications with real-time information. A webhook delivers data to other apps as it happens, unlike typical APIs where you would need to poll for data very frequently to get it in real-time. They have a message/payload and are sent to a unique URL i.e. phone number or address.

Webhooks are sometimes referred to as reverse APIs because they put the responsibility of communication on the server, rather than the client.

### Webhooks vs APIs

The following is a breakdown of the differences:

- Direction: Webhooks push data automatically based on events, while APIs exchange data based on explicit requests in push/pull process
- Trigger: Webhooks are event-driven, APIs are request-driven
- Use cases: Webhooks are used for real-time notifications, while APIs handle a wide range of operations like data retrieval and updates
- Configuration: Webhooks need configuration for specific events and endpoints
- Frequency: Webhooks operate in real-time, APIs operate based on the frequency of requests
- Security: Webhooks push data to exposed endpoints and require security measures, APIs often demand authentication for data access

### Consuming

The first step in consuming a webhook is giving the webhook provider a URL to deliver a request. Most webhooks will POST data to you in JSON or XML.

### Security

As webhooks deliver data to publicly available URLs, there is a chance that someone else could find that URL and then provide you with false data. To preven this, you could employ the following:

- Force TLS connections
- Add tokens to the URL that act as unique identification
- Have the provider to sign each request and verify the signature
