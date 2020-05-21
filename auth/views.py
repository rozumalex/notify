from aiohttp import web
import aiohttp_jinja2

from auth.models import Account
from auth.decorators import login_required, anonymous_required
from auth.tools import redirect
from auth.exceptions import ValidationError, LoginError, AccountNotFound

from auth import db
from notify import db as notify_db

class Signup(web.View):

    @anonymous_required
    @aiohttp_jinja2.template('signup.html')
    async def get(self):
        return {'session': self.session}

    @anonymous_required
    @aiohttp_jinja2.template('signup.html')
    async def post(self):
        data = await self.post()

        try:
            account = Account(data)
        except ValidationError as e:
            return {'session': self.session, 'error': e}

        try:
            account_id = await account.create(self.app.pool)
        except Exception as e:
            return {'session': self.session, 'error': e}
        await notify_db.create_tasks_table(self.app.pool, account_id)

        self.session['account_id'] = account_id
        raise redirect(self, 'index')

class Login(web.View):

    @anonymous_required
    @aiohttp_jinja2.template('login.html')
    async def get(self):
        return {'session': self.session}

    @anonymous_required
    @aiohttp_jinja2.template('login.html')
    async def post(self):
        data = await self.post()

        try:
            account = await db.get_account_by_email(self.app.pool, data['email'])
        except LoginError as e:
            return {'session': self.session, 'error': e}

        try:
            account.check_password(data['password'])
        except LoginError as e:
            return {'session': self.session, 'error': e}

        self.session['account_id'] = account.id
        raise redirect(self, 'index')

class Logout(web.View):

    @login_required
    async def get(self):
        self.session.pop('account_id')
        raise redirect(self, 'login')


class Profile(web.View):

    @login_required
    @aiohttp_jinja2.template('profile.html')
    async def get(self):
        return {'session': self.session, 'account': self.account}

    @login_required
    @aiohttp_jinja2.template('profile.html')
    async def update(self):
        data = await self.post()
        try:
            await self.account.update_personal_info(self.app.pool, data)
        except ValidationError as e:
            return {'session': self.session, 'account': self.account, 'error': e}
        raise redirect(self, 'profile')


    @login_required
    @aiohttp_jinja2.template('delete_account.html')
    async def get_delete(self):
        return {'session': self.session, 'account': self.account}

    @login_required
    async def delete(self):
        data = await self.post()
        try:
            await self.account.delete(self.app.pool, data)
        except LoginError as e:
            return {'session': self.session, 'account': self.account, 'error': e}
        else:
            self.session.pop('account_id')
            raise redirect(self, 'login')

    @aiohttp_jinja2.template('profile_view.html')
    async def view(self):
        try:
            account = await db.get_account_by_id(self.app.pool, self.match_info['id'])
        except AccountNotFound as e:
            raise web.HTTPNotFound
        return {'session': self.session, 'account': account}