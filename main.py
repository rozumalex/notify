from aiohttp import web
import logging

import aiohttp_session
import base64
from aiohttp_session.cookie_storage import EncryptedCookieStorage

import jinja2
import aiohttp_jinja2

from notify.settings import config, SECRET_KEY, TEMPLATES_DIR
from notify.db import init_pg, close_pg

from auth.middlewares import request_account_middleware, error_middleware

from routes import routes

from pprint import pprint


def init_app():

    logging.basicConfig(level=logging.DEBUG)

    secret_key = base64.urlsafe_b64decode(SECRET_KEY)

    middlewares = [
        aiohttp_session.session_middleware(EncryptedCookieStorage(secret_key)),
        request_account_middleware,
        error_middleware
    ]
    app = web.Application(middlewares=middlewares)
    app.config = config

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(TEMPLATES_DIR)))

    for setup_route in routes:
        setup_route(app)


    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    web.run_app(app)