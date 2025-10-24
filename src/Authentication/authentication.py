import json, os
from getpass import getpass
from Model.user_model import UserModel
from Validation.validators import Validator

BASE_PATH = os.getcwd()
USERS_FILE = os.path.join(BASE_PATH, "Database", "users.json")

class Auth:
    def __init__(self):
        self.admin_email = "admin@VFCPremium.com"
        self.admin_password = "Admin@123"
        self.admin_name = "Admin"

    def sign_up(self):
        role = input("Role (staff only): ").lower()
        if role != "staff":
            print("Only staff can sign up. Admin is predefined.")
            return

        name = input("Name: ")
        email = input("Email: ")
        mobile = input("Mobile: ")
        exp = input("Experience: ")
        password = getpass("Password: ")

        if not (Validator.is_valid_name(name) and Validator.is_valid_email(email) and
                Validator.is_valid_mobile(mobile) and Validator.is_valid_password(password)):
            print("Invalid input.")
            return

        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except:
            users = []

        if any(u["email"] == email for u in users):
            print("Email already registered.")
            return

        user = UserModel(email, name, mobile, exp, "staff", password)
        users.append(user.to_dict())
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)
        print("Staff sign-up successful.")

    def sign_in(self):
        email = input("Email: ")
        password = getpass("Password: ")

        # Check admin credentials
        if email == self.admin_email and password == self.admin_password:
            print(f"----- Welcome To VFC Premium -----")
            return "admin"

        # Check staff credentials
        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except:
            print("No users found.")
            return None

        for u in users:
            if u["email"] == email and u["password"] == password:
                print(f"Welcome {u['name']} ({u['role']})")
                return u["role"]

        print("Invalid credentials.")
        return None
