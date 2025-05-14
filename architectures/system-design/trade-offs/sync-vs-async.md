## Sync vs async processing

### Sync

- Tasks are executed sequentially and client waits for the server to finish before continuing (blocking)
- Simpler for tasks that need immediate confirmation
- Slow down system and can create bottlenecks
- Good for request/response APIs, transactional systems

### Async

- Tasks are executed independently (background)
- Can handle higher concurrency and generally perform more efficiently, especially for I/O heavy tasks
- Suitable for handling high volumes of requests
- Error handling and flow control are more complex
- Good for event-driven architecture, background jobs, real-time systems
