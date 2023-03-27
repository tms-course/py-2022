from aiohttp import web


app = web.Application()
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text='Hello World!')



app.add_routes(routes)

web.run_app(app)