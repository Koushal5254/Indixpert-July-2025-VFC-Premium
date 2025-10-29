import json, os
from getpass import getpass
from Model.user_model import UserModel
from Validation.validators import Validator
from Logs.logs import Logger

BASE_PATH = os.getcwd()
USERS_FILE = os.path.join(BASE_PATH, "Database", "users.json")

class Auth:
    def __init__(self):
        self.admin_email = "admin@vfcpremium.com"
        self.admin_password = "VFCadmin@123"
        self.admin_name = "VFC Premium Admin"

    def sign_up(self):
        role = input("Role (staff only): ").lower()
        if role != "staff":
            print(" Only staff can sign up.")
            Logger.write_log("Unauthorized sign-up attempt", actor="unknown", details=f"Role: {role}")
            return

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")
        exp = input("Enter Experience: ")
        password = getpass("Enter Password: ")

        if not (Validator.is_valid_name(name) and Validator.is_valid_email(email) and
                Validator.is_valid_mobile(mobile) and Validator.is_valid_password(password)):
            print(" Invalid input.")
            Logger.write_log("Sign-up failed", actor="staff", details=f"Email: {email}")
            return

        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except:
            users = []

        if any(u["email"] == email for u in users):
            print(" Email already registered. ")
            Logger.write_log("Duplicate sign-up attempt", actor="staff", details=f"Email: {email}")
            return

        user = UserModel(email, name, mobile, exp, "staff", password)
        users.append(user.to_dict())
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)
        print(" Welcome to VFC Premium! Staff sign-up successful. ")
        Logger.write_log("Staff signed up", actor="staff", details=f"Email: {email}")

    def sign_in(self):
        email = input("Email: ")
        password = getpass("Password: ")

        if email == self.admin_email and password == self.admin_password:
            print(f" Welcome {self.admin_name} (admin)")
            Logger.write_log("Admin signed in", actor="admin", details=f"Email: {email}")
            return "admin"

        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except:
            print(" No users found.")
            Logger.write_log("Sign-in failed", actor="staff", details="User file missing")
            return None

        for u in users:
            if u["email"] == email and u["password"] == password:
                print(f" Welcome {u['name']} ({u['role']}) to VFC Premium")
                Logger.write_log("Staff signed in", actor="staff", details=f"Email: {email}")
                return u["role"]

        print(" Invalid credentials. ")
        Logger.write_log("Sign-in failed", actor="staff", details=f"Email: {email}")
        return None
