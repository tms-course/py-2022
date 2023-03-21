import aiohttp_jinja2
import jinja2
from aiohttp import web

from settings import BASE_DIR, PORT
from adapters.persistence.db import async_session

def setup_external_libraries(app: web.Application) -> None:
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(f'{BASE_DIR}/templates'),
    )

def setup_routes(app: web.Application) -> None:
    from adapters.routes import setup_routes as setup_forum_routes

    setup_forum_routes(app)

def setup_app(app: web.Application) -> None:
    setup_external_libraries(app)
    setup_routes(app)


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app, port=PORT)
