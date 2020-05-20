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
             raise redirect(request, 'profile')
        return await func(request, *args, **kwargs)
    return wrapped
