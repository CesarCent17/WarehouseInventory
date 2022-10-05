from dao.repository import Repository

class RegisterFormController:
    def __init__(self):
        self.repository = Repository()

    def insert_user(self, user):
        return self.repository.insert_user(user)