class QuotaAggregator:
    RESOURCES = [
        'DEVICE_CATEGORY',
        'METRO_QUOTA',
        'RDA_QUOTA',
    ]

    def __init__(self, userinfo: UserInfo, endpoint: str):
        self.userinfo = userinfo
        self.endpoint = endpoint
        self.agg_quota = {}

    async def fetch_resource_task(self, client, resource: str):
        async with client.post(
            urljoin(self.endpoint, resource),
            json={
                'userinfo': json.loads(self.userinfo.json()),
                'payload': {}
            }
        ) as resp:
            payload = await resp.json()
            if resp.status >= 400:
                logger.error(f'unable to fetch resource {resource}: {payload}')
                resp.raise_for_status()
        return (resource, payload)

    async def execute(self):
        async with aiohttp.ClientSession() as client:
            tasks = []
            for r in self.RESOURCES:
                task = asyncio.create_task(self.fetch_resource_task(client, r))
                tasks.append(task)

            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
            for task in done:
                if task.exception():
                    # cancel pending tasks, need to wait for cancellations to propagate
                    for pt in pending:
                        pt.cancel()
                    await asyncio.wait(pending)
                    raise AggQuotaException('unable to fetch quota resources')
                else:
                    (resource, payload) = task.result()
                    self.agg_quota[resource.lower()] = payload

            return self.agg_quota
