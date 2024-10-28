## DASH (Dynamic Streaming over HTTP)

Netflix uses DASH protocol for streaming. Each video is encoded at several different quality levels, and is divided into small chunks, which are video segments of no more than a few seconds in length.

The client requests one video chunk at a time via HTTP. With each download, it measures the received bandwidth and runs a **rate determination algorithm** to determine the quality of the next chunk to request. DASH allows the player to freely switch between different quality levels at the chunk boundaries.
