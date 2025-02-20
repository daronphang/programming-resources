## Structure your logs appropriately

A typical microservices-based application might include several technology stacks. Should use a common structure across all services i.e. | as delimiter.

## Use a centralized log storage

Different services may span across different servers, and it would be a daunting task to implement logging in each microservice. Logs can be pushed to a centralized location so that they can be accessed in one place.

## Logs should be queryable

Use a correlation ID that is passed from one service to another if it is being called.

If using HTTP for API calls, can pass correlation ID in headers as 'X-Request-ID' or 'X-Correlation-ID'.

## Provide informative application logs

Logs should include the following information at bare minimum:

- Service name
- Username
- IP address
- Correlation ID
- Message received time in UTC
- Time taken
- Method name
- Call stack

### Dumping requests and responses into log

Convert request into a curl command and dump it into logs.

```
[base.HertzClientTrafficLogger] hertz client request @2025-02-12 16:40:58.555085899 +0800 CST m=+2297533.704809214: curl -X 'POST' -d '{"service_id":780248293753810,"aggr_event_id":8174968}' -H 'Content-Length: 54' -H 'Content-Type: application/json' -H 'Destination-Service: data.ti.cdn_info_strategy' -H 'Host: data.ti.cdn_info_strategy' -H 'Rpc-Persist-Host: ti.byted.org' -H 'Rpc-Persist-Ori-Path: /api/v1/services/cobra' -H 'Rpc-Persist-Ori-Psm: data.ti.agw' -H 'Rpc-Persist-Path: /api/v1/services/cobra' -H 'Rpc-Persist-Psm: data.ti.agw' -H 'Rpc-Persist-Service-Level: 32893' -H 'X-Jwt-Token: eyJhbGciOiJS' -H 'X-Tt-Env: prod' -H 'X-Tt-Logid: 202502121640588C4B08A59F62FB68B59F' 'http://[2605:340:cd51:2108:d3de:cfa3:fcba:a5f5]:9601/api/v1/plan/trigger/_search'
```
