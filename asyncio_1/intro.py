import asyncio

async def sleeper():
    print('sleeping')
    await asyncio.sleep(1)
