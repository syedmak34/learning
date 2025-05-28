age = int(input("Enter your age: "))

while age != 0:
    if age < 13:
        print('You are a child')
    elif age < 18:
        print('You are a teenager')
    else:
        print('You are an adult')
    
    age = int(input("Enter your age (0 to quit): "))
