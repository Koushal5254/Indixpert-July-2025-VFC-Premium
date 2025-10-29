from Domain.menu import Menu
from Domain.order import OrderOps
from Domain.booking import BookingOps
from Domain.bill_gen import BillGenerator
from Report.reports import ReportOps
from Logs.logs import Logger

class Dashboard:
    def __init__(self, role):
        self.role = role

    def show(self):
        while True:
            print("\n VFC Premium Dashboard ")
            print("1. View Menu")
            print("2. Book Table")
            print("3. Place Order")
            print("4. Generate Bill")

            if self.role == "admin":
                print("5. Update/Cancel Order")
                print("6. Add/Update Menu")
                print("7. View Reports")
                print("8. Cancel Booking")
                print("9. Exit")
            else:
                print("5. Cancel Booking")
                print("6. Exit")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                Menu().display_menu()
            elif choice == '2':
                BookingOps().book_table()
            elif choice == '3':
                OrderOps().place_order()
            elif choice == '4':
                BillGenerator().generate_bill()
            elif choice == '5' and self.role == "admin":
                OrderOps().update_or_cancel_order()
            elif choice == '6' and self.role == "admin":
                Menu().admin_menu_ops()
            elif choice == '7' and self.role == "admin":
                self.view_reports()
            elif choice == '8' and self.role == "admin":
                BookingOps().cancel_booking()
            elif choice == '5' and self.role == "staff":
                BookingOps().cancel_booking()
            elif choice == '6' and self.role == "staff":
                print(" Logging out of VFC Premium... ")
                Logger.write_log("User logged out", actor=self.role)
                break
            elif choice == '9' and self.role == "admin":
                print(" Logging out of VFC Premium... ")
                Logger.write_log("User logged out", actor=self.role)
                break
            else:
                print(" Invalid choice. ")

    def view_reports(self):
        print("\n VFC Premium Reports ")
        print("1. Daily Sales")
        print("2. Daily Orders")
        print("3. Daily Bookings")
        print("4. Monthly Sales")
        print("5. Monthly Orders")
        print("6. Monthly Bookings")
        print("7. Back")

        report = ReportOps()
        while True:
            choice = input("Enter report choice: ").strip()
            if choice == '1':
                report.daily_sales()
                Logger.write_log("Viewed daily sales", actor="admin")
            elif choice == '2':
                report.daily_orders()
                Logger.write_log("Viewed daily orders", actor="admin")
            elif choice == '3':
                report.daily_bookings()
                Logger.write_log("Viewed daily bookings", actor="admin")
            elif choice == '4':
                report.monthly_sales()
                Logger.write_log("Viewed monthly sales", actor="admin")
            elif choice == '5':
                report.monthly_orders()
                Logger.write_log("Viewed monthly orders", actor="admin")
            elif choice == '6':
                report.monthly_bookings()
                Logger.write_log("Viewed monthly bookings", actor="admin")
            elif choice == '7':
                break
            else:
                print(" Invalid choice. ")
