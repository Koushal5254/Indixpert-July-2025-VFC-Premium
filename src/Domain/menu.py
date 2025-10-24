import json, os
from Model.menu_data import MenuItem

BASE_PATH = os.getcwd()
MENU_FILE = os.path.join(BASE_PATH, "Database", "menu.json")

class Menu:
    def load_menu(self):
        try:
            with open(MENU_FILE, "r") as f:
                raw_items = json.load(f)
                return [MenuItem.from_dict(item) for item in raw_items]
        except:
            print(" Menu file missing or corrupted.")
            return []

    def show_menu(self):
        items = self.load_menu()
        print("\n ----- VFC PREMIUM MENU -----")
        categories = sorted(set(item.category for item in items))
        for cat in categories:
            print(f"\n- {cat}")
            for item in items:
                if item.category == cat:
                    print(f"  {item.code} - {item.name} : ₹{item.price}")

    def add_item(self, role):
        if role != "admin":
            print(" Access denied. Only admin can add items.")
            return

        code = input("Enter item code: ")
        name = input("Enter item name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))

        new_item = MenuItem(code, name, category, price).to_dict()

        try:
            with open(MENU_FILE, "r") as f:
                items = json.load(f)
        except:
            items = []

        items.append(new_item)
        with open(MENU_FILE, "w") as f:
            json.dump(items, f, indent=4)
        print(" Item added successfully.")

    def update_item(self, role):
        if role != "admin":
            print(" Access denied. Only admin can update items.")
            return

        code = input("Enter item code to update: ")
        try:
            with open(MENU_FILE, "r") as f:
                items = json.load(f)
        except:
            print(" Menu file missing..")
            return

        for item in items:
            if item["code"] == code:
                print(f"Current name: {item['name']}, price: ₹{item['price']}")
                item["name"] = input("New name: ") or item["name"]
                item["category"] = input("New category: ") or item["category"]
                new_price = input("New price: ")
                item["price"] = float(new_price) if new_price else item["price"]
                break
        else:
            print(" Item not found.")
            return

        with open(MENU_FILE, "w") as f:
            json.dump(items, f, indent=4)
        print(" Item updated successfully.")
