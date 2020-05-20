from aiohttp import web


def redirect(request, router_name, **kwargs):
    url = request.app.router[router_name].url_for(**kwargs)
    return web.HTTPFound(url)

