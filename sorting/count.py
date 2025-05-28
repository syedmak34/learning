data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

def count(data):
    n = len(data)
    maxx = int(max(data))  
    counts = [0] * (maxx + 1)

    for x in data:
        counts[int(x)] += 1  

    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            data[i] = c
            i += 1
            counts[c] -= 1

count(data)
print("Sorted data using count sort:", data)
