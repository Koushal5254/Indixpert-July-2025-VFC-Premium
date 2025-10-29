import json, os
from datetime import datetime, timedelta

BASE_PATH = os.getcwd()
BILLS_FILE = os.path.join(BASE_PATH, "Database", "bills.json")
ORDERS_FILE = os.path.join(BASE_PATH, "Database", "orders.json")
BOOKINGS_FILE = os.path.join(BASE_PATH, "Database", "bookings.json")

class ReportOps:
    def __init__(self):
        self.today = datetime.now().date()
        self.month_ago = self.today - timedelta(days=30)

    def daily_sales(self):
        total = 0
        try:
            with open(BILLS_FILE, "r", encoding="utf-8") as f:
                bills = json.load(f)
            for bill in bills:
                bill_date = datetime.strptime(bill["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                if bill_date == self.today:
                    print(f"{bill['bill_id']} | {bill.get('customer_name','Unknown')} | ₹{bill['total']}")
                    total += bill["total"]
            print(f"\nToday's Total Sales: ₹{total}")
        except:
            print(" No billing data found. ")

    def daily_orders(self):
        count = 0
        try:
            with open(ORDERS_FILE, "r", encoding="utf-8") as f:
                orders = json.load(f)
            for order in orders:
                order_date = datetime.strptime(order["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                if order_date == self.today:
                    count += 1
            print(f"Today's Orders: {count}")
        except:
            print(" No order data found. ")

    def daily_bookings(self):
        count = 0
        try:
            with open(BOOKINGS_FILE, "r", encoding="utf-8") as f:
                bookings = json.load(f)
            for booking in bookings:
                booking_date = datetime.strptime(booking["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                if booking_date == self.today:
                    count += 1
            print(f"Today's Bookings: {count}")
        except:
            print(" No booking data found. ")

    def monthly_sales(self):
        total = 0
        try:
            with open(BILLS_FILE, "r", encoding="utf-8") as f:
                bills = json.load(f)
            for bill in bills:
                bill_date = datetime.strptime(bill["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                if self.month_ago <= bill_date <= self.today:
                    total += bill["total"]
            print(f"Last 30 Days Sales: ₹{total}")
        except:
            print(" No billing data found. ")

    def monthly_orders(self):
        count = 0
        try:
            with open(ORDERS_FILE, "r", encoding="utf-8") as f:
                orders = json.load(f)
            for order in orders:
                order_date = datetime.strptime(order["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                if self.month_ago <= order_date <= self.today:
                    count += 1
            print(f"Last 30 Days Orders: {count}")
        except:
            print(" No order data found. ")

    def monthly_bookings(self):
        count = 0
        try:
            with open(BOOKINGS_FILE, "r", encoding="utf-8") as f:
                bookings = json.load(f)
            for booking in bookings:
                booking_date = datetime.strptime(booking["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                if self.month_ago <= booking_date <= self.today:
                    count += 1
            print(f"Last 30 Days Bookings: {count}")
        except:
            print(" No booking data found. ")
