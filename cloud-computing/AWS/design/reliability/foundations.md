## Infrastructure architecture

- AWS have service quotas and limits
- Use highly available network connectivity for your public endpoints
- Provision redundant connectivity in your private endpoints
- Ensure IP addresses are not under-allocated or un-managed

## Application architecture

- Segment your works
- Provide service contracts
- Service-oriented architecture
- Heartbeat services
- Failing gracefully
- Throttle API requests
- Limit retry calls e.g. exponential backoff
- Limit queues
- Make services stateless
- Make emergency levers

## Change management

- Monitor all components
- Define metrics
- Send notifications
- Automate responses for elasticity e.g. scale up/down
- Analytics and data display
- Review data and metrics
- Monitor sessions
- Perform loadtesting on your workload
- Add the capability to enable and disable changes
- Limit change to one isolated zone at a time
- Review change capability and improve it
- Automate change with ability to rollback

## Failure management

- Anticipating and planning for failure
- Chaos engineering
