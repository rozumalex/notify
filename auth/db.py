from datetime import datetime

from auth.models import Account
from auth.exceptions import AccountNotFound

from db import db_connector


@db_connector
async def create_account(conn, account: Account) -> int:
    result = await conn.fetchval('''
        INSERT INTO accounts(email, password, registration_date) VALUES(
        $1, $2, $3) RETURNING id
    ''', account.email, account.password, datetime.utcnow())
    return result


@db_connector
async def get_account_by_email(conn, email: str):
    result = await conn.fetchrow(
        '''SELECT * FROM accounts WHERE email = $1''', email)
    if result is None:
        raise AccountNotFound
    return Account(result)


@db_connector
async def get_account_by_id(conn, account_id: int):
    result = await conn.fetchrow('''SELECT * FROM accounts WHERE id = $1''',
                                 int(account_id))
    if result is None:
        raise AccountNotFound
    return Account(result)


@db_connector
async def delete_account(conn, account_id: int):
    await conn.execute(
        '''DELETE FROM accounts WHERE id = $1''', account_id)


@db_connector
async def update_account(conn, account: Account):
    await conn.execute(
        '''UPDATE accounts SET email = $2, full_name = $3,
        phone = $4 WHERE id = $1''',
        account.id, account.email, account.full_name, account.phone)
