from notify.views import Index
from settings import STATIC_DIR

from notify.views import Tasks


def setup_static(app):
    app.router.add_static('/static/', STATIC_DIR, name='static')


def setup_routes(app):
    app.router.add_get('/', Index.get, name='index')
    app.router.add_get('/tasks/', Tasks.get_all, name="tasks")
    app.router.add_get('/tasks/new', Tasks.get_new, name='new_task')
    app.router.add_post('/tasks/new', Tasks.new)
    app.router.add_get('/tasks/{id}', Tasks.view)
    app.router.add_post('/tasks/{id}', Tasks.update)
    app.router.add_get('/tasks/{id}/delete', Tasks.delete)
    setup_static(app)
