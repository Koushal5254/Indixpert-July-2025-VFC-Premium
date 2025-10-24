import json, os
from datetime import datetime
from Logs.logs import Logger

BASE_PATH = os.getcwd()
ORDERS_FILE = os.path.join(BASE_PATH, "Database", "orders.json")
MENU_FILE = os.path.join(BASE_PATH, "Database", "menu.json")
BILLS_FILE = os.path.join(BASE_PATH, "Database", "bills.json")

class BillGenerator:
    def generate_bill(self):
        table = input("Enter table number to bill: ")

        try:
            with open(ORDERS_FILE, "r") as f:
                orders = json.load(f)
            with open(MENU_FILE, "r") as f:
                menu_raw = json.load(f)
        except:
            print(" Required files missing.")
            Logger.write_log("Bill generation failed", actor="admin", details="Missing order/menu files")
            return

        order = next((o for o in orders if o["table"] == table), None)
        if not order:
            print(" No order found for this table.")
            Logger.write_log("Bill generation failed", actor="admin", details=f"Table: {table} not found")
            return

        total = 0
        print("\n ---------- VFC Premium Invoice ----------")
        print(f"🕒 Date: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
        print(f"🪑 Table No: {table}")
        print("--------------------------------------------")
        print("Item Name                Price (₹)")
        print("--------------------------------------------")

        for code in order["items"]:
            item = next((m for m in menu_raw if m["code"] == code), None)
            if item:
                print(f"{item['name']:<25} ₹{item['price']}")
                total += item["price"]
            else:
                print(f"{code:<25}  Not found")
                Logger.write_log("Missing menu item during billing", actor="admin", details=f"Code: {code}")

        gst = round(total * 0.05, 2)
        grand_total = total + gst

        print("--------------------------------------------")
        print(f"{'Subtotal':<25} ₹{total}")
        print(f"{'GST (5%)':<25} ₹{gst}")
        print(f"{'Total Amount':<25} ₹{grand_total}")
        print("--------------------------------------------")
        print(" Thank you for dining with us!")
        print("--------------------------------------------")

        bill = {
            "table": table,
            "items": order["items"],
            "subtotal": total,
            "gst": gst,
            "total": grand_total,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        try:
            with open(BILLS_FILE, "r") as f:
                bills = json.load(f)
        except:
            bills = []

        bills.append(bill)
        with open(BILLS_FILE, "w") as f:
            json.dump(bills, f, indent=4)
        print(" Bill generated successfully.")
        Logger.write_log("Bill generated", actor="admin", details=f"Table: {table}, Total: ₹{grand_total}")
