## Broadcast Channel API

The Broadcast Channel API allows communication between Tabs, Windows, Frames, Iframes, and Web Workers. One tab can create and post to a channel as follows:

```js
const channel = new BroadcastChannel("app-data");
channel.postMessage(data);
```

Other tabs can listen to the channel as follows.

```js
cost channel = new BroadcastChannel('app-data');
channel.addEventListener('message', (event) => {
    console.log(event.data);
})
```
