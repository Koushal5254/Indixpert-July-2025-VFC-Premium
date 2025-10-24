from Domain.menu import Menu
from Domain.order import Order
from Domain.bill_gen import Bill
from Domain.booking import Booking

class Dashboard:
    def __init__(self, role):
        self.role = role.lower()
        self.menu = Menu()
        self.order = Order()
        self.bill = Bill()
        self.booking = Booking()

    def run(self):
        while True:
            print(f"\n----- {self.role.capitalize()} Dashboard -----")
            print("1. View Menu")
            print("2. Book Table")
            print("3. Place Order")
            print("4. Generate Bill")

            if self.role == "admin":
                print("5. Update/Cancel Order")
                print("6. Add Menu Item")
                print("7. Update Menu Item")
                print("8. View Reports")
                print("9. Logout")
            else:
                print("5. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.menu.show_menu()
            elif choice == '2':
                self.booking.book_table()
            elif choice == '3':
                self.order.place_order()
            elif choice == '4':
                self.bill.generate_bill()
            elif choice == '5' and self.role == "admin":
                self.order.update_or_cancel_order()
            elif choice == '6' and self.role == "admin":
                self.menu.add_item(self.role)
            elif choice == '7' and self.role == "admin":
                self.menu.update_item(self.role)
            elif choice == '8' and self.role == "admin":
                print(" Reports will be coming soon...")
            elif (choice == '9' and self.role == "admin") or (choice == '5' and self.role == "staff"):
                print(" Logging out...")
                break
            else:
                print(" Invalid choice. Please try again.")
