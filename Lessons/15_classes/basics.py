# simplest class definition
class Shape:
    pass


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi!")

    def greet(self, group = "World"):
        print(f"Hello, {group}!")

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def debug(self, *args, **kwargs):
        print(f"{self=} {args=} {kwargs=}")


def outside_method(self):
    print("I'm a method defined outside of the class")
Person.outside_method = outside_method


# Python uses object-reference when passing values
def change_name(person):
    person.name = "I was changed!"


sergey = Person("Sergey")
john = Person("John")

sergey.set_name("Sergey")
change_name(sergey)

print(sergey.get_name())
print(f"My name is {sergey.name}")
sergey.greet()

sergey.say_hi()
john.greet("Python World")

print(john.get_name())
john.outside_method()

sergey.debug(1, 2, 3, age=18, dob="01.01.2023")
