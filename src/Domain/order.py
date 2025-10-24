import json, os
from Domain.menu import Menu

BASE_PATH = os.getcwd()
ORDERS_FILE = os.path.join(BASE_PATH, "Database", "orders.json")

class Order:
    def place_order(self):
        table = input("Enter table number: ")
        codes = input("Enter item codes (comma-separated): ").split(',')

        # Load menu items as MenuItem objects
        menu_items = Menu().load_menu()

        selected_items = []
        for code in codes:
            code = code.strip()
            item = next((i for i in menu_items if i.code == code), None)
            if item:
                selected_items.append(item.code)
            else:
                print(f" Item code '{code}' not found in menu.")

        if not selected_items:
            print(" No valid items selected.")
            return

        order = {
            "table": table.strip(),
            "items": selected_items
        }

        try:
            with open(ORDERS_FILE, "r") as f:
                orders = json.load(f)
        except:
            orders = []

        orders.append(order)
        with open(ORDERS_FILE, "w") as f:
            json.dump(orders, f, indent=4)
        print(" Order placed successfully.")

    def update_or_cancel_order(self):
        table = input("Enter table number to update/cancel: ")
        try:
            with open(ORDERS_FILE, "r") as f:
                orders = json.load(f)
        except:
            print(" No orders found.")
            return

        found = False
        for order in orders:
            if order["table"] == table:
                found = True
                print("1. Update Order")
                print("2. Cancel Order")
                choice = input("Enter choice: ")
                if choice == '1':
                    new_codes = input("Enter new item codes (comma-separated): ").split(',')
                    order["items"] = [code.strip() for code in new_codes]
                    print(" Order updated.")
                elif choice == '2':
                    orders.remove(order)
                    print(" Order cancelled.")
                else:
                    print(" Invalid choice.")
                break

        if not found:
            print(" Order not found.")

        with open(ORDERS_FILE, "w") as f:
            json.dump(orders, f, indent=4)
