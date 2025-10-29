import json, os
from datetime import datetime, time, timedelta
from Logs.logs import Logger
from Validation.validators import Validator

BASE_PATH = os.getcwd()
BOOKINGS_FILE = os.path.join(BASE_PATH, "Database", "bookings.json")

# Ensure bookings file and folder exist
os.makedirs(os.path.dirname(BOOKINGS_FILE), exist_ok=True)
if not os.path.exists(BOOKINGS_FILE):
    with open(BOOKINGS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

class BookingOps:
    def book_table(self):
        table = input("Enter table number (T1-T10): ").strip().upper()
        if not Validator.is_valid_table(table):
            print(" Invalid table.")
            return

        name = input("Customer name: ").strip()
        mobile = input("Customer mobile (10 digits): ").strip()
        guests = input("Number of guests (1-20): ").strip()
        date_str = input("Enter booking date (YYYY-MM-DD): ").strip()
        time_str = input("Enter booking time (HH:MM in 24hr format): ").strip()

        if not Validator.is_valid_name(name) or not Validator.is_valid_mobile(mobile) or not Validator.is_valid_guests(guests):
            print(" Invalid customer details. ")
            return
        if not Validator.is_valid_date(date_str) or not Validator.is_valid_time(time_str):
            print(" Invalid date or time format. ")
            return

        booking_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        now = datetime.now()

        if booking_datetime.date() == now.date() and booking_datetime.time() <= now.time():
            print(" Booking time must be later than current time. ")
            return
        if booking_datetime.date() < now.date():
            print(" Booking date must be today or in the future. ")
            return
        if not (time(9, 0) <= booking_datetime.time() <= time(23, 0)):
            print(" Booking time must be between 09:00 and 23:00. ")
            return

        with open(BOOKINGS_FILE, "r", encoding="utf-8") as f:
            bookings = json.load(f)

        for b in bookings:
            if b["table"] == table and b["date"] == date_str and b["time"] == time_str:
                print(" Table already booked at that time. ")
                suggested = booking_datetime
                while True:
                    suggested += timedelta(minutes=30)
                    if suggested.time() > time(23, 0):
                        print(" No slots available today. ")
                        return
                    slot_taken = any(
                        bk["table"] == table and
                        bk["date"] == suggested.strftime("%Y-%m-%d") and
                        bk["time"] == suggested.strftime("%H:%M")
                        for bk in bookings
                    )
                    if not slot_taken:
                        print(f" Next available slot: {suggested.strftime('%Y-%m-%d %H:%M')} ")
                        return
                return

        booking = {
            "table": table,
            "name": name,
            "mobile": mobile,
            "guests": int(guests),
            "date": date_str,
            "time": time_str,
            "timestamp": now.strftime('%Y-%m-%d %H:%M:%S')
        }

        bookings.append(booking)
        with open(BOOKINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(bookings, f, indent=4)

        print(" Table booked successfully. ")
        Logger.write_log("Table booked", actor="staff", details=f"Table: {table}, Time: {time_str}, Date: {date_str}, Name: {name}")

    def cancel_booking(self):
        table = input("Enter table number to cancel (T1-T10): ").strip().upper()
        time_str = input("Enter booking time to cancel (HH:MM): ").strip()
        date_str = input("Enter booking date to cancel (YYYY-MM-DD): ").strip()

        if not Validator.is_valid_table(table):
            print(" Invalid table number. ")
            return
        if not Validator.is_valid_time(time_str):
            print(" Invalid time format. ")
            return
        if not Validator.is_valid_date(date_str):
            print(" Invalid date format. ")
            return

        with open(BOOKINGS_FILE, "r", encoding="utf-8") as f:
            bookings = json.load(f)

        match_found = False
        for b in bookings:
            if b.get("table") == table and b.get("time") == time_str and b.get("date") == date_str:
                bookings.remove(b)
                with open(BOOKINGS_FILE, "w", encoding="utf-8") as f:
                    json.dump(bookings, f, indent=4)
                print(" Booking cancelled. ")
                Logger.write_log("Booking cancelled", actor="staff", details=f"Table: {table}, Time: {time_str}, Date: {date_str}")
                match_found = True
                break

        if not match_found:
            print(" No matching booking found. ")
            Logger.write_log("Cancellation failed", actor="staff", details=f"Table: {table}, Time: {time_str}, Date: {date_str}")
