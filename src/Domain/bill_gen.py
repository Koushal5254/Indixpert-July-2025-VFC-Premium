import json, os
from datetime import datetime
from Logs.logs import Logger
from Validation.validators import Validator

BASE_PATH = os.getcwd()
ORDERS_FILE = os.path.join(BASE_PATH, "Database", "orders.json")
BOOKINGS_FILE = os.path.join(BASE_PATH, "Database", "bookings.json")
MENU_FILE = os.path.join(BASE_PATH, "Database", "menu.json")
BILLS_FILE = os.path.join(BASE_PATH, "Database", "bills.json")

class BillGenerator:
    def generate_bill(self):
        table = input("Enter table number (T1-T10): ").strip().upper()
        if not Validator.is_valid_table(table):
            print(" Invalid table number.")
            return

        try:
            with open(ORDERS_FILE, "r", encoding="utf-8") as f:
                orders = json.load(f)
        except:
            print(" No orders found.")
            return

        order = next((o for o in orders if o.get("table") == table and o.get("items")), None)
        if not order:
            print(" No order found for this table.")
            return

        item_codes = order.get("items", [])
        if not item_codes:
            print(" No items found in order.")
            return

        try:
            with open(MENU_FILE, "r", encoding="utf-8") as f:
                menu = json.load(f)
        except:
            print(" Menu not available.")
            return

        item_count = {}
        for code in item_codes:
            item_count[code] = item_count.get(code, 0) + 1

        subtotal = 0
        item_details = []
        for code, qty in item_count.items():
            item = next((m for m in menu if m["code"] == code), None)
            if item:
                price = item["price"]
                subtotal += price * qty
                item_details.append({
                    "code": code,
                    "name": item["name"],
                    "quantity": qty,
                    "unit_price": price,
                    "total_price": price * qty
                })

        gst = round(subtotal * 0.05, 2)
        total = round(subtotal + gst, 2)

        customer_name = "Unknown"
        customer_mobile = "Unknown"
        guests = 0
        try:
            with open(BOOKINGS_FILE, "r", encoding="utf-8") as f:
                bookings = json.load(f)
            for b in bookings:
                if b.get("table") == table:
                    customer_name = b.get("name", "Unknown")
                    customer_mobile = b.get("mobile", "Unknown")
                    guests = b.get("guests", 0)
                    break
        except:
            pass

        try:
            with open(BILLS_FILE, "r", encoding="utf-8") as f:
                bills = json.load(f)
        except:
            bills = []

        bill_id = f"BILL{len(bills)+1:03d}"

        bill = {
            "bill_id": bill_id,
            "table": table,
            "customer_name": customer_name,
            "customer_mobile": customer_mobile,
            "guests": guests,
            "items": item_details,
            "subtotal": subtotal,
            "gst": gst,
            "total": total,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        bills.append(bill)
        with open(BILLS_FILE, "w", encoding="utf-8") as f:
            json.dump(bills, f, indent=4)

        print(f"\n Bill generated: {bill_id}")
        print(f" Customer: {customer_name} ({customer_mobile})")
        print(f" Guests: {guests}")
        print("\n Items Ordered:")
        for item in item_details:
            print(f"- {item['name']} x {item['quantity']} @ ₹{item['unit_price']} = ₹{item['total_price']}")

        print(f"\n Subtotal: ₹{subtotal}")
        print(f" GST (5%): ₹{gst}")
        print(f" Total: ₹{total}")

        Logger.write_log("Bill generated", actor="staff", details=f"{bill_id} | Table: {table} | Total: ₹{total}")
