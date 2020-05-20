from aiohttp import web
from aiohttp_session import get_session
import aiohttp_jinja2

from auth.models import Account
from auth.decorators import login_required, anonymous_required
from auth.tools import redirect
from auth.exceptions import ValidationError, LoginError

from notify import db
from pprint import pprint

class Signup(web.View):

    @anonymous_required
    @aiohttp_jinja2.template('signup.html')
    async def get(self):
        return {}

    @anonymous_required
    @aiohttp_jinja2.template('signup.html')
    async def post(self):
        data = await self.post()

        try:
            account = Account(data)
        except ValidationError as e:
            return {'error': e}

        try:
            account_id = await account.create(self.app.db)
        except Exception as e:
            return {'error': e}

        self.session['account_id'] = account_id
        raise redirect(self, 'index')

class Login(web.View):

    @anonymous_required
    @aiohttp_jinja2.template('login.html')
    async def get(self):
        return {}

    @anonymous_required
    @aiohttp_jinja2.template('login.html')
    async def post(self):
        data = await self.post()

        try:
            account = Account(await db.get_account_by_email(self.app.db, data['email']))
        except LoginError as e:
            return {'error': e}

        try:
            account.check_password(data['password'])
        except LoginError as e:
            return {'error': e}

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
        return self.__dict__

    @login_required
    @aiohttp_jinja2.template('profile.html')
    async def update(self):
        data = await self.post()
        try:
            await self.account.update_personal_info(self.app.db, data)
        except ValidationError as e:
            result = {}
            result['error'] = e
            result.update(self.__dict__)
            return result
        raise redirect(self, 'profile')


    @login_required
    @aiohttp_jinja2.template('delete_account.html')
    async def get_delete(self):
        return self.__dict__

    @login_required
    async def delete(self):
        data = await self.post()
        try:
            await self.account.delete(self.app.db, data)
        except LoginError as e:
            result = {}
            result['error'] = e
            result.update(self.__dict__)
            return self.__dict__
        else:
            self.session.pop('account_id')
            raise redirect(self, 'login')