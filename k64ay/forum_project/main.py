from aiohttp import web 

from settings import PORT


def app_factory() -> web.Application:
    from adapters.routes import setup_routes

    app = web.Application()

    setup_routes(app)

    return app


if __name__ == '__main__':
    app = app_factory()
    web.run_app(app, port=PORT)
