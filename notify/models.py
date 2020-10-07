from notify import db
from notify.exceptions import NameValidationError


class Task:

    def __init__(self, data):
        self._validate_all(data)
        self.id = int(data['id']) if 'id' in data else None
        self.name = data['name'] if 'name' in data else None
        self.enabled = True if data.get('enabled') else False
        self.account_id = int(data['account_id'])

    @staticmethod
    def _validate_name(name: str) -> None:
        if len(name) < 3:
            raise NameValidationError

    def _validate_all(self, data):
        if 'name' in data:
            self._validate_name(data['name'])

    async def create(self, pool):
        return await db.create_task(pool, self)

    async def delete(self, pool):
        return await db.delete_task(pool, self)

    async def update(self, pool):
        return await db.update_task(pool, self)
