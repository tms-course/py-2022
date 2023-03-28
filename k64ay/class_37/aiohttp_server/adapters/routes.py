from datetime import datetime

import aiohttp_jinja2
from aiohttp import web, WSMsgType

from .persistence.db import engine, async_session
from .persistence.repos.message import MessageRepo

routes = web.RouteTableDef()

@routes.get('/messages')
async def list_messages(request) -> list:
    async with async_session() as session:
        msg_repo = MessageRepo(session)

        messages = await msg_repo.list()

        print(messages)

        return web.json_response([{'id': m.id, 'text': m.text} for m in messages])
    

@routes.post('/messages')
async def create_message(request):
    data = await request.json()

    async with async_session() as session:
        msg_repo = MessageRepo(session)

        message = await msg_repo.create(text=data['text'])

        return web.json_response({'id': message.id, 'text': message.text})
    
@routes.get('/')
@aiohttp_jinja2.template('chat/index.html')
async def get(request):
    return {}

@routes.get('/ws')
async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    request.app['clients'].append(ws)

    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            print(msg)
            if msg.data == 'close':
                await ws.close()
            else:
                for client in request.app['clients']:
                    if client == ws:
                        continue

                    await client.send_str(msg.data)
        elif msg.type == WSMsgType.ERROR:
            print('WebSocket connection closed with exc %s' % ws.exception())

    print('WebSocket connection closed.')

    return ws

def setup_routes(app: web.Application) -> None:
    app.add_routes(routes)