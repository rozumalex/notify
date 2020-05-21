from notify import db


class Task:

    def __init__(self, data):
        self.id = data['id'] if 'id' in data else None
        self.name = data['name']
        self.enabled = True if data.get('enabled') else False
        self.account_id = data['account_id']


    async def create(self, pool):
        return await db.create_task(pool, self)