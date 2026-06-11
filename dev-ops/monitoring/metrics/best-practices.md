## Low cardinality

Never use a unique ID (like a user_id or request_id) as a label. If you have 1 million users, you'll create 1 million unique metrics, which will crash your metrics server (this is called "Cardinality Explosion").

## Standard units

Always use base units (seconds instead of milliseconds, bytes instead of megabytes). It makes math easier in your dashboards later.
