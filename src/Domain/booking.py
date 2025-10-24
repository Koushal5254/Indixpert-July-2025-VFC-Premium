import json, uuid, os
from Validation.validators import Validator

BASE_PATH = os.getcwd()
BOOKINGS_FILE = os.path.join(BASE_PATH, "Database", "bookings.json")

class Booking:
    def book_table(self):
        name = input("Customer name: ")
        email = input("Email: ")
        mobile = input("Mobile: ")
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM): ")
        guests = input("Guests: ")
        table = input("Table No (e.g., T1): ")

        if not (Validator.is_valid_name(name) and Validator.is_valid_email(email) and
                Validator.is_valid_mobile(mobile) and Validator.is_valid_date(date) and
                Validator.is_valid_time(time) and Validator.is_valid_guests(guests) and
                Validator.is_valid_table(table)):
            print("Invalid booking details.")
            return

        booking = {
            "booking_id": f"BK{uuid.uuid4().hex[:6].upper()}",
            "name": name,
            "email": email,
            "mobile": mobile,
            "date": date,
            "time": time,
            "guests": int(guests),
            "table_no": table.upper(),
            "status": "Confirmed"
        }

        try:
            with open(BOOKINGS_FILE, "r") as f:
                bookings = json.load(f)
        except:
            bookings = []

        bookings.append(booking)
        with open(BOOKINGS_FILE, "w") as f:
            json.dump(bookings, f, indent=4)
        print("Table booked successfully.")

    def view_bookings(self):
        try:
            with open(BOOKINGS_FILE, "r") as f:
                bookings = json.load(f)
        except:
            print("No bookings found..")
            return

        print("\n----- Bookings -----")
        for b in bookings:
            print(f"{b['booking_id']} | {b['name']} | {b['date']} {b['time']} | Table: {b['table_no']} | Guests: {b['guests']} | Status: {b['status']}")
