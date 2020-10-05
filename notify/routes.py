from notify.views import Index
from notify.settings import STATIC_DIR

from notify.views import Tasks


def setup_static(app):
    app.router.add_static('/static/', STATIC_DIR, name='static')
    app.router.add_get('/new_task', Tasks.get, name='new_task')
    app.router.add_post('/new_task', Tasks.create)


def setup_routes(app):
    app.router.add_get('/', Index.get, name='index')
    setup_static(app)
