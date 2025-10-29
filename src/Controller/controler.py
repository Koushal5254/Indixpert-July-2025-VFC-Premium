from Authentication.authentication import Auth
from Report.Dashboards.dashboard import Dashboard
from Domain.menu import Menu

class AppController:
    def run(self):
        while True:
            print("\n Welcome to VFC Premium ")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. View Menu")
            print("4. Exit")

            choice = input("Enter your choice: ")
            auth = Auth()

            if choice == '1':
                auth.sign_up()
            elif choice == '2':
                role = auth.sign_in()
                if role:
                    Dashboard(role).show()
            elif choice == '3':
                Menu().display_menu()
            elif choice == '4':
                print(" Thank you for visiting at VFC Premium! ")
                break
            else:
                print(" Invalid choice. ")
