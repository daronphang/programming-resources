## Edge computing

Edge acceleration refers to enhancing the capabilities of edge nodes (L1 nodes), to do more than just cache and deliver content. One such enhancement is enabling them to parse and execute JS.

### Benefits

1. **Dynamic content handling at edge**: Traditionally, CDNs serve static content. With JS execution at the edge, CDN can dynamically generate/modify responses based on user/device/location/request context, i.e. personalizing content, redirecting based on geolocation, A/B testic logic
2. **Reduced latency and faster TTFB (time to first byte)**: By moving logic closer to users, you eliminate unnecessary round trips to the origin server. For fetch requests, depending on the vendors, edge function can perform a more efficient routing through subrequest, i.e. If the static asset is already cached on the same node, to fetch locally without extra network hop; otherwise it may go to L2 or origin. Additionally, some platforms allow the edge node to directly access cache (edge-to-edge tunnel rather than edge-to-origin), which further reduces latency
3. **Improved resilience and availability**: Even if the origin server is slow or unresponsive, edge node can still serve a fallback or computed response using JS logic
4. **Traffic offloading**: Executing logic at the edge reduces load on your backend systems by handling simple logic (e.g., redirects, rewrites, headers, cookies) locally
5. **Support for modern app architectures**: Many SPAs, SSR frameworks require edge-side rendering, hydration or logic
