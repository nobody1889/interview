import aiohttp
import asyncio

async def main():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.telegram.org") as resp:
                print(resp.status)
                print(await resp.text()[:100])
    except Exception as e:
        print("Network error:", e)

asyncio.run(main())

