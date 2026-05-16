class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Moving at {self.speed} km/h")


class Car(Vehicle):
    pass


class Plane(Vehicle):
    pass


class Bicycle(Vehicle):
    pass


car = Car(120)
plane = Plane(900)
bicycle = Bicycle(25)

car.move()
plane.move()
bicycle.move()