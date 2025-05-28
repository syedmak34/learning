import numpy as np

def gaussjordan(matrix):
    n = len(matrix)
    a = np.array(matrix, dtype=int)

    for i in range(n):
        a[i] = a[i] / a[i][i]

        for j in range(n):
            if j != i:
                a[j] = a[j] - a[j][i] * a[i]

    return a 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print(f"Enter the elements of matrix A row by row. Exactly {cols} integers per row also write answer in the end:")
a = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    while len(row) != cols+1:
        print(f"Please enter exactly {cols+1} integers.")
        row = list(map(int, input(f"Row {i+1}: ").split()))
    a.append(row)
a = np.array(a)
c=gaussjordan(a)
print("Solution:")
print (c)