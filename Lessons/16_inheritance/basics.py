class Animal:
    def __init__(self, name) -> None:
        if len(name) > 100:
            raise ValueError("Name can't be bigger than 100 chars")

        self.name = name

    def print_class(self):
        print(self.__class__)

        if isinstance(self, Cat):
            print("I'm the Cat instance")
        elif isinstance(self, Dog):
            print("I'm the Dog instance")
    
    def print_name(self):
        print(self.name)

    def greet_owner(self):
        raise RuntimeError("I don't know how to greet owner!")


class Cat(Animal):
    def greet_owner(self):
        print("Mew")


class Dog(Animal):
    def greet_owner(self):
        print("Bark")


class Duck(Animal):
    def __init__(self, name, can_fly = False) -> None:
        self.can_fly = can_fly
        
        super().__init__(name)
    
    def print_class(self):
        super().print_class()

        print("I'm the Duck instance")

    def greet_owner(self):
        print("Quak")
        print("I can fly!" if self.can_fly else "I can't fly :(")


cat = Cat("Cat 1")
dog = Dog("Dog 1")

print("Cat:")
cat.print_name()
cat.greet_owner()
cat.print_class()

print()

print("Dog:")
dog.print_name()
dog.greet_owner()

print()

print("Duck:")
duck = Duck("Duck 007")
duck.print_name()
duck.greet_owner()
