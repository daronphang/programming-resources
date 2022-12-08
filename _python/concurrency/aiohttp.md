## aiohttp

Compared with requests (blocks three times), aiohttp gives the evenet loop three opportunities to switch context:
- When performing .get(), 'async with' gives guarantee that it does not block and is cleanly finalized.
- When getting response.text(), aiohttp loads only when .get() is executed, hence need to await.
- For ClientSession(), it does not perform I/O when entering the block, but at the end of it, ensuring all resources are closed correctly.

```py
import aiohttp
import asyncio

# 

# requests
response = requests.get('http://python.org')
print(response.text)

# aiohttp
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### Sessions

Best practice is to use a session context manager. Do not create a session per request, and one session per application is sufficient to perform all requests together.

A session contains a connection pool inside. Connection reusage and keep-alives (both are on by default) may speed up total performance.
