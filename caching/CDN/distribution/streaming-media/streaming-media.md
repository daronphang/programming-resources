## Streaming media

Streaming media is often referred to as the **combination of multimedia technology and network technology** i.e. a multimedia file that is compressed, encoded, streamed, and transmitted to the user through network for playback. Multimedia is a medium for storing, disseminating, and presenting information that integrates various but interrelated media, such as sound, video, graphics, animation, etc. As the bandwidth bottleneck encountered in transmitting streaming media is eliminated, streaming media traffic has replaced web content as the main traffic on the Internet.

Streaming media technology is not a single but comprehensive solution that integrates streaming media data acquisition, compression, encoding, storage, transmission, playback, network communication, etc.

### How multimedia files are played

All players (Baoying Yingsheng, Media Player, RealPlayer) have similar principles for playing videos:

1. File acquisition, refers to the system reading multimedia files from the hard disk to memory buffer
2. Demux (de-multiplexing) separates audio and video that are usually combined together to facilitate transmission. Demux is required as audio and video are encoded separately during production
3. Decoding the compressed and encoded audio and video
4. Output audio and video

## Streaming media acceleration vs web acceleration

Streaming media business has real-time, continuity and timing characteristics. As streaming media is divided into segments, startup delay is shortened significantly, and also it does not require much cache capacity.

The key difference is the technology implemented in transmission.

### Content type

Web content (text, images, animations) are provided to users in static files. This requires the entire content to be downloaded before it can be displayed. On the other hand, streaming media does not have a fixed size, and content can be downloaded simultaneously while playing.

### User behavior

Streaming media allows for playback control e.g. drag, fast forward, pause, play, etc.

### Content management requirements

Web content normally has copyrights, and companies need to purchase copyrights. Hence, they have shorter lifespans as companies are not willing to spend money on videos that have low popularity.

In contrast, streaming media files are large in size, small in quantity, and have a long lifespan. Hence, streaming media CDN adopts different design methods in terms of content management, such as establishing a mapping relationship between content names and internal URLs, managing file clips, regularly judging the popularity of content, and storing a large amount of content in cache devices.

### Back-to-source (backtracking) requirements

Due to the high bandwidth requirements for streaming media file transmission and the need to maintain long TCP connections (session persistence), if the CDN backtracking ratio is too high, the server will be overwhelmed. On the other hand, web content has a shorter lifespan and fast file acquisition, and there is no problem with larger backtracking ratio.

For streaming media content, system generally chooses to pre-distribute hot content using PUSH method, while ordinary web content is almost 100% using PULL method.
