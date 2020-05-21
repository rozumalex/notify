from datetime import datetime

from notify.models import Task


async def create_tasks_table(conn, account_id):
    table_name = f'id_{account_id}_tasks'
    await conn.execute(f'''
            CREATE TABLE {table_name}(
                id serial PRIMARY KEY,
                name text UNIQUE,
                enabled boolean
            )
        ''')
    print(f'{datetime.now().strftime("%H:%M")} table {table_name} created')


async def create_task(conn, task: Task):
    await conn.execute(f'''
        INSERT INTO id_{task.account_id}_tasks(name, enabled) VALUES($1, $2) RETURNING *
    ''', task.name, task.enabled)


async def get_all_tasks(conn, account_id):
    result = await conn.fetch(f'''
        SELECT * FROM id_{account_id}_tasks
    ''')
    return result


async def delete_task(conn, task_id):
    pass


async def update_task(conn, task_id):
    pass
