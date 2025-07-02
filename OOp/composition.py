class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine

    def drive(self):
        self.engine.start()
        print("Car is moving")

# Testing
my_car = Car()
my_car.drive()
