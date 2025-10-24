from Authentication.authentication import Auth
from Report.Dashboards.dashboard import Dashboard
from Domain.menu import Menu

class AppController:
    def __init__(self):
        self.auth = Auth()
        self.menu = Menu()

    def run(self):
        while True:
            print("\n------ Welcome To VFC Premium ------")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. View Menu")
            print("4. Exit")
            choice = input("Enter your choice : ")

            if choice == '1':
                self.auth.sign_up()
            elif choice == '2':
                role = self.auth.sign_in()
                if role in ["admin", "staff"]:
                    Dashboard(role).run()
                else:
                    print("Access denied.")
            elif choice == '3':
                self.menu.show_menu()
            elif choice == '4':
                print("Exiting.. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")
