import numpy as np
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
def matriximput(name):
    print(f"Enter the elements of matrix {name} row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} integers.")
            row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)
a = matrixinput("A")
b = matrixinput("B")
c = a + b
d = a*b
e = a-b
print("Resultant of addition:")
print(c)
print("    ")
print("result of subtraction")
print(e)
print("result of multipliction")
print(d)
