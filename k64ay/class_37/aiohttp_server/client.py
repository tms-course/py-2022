import asyncio
from aiohttp import ClientSession, WSMsgType

async def connect() -> None:
    session = ClientSession()
    async with session.ws_connect('http://localhost:7000/ws') as ws:
        await ws.send_str('Hello, my server')

        async for msg in ws:
            print(msg)
            if msg.type == WSMsgType.TEXT:
                ...
            elif msg.type == WSMsgType.CLOSED:
                break
            elif msg.type == WSMsgType.ERROR:
                break


async def main() -> None:
    await asyncio.create_task(connect())

if __name__ == '__main__':
    asyncio.run(main())