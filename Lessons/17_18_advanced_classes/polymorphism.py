class Student:
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str):
        self.name = name

    def get_fav_lesson(self) -> str:
        return "Math"


class Teacher:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str):
        self.name = name

    def get_salary_level(self) -> int:
        return 10000


class Apple:
    def get_name(self) -> str:
        return "Apple"
    

class Orange:
    def get_color(self) -> str:
        return "orange"


def make_person(cls, name: str):
    return cls(name)


def print_person_name(person):
    # in real projects there should be the validation
    # like this:
    # if not isinstance(person, Student | Teacher):
    #     raise ValueError("Only Student or Teacher instances are allowed")
    
    print(f"I'm {person.get_name()}")


student = make_person(Student, "John")
teacher = make_person(Teacher, "Sergey")

apple = Apple()
orange = Orange()

print_person_name(student)
print_person_name(teacher)
print_person_name(apple)
print_person_name(orange)
