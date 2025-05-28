data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

def merge(data):
    n = len(data)
    if n <= 1:
        return data

    m = n // 2
    L = data[:m]
    R = data[m:]

    L = merge(L)
    R = merge(R)

    sorted_data = []
    l = r = 0
    L_len = len(L)
    R_len = len(R)

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_data.append(L[l])
            l += 1
        else:
            sorted_data.append(R[r])
            r += 1

    while l < L_len:
        sorted_data.append(L[l])
        l += 1

    while r < R_len:
        sorted_data.append(R[r])
        r += 1

    return sorted_data

sorted = merge(data)
print("Sorted data:", sorted)