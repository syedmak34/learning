class Add:
    def do(self, numbers):
        return sum(numbers)

class Multiply:
    def do(self, numbers):
        result = 1
        for n in numbers:
            result *= n
        return result

class Calculator:
    def __init__(self, method):
        self.method = method

    def calculate(self, numbers):
        return self.method.do(numbers)
calc = Calculator(Add())
print("Add:", calc.calculate([1, 2, 3]))  # 6

calc.method = Multiply()
print("Multiply:", calc.calculate([1, 2, 3]))  # 6
