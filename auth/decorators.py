from auth.tools import redirect


def login_required(func):
    async def wrapped(request, *args, **kwargs):
        if not request.account:
            raise redirect(request, 'login')
        return await func(request, *args, **kwargs)
    return wrapped


def anonymous_required(func):
    async def wrapped(request, *args, **kwargs):
        if request.account:
            raise redirect(request, 'index')
        return await func(request, *args, **kwargs)
    return wrapped


def db_connector(func):
    """Декоратор перехватывает пул и отдает соединение"""
    async def wrapped(pool, request, *args, **kwargs):
        async with pool.acquire() as connection:
            async with connection.transaction():
                return await func(connection, request, *args, **kwargs)
    return wrapped
