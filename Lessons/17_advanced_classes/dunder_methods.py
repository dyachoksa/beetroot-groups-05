class Person:
    def __init__(self, name, age=None) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        # __str__ is used for str() function

        return self.get_name()
        # or
        # return self.name

    def __int__(self) -> int:
        # __int__ is used for int() function
        return self.age

    def __repr__(self) -> str:
        # __repr__ is used for repr() function
        return "<Person name={} age={}>".format(self.name, self.age)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Person | int):
            return False
        
        if isinstance(other, int):
            return self.age == other
        
        return self.name == other.name and self.age == other.age
    
    def __len__(self) -> int:
        return self.get_age()
    
    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("Only integers are allowed")
        
        self.age += other
        return self

    def get_name(self) -> str:
        return self.name
    
    def get_age(self) -> str:
        return self.age
    
    def set_name(self, name: str):
        self.name = name

    def set_age(self, age: int):
        self.age = age


person = Person("Sergey", 18)

print(f"I'm {person}")
print(f"I'm {person.get_age()} years old")
