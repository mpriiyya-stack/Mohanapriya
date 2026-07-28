class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} is driving.")
car = Car("BMW")
car.drive()