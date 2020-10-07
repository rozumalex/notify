from auth.routes import setup_routes as auth_routes
from notify.routes import setup_routes as notify_routes


routes = (
    auth_routes,
    notify_routes,
)
