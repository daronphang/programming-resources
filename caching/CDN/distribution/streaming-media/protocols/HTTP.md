## Progressive Download (PD)

PD is the predecessor of HTTP Streaming, which transfers files using HTTP protocol:

1. When a user plays a video, it will send a video file to the user
2. The user can play without waiting for the entire file to be downloaded
3. If the user stops playing, the download continues (wastes bandwidth)

PD incurs **significant bandwidth wastage**, especially during peak periods. Moreover, PD pins down the video with a designated resolution; depending on the user's network quality, the user may run into buffering if network is poor. For these reasons, HTTP streaming was proposed.

## HTTP Streaming

RTSP/RTP and HTTP Streaming are currently the most widely used streaming protocols. HTTP Streaming first encodes visual data on the server (live video streams, on-demand video files), finely grains the encoded data, and finally transmits each segment through HTTP protocol.

Unlike PD, the client needs to send a HTTP request to each sub-file of the video file. This gives the client flexibility and control over the download.

### How it works

The underlying idea is as follows:

- Manifest files are used to describe relevant aspects of the media content as a whole
- Video content with multiple resolutions are divided into data units (segments), which are encoded and stored
- HTTP GET request is used as the primary protocol for client-server interaction, both for manifests and media segments
- When the user plays a video, the stored video strategically uses the network information to provide the user with optimized streaming service
- If the user's network is performing poorly, the user has the option of streaming content with lower resolution, and switching back to higher resolution once network has been stabilized

### RTSP/RTP vs HTTP Streaming

- HTTP Streaming is based on TCP for transmission, which can use TCP's flow control mechanism to adapt to bandwidth changes
- Can save the played content in the client
- Can directly use port 80 to transmit streaming media; this is useful when crossing firewalls that only allow port 80
- Uses HTTP protocol and hence, only requires a standard HTTP server to support

## Mainstream camps

Currently, the mainstream camps of HTTP Streaming include: 3GPP Adaptive HTTP Streaming, Microsoft IIS Smooth Streaming, Adobe HTTP Dynamic Streaming, and Apple HTTP Live Streaming.

### Adaptive HTTP Streaming

The main purpose is to adapt/react to the user's network status to stream the content.
