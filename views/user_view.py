class UserView:
    def show_users(self, users):
        print("Lista de usuarios:")
        for user in users:
            print(f"- {user}")