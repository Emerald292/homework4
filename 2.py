class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(f"Age: {self.age}")


class Driver(Person):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"License Number: {self.license_number}")


driver = Driver("Alex", 25, "AB123456")

driver.show_info()