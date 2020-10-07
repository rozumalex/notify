import asyncpg
from datetime import datetime


async def init_pool(app) -> None:
    config = app.config['postgres']
    pool = await asyncpg.create_pool(
        database=config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
    )
    app.pool = pool
    try:
        await create_accounts_table(app.pool)
    except asyncpg.exceptions.DuplicateTableError:
        pass


def db_connector(func):
    """Декоратор перехватывает пул и отдает соединение"""
    async def wrapped(pool, request, *args, **kwargs):
        async with pool.acquire() as connection:
            async with connection.transaction():
                return await func(connection, request, *args, **kwargs)
    return wrapped


async def create_accounts_table(conn):
    table_name = 'accounts'
    await conn.execute(f'''
            CREATE TABLE {table_name}(
                id serial PRIMARY KEY,
                email text UNIQUE NOT NULL,
                password bytea NOT NULL,
                full_name text,
                phone text,
                registration_date timestamp NOT NULL
            )
        ''')
    print(f'{datetime.now().strftime("%H:%M")} table {table_name} created')


async def create_tasks_table(conn, account_id):
    table_name = f'id_{account_id}_tasks'
    await conn.execute(f'''
            CREATE TABLE {table_name}(
                id serial PRIMARY KEY,
                name text UNIQUE NOT NULL,
                enabled boolean NOT NULL
            )
        ''')
    print(f'{datetime.now().strftime("%H:%M")} table {table_name} created')
