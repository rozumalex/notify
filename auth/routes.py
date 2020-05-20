from auth.views import Signup, Login, Logout, Profile

def setup_routes(app):
    app.router.add_get('/signup', Signup.get, name='signup')
    app.router.add_post('/signup', Signup.post)
    app.router.add_get('/login', Login.get, name='login')
    app.router.add_post('/login', Login.post)
    app.router.add_get('/logout', Logout.get)
    app.router.add_get('/profile', Profile.get, name='profile')
    app.router.add_post('/profile', Profile.update)
    app.router.add_get('/profile/{id}', Profile.view)
    app.router.add_get('/delete_account', Profile.get_delete)
    app.router.add_post('/delete_account', Profile.delete)