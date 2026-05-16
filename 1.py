class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Bobik", 3)
cat = Cat("Murka", 2)

dog.make_sound()
cat.make_sound()