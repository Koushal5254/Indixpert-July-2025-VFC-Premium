class UserModel:
    def __init__(self, email, name, mobile, experience, role, password):
        self.email = email
        self.name = name
        self.mobile = mobile
        self.experience = experience
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
