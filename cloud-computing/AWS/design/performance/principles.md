## Design principles for performance

### Democratize advanced technologies

- Make technology simple and available by making them as services in the cloud

### Go global in minutes

- Deploy your workload globally
- Bring your services closer to your user base
- Use automation to do so
- Use resiliency/failover to support distribution of load to increase performance

### Use serverless architectures

- Removes the need to maintain underlying servers
- Automated scaling invisible to you is ideal
- Event-driven architectures are not running constantly
- Serverless scales and performs better than managing servers

### Experiment more often

- Try scenarios and improvements with your technology architecture as new ideas and patterns emerge
- Create short-lived pre-production environments where innovation and new ideas are explored
- Make sure you have metrics for existing and new experiments
- Gives you more options and knowledge about what works for your application
- Cost optimization

### Consider mechanical sympathy

- Databases are designed for different purposes
- Compute is designed for different hosting functions
- Use the service for what it was designed for
- Use the bare minimum e.g. CRON job with Lambda and not with an EC2
