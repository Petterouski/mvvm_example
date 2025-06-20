from models.user_model import UserModel

class UserViewModel:
    def __init__(self):
        self.model = UserModel()

    def add_user(self, name):
        self.model.add_user(name)

    def get_users(self):
        return self.model.get_users()