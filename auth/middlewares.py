import aiohttp_jinja2
from aiohttp import web
from aiohttp_session import get_session

from auth import db
from auth.exceptions import AccountNotFound


async def request_account_middleware(app, handler):
    async def middleware(request):
        request.session = await get_session(request)
        request.account = None
        account_id = request.session.get('account_id')
        if account_id is not None:
            try:
                request.account = await db.get_account_by_id(app.pool,
                                                             account_id)
            except AccountNotFound:
                request.session.pop('account_id')
        return await handler(request)
    return middleware


async def handle_403(request):
    return aiohttp_jinja2.render_template('403.html', request, {})


async def handle_404(request):
    return aiohttp_jinja2.render_template('404.html', request, {})


async def handle_500(request):
    return aiohttp_jinja2.render_template('500.html', request, {})


def create_error_middleware(overrides):

    @web.middleware
    async def error_middleware(request, handler):

        try:
            response = await handler(request)
            override = overrides.get(response.status)
            if override:
                return await override(request)

            return response

        except web.HTTPException as e:
            override = overrides.get(e.status)
            if override:
                return await override(request)
            raise

    return error_middleware


error_middlewares = create_error_middleware({
    403: handle_403,
    404: handle_404,
    500: handle_500
})
