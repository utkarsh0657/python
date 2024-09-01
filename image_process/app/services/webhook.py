import aiohttp

async def trigger_webhook(request_id):
    url = "http://example-webhook-url.com"  # Replace with actual webhook URL
    async with aiohttp.ClientSession() as session:
        await session.post(url, json={"request_id": request_id})
