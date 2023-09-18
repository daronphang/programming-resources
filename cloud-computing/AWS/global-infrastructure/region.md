## Region

When selecting the right Region for your services, data, and applications, need to consider several factors. AWS supports three Regions: Standard Regions, China Regions, and AWS GovCloud (US).

### Compliance with data governance and legal requirements

You might need to run your data out of specific areas.

### Proximity to your customers

Selecting a Region that is close to your customers will help you to get content to them faster.

### Available services within a Region

Sometimes, the closest Region might not have all the features that you want to offer to customers. AWS is frequently innovating by creating new services and expanding on features within existing services; however, making new services may require AWS to build out physical hardware one Region at a time.

### Pricing

Tax structures are setup differently in different countries.

## Availability Zones

An Availability Zone is a single data center or a group of data centers within a Region. A Region consists of three or more Availability Zones. Availability Zones are located tens of miles apart from each other. This is close enough to have low latency (time between when content requested and received) between Availability Zones.

If a disaster occurs in one part of the Region, they are distant enough to reduce the chance that multiple Availability Zones are affected.

A best practice is to run applications across at least two Availability Zones in a Region. If one Availability Zone fails, your application would still be up and running.

## Edge Locations

An Edge Location is a site that Amazon CloudFront uses to store cached copies of your content to your customers for faster delivery.

For example:

- Your data is stored in Brazil but your customers are in China
- You don't have to migrate all content to one of the Chinese Regions
- Instead, you cache a copy locally at an edge location that is close to your customers in China
- When a customer requests for data in China, Amazon CloudFront retrieves the file from the cache in the edge location and delivers it to your customer
