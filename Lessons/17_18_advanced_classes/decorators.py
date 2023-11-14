class User:
    def __init__(self, email, first_name, last_name=None, age=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    @staticmethod
    def class_name():
        return "User"

    @classmethod
    def from_dict(cls, data):
        return cls(data["email"], data["first_name"], data["last_name"], data["age"])
    
    @property
    def full_name(self):
        return self.get_full_name()
    
    def get_full_name(self):
        last_name = self.last_name if self.last_name is not None else ""
        return f"{self.first_name} {last_name}"

    def get_next_year_age(self):
        if self.age is None:
            return "Unknown"

        return self.age + 1


print("Class name:", User.class_name())

# user = User("user@example.com", "John", last_name="Snow")

# or with class method
user = User.from_dict({
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Snow",
    "age": 36
})

print(user.get_full_name())
print(user.full_name)

