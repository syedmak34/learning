data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

def cocktail_sort(data):
    data = data.copy()

    n = len(data)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True

        start += 1

    print("Sorted data using Cocktail Sort:", data)

cocktail_sort(data)
