import json, os
from Validation.validators import Validator
from Logs.logs import Logger

BASE_PATH = os.getcwd()
MENU_FILE = os.path.join(BASE_PATH, "Database", "menu.json")

# Ensure menu file exists
os.makedirs(os.path.dirname(MENU_FILE), exist_ok=True)
if not os.path.exists(MENU_FILE):
    with open(MENU_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

class Menu:
    def display_menu(self):
        try:
            with open(MENU_FILE, "r", encoding="utf-8") as f:
                menu = json.load(f)
        except:
            print(" Menu file missing or unreadable. ")
            return

        if not menu:
            print(" Menu is currently empty. ")
            return

        print("\n VFC Premium Menu ")
        print("-" * 40)
        for item in menu:
            print(f"{item['code']} | {item['name']} | ₹{item['price']} | {item['category']}")
        print("-" * 40)

    def admin_menu_ops(self):
        while True:
            print("\n Admin Menu Options ")
            print("1. Add New Item")
            print("2. Update Existing Item")
            print("3. Back")
            choice = input("Enter choice: ").strip()

            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.update_item()
            elif choice == '3':
                break
            else:
                print(" Invalid choice. ")

    def add_item(self):
        code = input("Enter item code (e.g., M01): ").strip().upper()
        name = input("Enter item name: ").strip()
        price = input("Enter price (₹): ").strip()
        category = input("Enter category (Starter/Main/Dessert/Drink): ").strip().capitalize()

        if not Validator.is_valid_code(code) or not Validator.is_valid_name(name) or not Validator.is_valid_price(price):
            print(" Invalid item details. ")
            return

        try:
            with open(MENU_FILE, "r", encoding="utf-8") as f:
                menu = json.load(f)
        except:
            menu = []

        if any(item["code"] == code for item in menu):
            print(" Item code already exists. ")
            return

        new_item = {
            "code": code,
            "name": name,
            "price": float(price),
            "category": category
        }

        menu.append(new_item)
        with open(MENU_FILE, "w", encoding="utf-8") as f:
            json.dump(menu, f, indent=4)

        print(" Item added to menu. ")
        Logger.write_log("Menu item added", actor="admin", details=f"{code} | {name} | ₹{price} | {category}")

    def update_item(self):
        code = input("Enter item code to update: ").strip().upper()

        try:
            with open(MENU_FILE, "r", encoding="utf-8") as f:
                menu = json.load(f)
        except:
            print(" Menu file missing. ")
            return

        item = next((i for i in menu if i["code"] == code), None)
        if not item:
            print(" Item not found. ")
            return

        print(f"Current: {item['name']} | ₹{item['price']} | {item['category']}")
        name = input("New name (leave blank to keep): ").strip()
        price = input("New price (leave blank to keep): ").strip()
        category = input("New category (leave blank to keep): ").strip().capitalize()

        if name:
            if not Validator.is_valid_name(name):
                print(" Invalid name. ")
                return
            item["name"] = name
        if price:
            if not Validator.is_valid_price(price):
                print(" Invalid price. ")
                return
            item["price"] = float(price)
        if category:
            item["category"] = category

        with open(MENU_FILE, "w", encoding="utf-8") as f:
            json.dump(menu, f, indent=4)

        print(" Item updated. ")
        Logger.write_log("Menu item updated", actor="admin", details=f"{code} | {item['name']} | ₹{item['price']} | {item['category']}")
