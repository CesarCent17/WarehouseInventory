from dao.auth import Auth

class LoginController():
    def __init__(self):
        self.auth = Auth()

    def getUserAuth(self, email, passw):
        return self.auth.getUserAuth(email, passw)

