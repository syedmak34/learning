data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

def radix(data):
    data = data.copy()
    
    if any(float(x) != int(x) for x in data):
        return

    def countingexp(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for num in arr:
            index = (int(num) // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (int(arr[i]) // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    max_val = int(max(data))
    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(data, exp)
        exp *= 10
    print("sort:", data)

radix(data)
print(data)