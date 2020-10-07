from aiohttp import web
import aiohttp_jinja2
import asyncpg

from notify.models import Task
from notify import db
from notify.exceptions import ValidationError

from auth.decorators import login_required

from tools import redirect


class Index(web.View):

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        if self.account:
            raise redirect(self, 'tasks')
        result = {'account': self.account, 'session': self.session}
        return result


class Tasks(web.View):

    @login_required
    @aiohttp_jinja2.template('tasks.html')
    async def get_all(self):
        result = {'account': self.account, 'session': self.session}
        tasks = await db.get_all_tasks(self.app.pool, self.account.id)
        result['tasks'] = tasks
        return result

    @login_required
    @aiohttp_jinja2.template('new_task.html')
    async def get_new(self):
        return {'account': self.account, 'session': self.session}

    @login_required
    @aiohttp_jinja2.template('new_task.html')
    async def new(self):
        data = await self.post()

        try:
            task = Task(data)
        except ValidationError as e:
            return {'account': self.account,
                    'session': self.session,
                    'error': e}

        try:
            await task.create(self.app.pool)
        except asyncpg.exceptions.UniqueViolationError as e:
            return {'account': self.account,
                    'session': self.session,
                    'error': e}

        raise redirect(self, 'index')

    @login_required
    @aiohttp_jinja2.template('single_task.html')
    async def view(self):
        task = Task({'id': self.match_info['id'],
                     'account_id': self.account.id})
        result = await db.get_task_by_id(self.app.pool, task)
        return {'account': self.account,
                'session': self.session,
                'task': result}

    @login_required
    @aiohttp_jinja2.template('single_task.html')
    async def update(self):
        data = await self.post()
        try:
            task = Task(data)
        except ValidationError as e:
            return {'account': self.account,
                    'session': self.session,
                    'error': e}

        try:
            await task.update(self.app.pool)
        except asyncpg.exceptions.UniqueViolationError as e:
            return {'account': self.account,
                    'session': self.session,
                    'error': e}

        raise redirect(self, 'index')

    @login_required
    @aiohttp_jinja2.template('single_task.html')
    async def delete(self):
        task = Task({'id': self.match_info['id'],
                     'account_id': self.account.id})
        await db.delete_task(self.app.pool, task)
        raise redirect(self, 'index')
