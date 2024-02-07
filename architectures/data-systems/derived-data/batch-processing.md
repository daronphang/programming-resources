## Batch Processing

As an example, we have a web server that appends a line to a log file every time it serves a request, and you want to find the five most popular pages on your website.

```log
216.58.210.78 - - [27/Feb/2015:17:55:11 +0000] "GET /css/typography.css HTTP/1.1"
200 3377 "http://martin.kleppmann.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X
10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115
Safari/537.36"
```

### With Unix Tools

Each command all treat their input file as a list of records separated by the \n character.

```console
$ cat /var/log/nginx/access.log | awk '{print $7}' | sort | uniq -c | sort -r -n | head -n 5
```

### With Custom Program

Uses in-memory hashmap.

```py
import heapq

counts = {}

with open('/var/log/nginx/access.log', 'r') as f:
    line = f.readline()
    url = line.split(' ')[6]
    if url in counts: counts[url] += 1
    else: counts[url] = 1

h = []
for k,v in counts.items():
    pq.heappush(h, (k,-v))

for _ in range(5):
    print(heappop(h))
```

### Sorting vs In-Memory Aggregation

The sort utility in GNU Coreutils (Linux) automatically handles larger-than-memory datasets by spilling to disk, and automatically parallelizes sorting across multiple CPU cores. However, sorting implementations in most programming languages do not spill to disk and do not use multiple threads.
