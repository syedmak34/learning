data = []
n = int(input("Enter the amount of numbers in list: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

def comb_sort(data):
    n = len(data)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True  

      
        i = 0
        while i + gap < n:
            if data[i] > data[i + gap]:
                
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted = False  
            i += 1
    return data


sorted_data = comb_sort(data)
print("Sorted data using comb sort: ", sorted_data)