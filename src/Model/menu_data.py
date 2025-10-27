class MenuItem:
    def __init__(self, code, name, category, pricee):
        self.code = code
        self.name = name
        self.category = category
        self.price = pricee

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "category": self.category,
            "price": self.price
        }
    
    #To get the data
    @staticmethod
    def from_dict(data):
        return MenuItem(
            code=data.get("code"),
            name=data.get("name"),
            category=data.get("category"),
            price=data.get("price")
        )
