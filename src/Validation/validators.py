import re
from datetime import datetime

class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email and len(email) >= 7

    @staticmethod
    def is_valid_mobile(mobile):
        return mobile.isdigit() and len(mobile) == 10

    @staticmethod
    def is_valid_name(name):
        return name.replace(" ", "").isalpha() and len(name) >= 2

    @staticmethod
    def is_valid_experience(exp):
        return exp.isdigit() and int(exp) >= 0

    @staticmethod
    def is_valid_password(password):
        if len(password) < 6:
            return False
        if not re.search(r'[A-Z]', password):  
            return False
        if not re.search(r'[!@#$%^&*d]', password):  
            return False
        return True

    @staticmethod
    def is_valid_code(code):
        return code.isalnum() and len(code) >= 3

    @staticmethod
    def is_valid_quantity(qty):
        return qty.isdigit() and int(qty) > 0

    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except:
            return False

    @staticmethod
    def is_valid_time(time_str):
        try:
            datetime.strptime(time_str, "%H:%M")
            return True
        except:
            return False

    @staticmethod
    def is_valid_guests(guests):
        return guests.isdigit() and 1 <= int(guests) <= 20

    @staticmethod
    def is_valid_table(table_no):
        return table_no.upper().startswith("T") and table_no[1:].isdigit()
