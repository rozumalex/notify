from aiohttp import web
import aiohttp_jinja2
from aiohttp_session import get_session

class Index(web.View):

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        return self.__dict__
