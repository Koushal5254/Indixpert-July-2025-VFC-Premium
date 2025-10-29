class MenuItem:
    def __init__(self, code, name, category, price):
        self.code = code
        self.name = name
        self.category = category
        self.price = price

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "category": self.category,
            "price": self.price
        }
