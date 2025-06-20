from viewmodels.user_viewmodel import UserViewModel
from views.user_view import UserView

def main():
    viewmodel = UserViewModel()
    view = UserView()

    viewmodel.add_user("Charlie")
    viewmodel.add_user("Diana")

    users = viewmodel.get_users()
    view.show_users(users)

if __name__ == "__main__":
    main()