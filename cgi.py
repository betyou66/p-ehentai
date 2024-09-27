#基类应该尽量简单明了
import asyncio,re,socket,threading
loop = asyncio.new_event_loop()
async def ma():
    await asyncio.sleep(3)
    print(5)

async def op():
    await asyncio.sleep(2)
    print('io')

asyncio.run(ma())
loop.run_until_complete(loop.create_task(op()))
