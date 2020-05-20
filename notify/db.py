import asyncpg
from datetime import datetime

from auth.exceptions import AccountNotFound

from notify.init_db import create_tables


async def init_pg(app):
    config = app.config['postgres']
    engine = await asyncpg.connect(
        database=config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
    )
    app.db = engine
    # await create_tables(app.db)


async def close_pg(app):
    app.db.close()
    await app.db.wait_closed()


async def create_account(conn, account):
    result = await conn.fetchval('''
        INSERT INTO accounts(email, password, registration_date) VALUES($1, $2, $3) RETURNING id
    ''', account.email, account.password, datetime.utcnow())
    return result


async def get_account_by_email(conn, email):
    result = await conn.fetchrow(
        '''SELECT * FROM accounts WHERE email = $1''', email)
    if result is None:
        raise AccountNotFound
    return result


async def get_account_by_id(conn, id):
    result = await conn.fetchrow(
        '''SELECT * FROM accounts WHERE id = $1''', id)
    if result is None:
        raise AccountNotFound
    return result


async def delete_account(conn, id):
    result = await conn.execute(
        '''DELETE FROM accounts WHERE id = $1''', id)
    return result


async def update_account(conn, account):
    result = await conn.execute(
        '''UPDATE accounts SET email = $2, full_name = $3, phone = $4 WHERE id = $1''',
        account.id, account.email, account.full_name, account.phone)
    return result
