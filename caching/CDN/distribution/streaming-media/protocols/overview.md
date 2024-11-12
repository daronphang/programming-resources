## Streaming media transmission protocol

Initially, the Internet was not designed for transmitting media content but textual data:

- Multimedia data requires more bandwidth by several magnitudes as compared to textual data
- Multimedia requires real-time and stable network transmission. Delays in data transmission caused by discarding and recovery make network congestion more severe
- Multimedia streams have **strong bursts**, and increasing bandwidth often cannot solve this problem. Hence, most multimedia applications have a **caching mechanism** at the receiving end that makes reasonable adjustment to the data stream to avoid overflow of program's cache

It is unrealistic to resolve the above challenges as the Internet tends to maintain its technical simplicity and best-effort concept. Hence, designing a streaming media transmission protocol is needed. All protocols are located on the upper layer of TCP/UDP.
