import json, os
from Domain.menu import Menu
from Logs.logs import Logger

BASE_PATH = os.getcwd()
ORDERS_FILE = os.path.join(BASE_PATH, "Database", "orders.json")

class OrderOps:
    def place_order(self):
        table = input("Enter table number : ")
        codes = input("Enter item codes (comma-separated): ").split(',')

        menu_items = Menu().load_menu()
        selected_items = []

        for code in codes:
            code = code.strip()
            item = next((i for i in menu_items if i.code == code), None)
            if item:
                selected_items.append(item.code)
            else:
                print(f" Item code '{code}' not found.")
                Logger.write_log("Invalid item code during order", actor="staff", details=f"Code: {code}")

        if not selected_items:
            print(" No valid items selected.")
            Logger.write_log("Order failed", actor="staff", details=f"Table: {table}")
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
        Logger.write_log("Order placed", actor="staff", details=f"Table: {table}, Items: {', '.join(selected_items)}")

    def update_or_cancel_order(self):
        table = input("Enter table number to update/cancel: ")
        try:
            with open(ORDERS_FILE, "r") as f:
                orders = json.load(f)
        except:
            print(" No orders found.")
            Logger.write_log("Order update failed", actor="admin", details="Order file missing")
            return

        for order in orders:
            if order["table"] == table:
                print("1. Update Order")
                print("2. Cancel Order")
                choice = input("Enter choice: ")
                if choice == '1':
                    new_codes = input("Enter new item codes (comma-separated): ").split(',')
                    order["items"] = [code.strip() for code in new_codes]
                    print(" Order updated.")
                    Logger.write_log("Order updated", actor="admin", details=f"Table: {table}, New Items: {', '.join(order['items'])}")
                elif choice == '2':
                    orders.remove(order)
                    print(" Order cancelled.")
                    Logger.write_log("Order cancelled", actor="admin", details=f"Table: {table}")
                else:
                    print(" Invalid choice.")
                break
        else:
            print(" Order not found.")
            Logger.write_log("Order not found", actor="admin", details=f"Table: {table}")

        with open(ORDERS_FILE, "w") as f:
            json.dump(orders, f, indent=4)
