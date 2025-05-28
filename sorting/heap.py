data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

def heap_sort(data):
    data = data.copy()

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1  
        r = 2 * i + 2  

        if l < n and arr[l] > arr[largest]:
            largest = l

        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(data)

    
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    print("Sorted data using Heap Sort:", data)

heap_sort(data)