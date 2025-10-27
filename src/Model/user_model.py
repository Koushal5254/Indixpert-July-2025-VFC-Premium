class UserModel:
    def __init__(self, email, name, mobile, experiencee, role, password):
        self.email = email
        self.name = name
        self.mobile = mobile
        self.experience = experiencee
        self.role = role
        self.password = password

    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "mobile": self.mobile,
            "experience": self.experience,
            "role": self.role,
            "password": self.password
        }

    #To get the data
    @staticmethod
    def from_dict(data):
        return UserModel(
            email=data.get("email"),
            name=data.get("name"),
            mobile=data.get("mobile"),
            experience=data.get("experience"),
            role=data.get("role"),
            password=data.get("password")
        )
