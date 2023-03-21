from datetime import datetime
from aiohttp import web 

from .persistence.db import async_session
from .persistence.repos.message import MessageRepo

routes = web.RouteTableDef()

@routes.get('/messages')
async def list_messages(request):
    async with async_session() as session:
        msg_repo = MessageRepo(session)
        messages = await msg_repo.list()

        return web.json_response([
            {
                'id': m.id, 
                'text': m.text, 
                'created_at': m.created_at.strftime('%Y-%m-%d %H:%M:%S')
            } for m in messages
        ])

@routes.post('/messages')
async def create_message(request):
    data = await request.json()

    async with async_session() as session:
        msg_repo = MessageRepo(session)
        message = await msg_repo.create(text=data['text'])

        return web.json_response({
            'id': message.id, 
            'text': message.text, 
            'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })


def setup_routes(app: web.Application) -> None:
    app.add_routes(routes)