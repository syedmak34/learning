def add(numbers):
    return sum(numbers)

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def calculate(method, numbers):
    return method(numbers)
print("Add:", calculate(add, [1, 2, 3]))        # 6
print("Multiply:", calculate(multiply, [1, 2, 3]))  # 6
