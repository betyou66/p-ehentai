import asyncio
import websockets
from websockets.legacy.server import WebSocketServerProtocol


async def ws_handle(websocket: WebSocketServerProtocol, path: str):
    async for message in websocket:
        da = open('pix/server/'+message,'rb').read()
        await websocket.send(da)


async def main():
    async with websockets.serve(ws_handle, "127.0.0.1", 8001):
        await asyncio.Future()              # run forever


asyncio.run(main())
