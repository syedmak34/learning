data = []
n = int(input("Enter how many numbers are in list: "))
for i in range(n):
    number = int(input(f"Enter number, {i+1}: "))
    data.append(number)

def insertion(arr):
  n = len(arr)
  for i in range(1, n):
    for j in range(i, 0, -1):
      if arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
      else:
        break

insertion(data)
print(data)