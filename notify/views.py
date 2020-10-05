from aiohttp import web
import aiohttp_jinja2

from notify.models import Task
from notify import db

from auth.decorators import login_required
from auth.tools import redirect


class Index(web.View):

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        result = {'session': self.session}
        try:
            tasks = await db.get_all_tasks(self.app.pool, self.account.id)
            result['tasks'] = tasks
        except Exception:
            pass
        return result


class Tasks(web.View):

    @login_required
    @aiohttp_jinja2.template('new_task.html')
    async def get(self):
        return {'account': self.account, 'session': self.session}

    async def create(self):
        data = await self.post()
        task = Task(data)
        await task.create(self.app.pool)
        raise redirect(self, 'index')
