from notify.views import Index
from notify.settings import STATIC_DIR

def setup_static(app):
    app.router.add_static('/static/', STATIC_DIR, name='static')

def setup_routes(app):
    app.router.add_get('/', Index.get, name='index')
    setup_static(app)