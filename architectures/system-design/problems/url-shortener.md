## URL shortener

URL shortening is used to create shorter aliases for long URLs. Users are redirected to the original URL when they hit these short links. Short links save a lot of space when displayed, printed, messaged, or tweeted. Additionally, users are less likely to mistype shorter URLs.

URL shortening is used to optimize links across devices, track individual links to analyze audience, measure ad campaigns' performance, or hide affiliated original URLs.

```
Original: https://www.designgurus.org/course/grokking-the-system-design-interview
Shortened: https://tinyurl.com/vzet59pa
```

## Requirements

### Functional

- Given a URL, our service should generate a shorter and unique alias of it
- When users access a short link, our service should redirect them to the original link
- Users should optionally be able to pick a custom short link for their URL
- Links will expire after a standard default timespan; users should be able to specify the expiration time

## Non-functional

- Highly available
- URL redirection should happen in real-time with minimal latency
- Shortened links should not be guessable i.e. must be unpredictable

## Capacity estimation and constraints (back of the envelope)

System will be read-heavy with many redirection requests as compared to new URL shortenings. Assumptions made are as follows:

- 100:1 ratio between read and write
- 500M new URL shortenings per month
- Data is persisted for 5 years

### Traffic

```
QPS = 500M / (30 days * 24 hours * 3600 seconds) = 200 URLs/second
Redirections = 200 URLs/second * 100 = 20,000/s
```

### Storage

```
500M * 5 years * 12 months = 30 billion
Storage = 30 billion * 500 bytes = 15 TB
```

### Bandwidth

```
Write: 200 URLs/second * 500 bytes = 100 KB/s
Read: 20,000 URLs/second * 500 bytes = 10 MB/s
```

### Memory

To cache hot URLs that are frequently accessed, following 80-20 rule, 20% of URLs generate 80% of traffic.

```
20,000 URLs/second * 3600 seconds * 24 hours = 1.7 billion
1.7 billion * 0.2 * 500 bytes = 170 GB
```

## Algorithm

Assuming we want the URL to be encoded in base64, we can determine the length of short key as follows:

- 6 letters: 64^6 = 68.7 billion combinations
- 8 letters: 64^8 = 281 trillion combinations

From the above, six letters would suffice.

### Encoding with hash

We can compute a unique hash (MD5, SHA256, etc.) of the given URL, followed by encoding it with base64 for display. However, it will produce a 128-bit hash value, and encoding into base64 will return a string more than 21 characters (128 / 6 bits).

Moreover, hashing the same URL would result in the same short key, and this is not desirable.

### Generating keys offline

We can have a standalone Key Generation Service (KGS) that generates random six-letter strings beforehand and store them in a database. Whenever we have a new request to shorten a URL, we can take of the already-generated keys and use it. This approach is simple, fast, and eliminates duplications or collisions.
