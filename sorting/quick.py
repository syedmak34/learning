data = []
n = int(input("Enter the amount of numbers in yout list: "))
for i in range(n):
    element = int(input(f"Enter number {i+1}: "))
    data.append(element)

def quick(data):
  if len(data) <= 1:
    return data

  p = data[-1]

  L = [x for x in data[:-1] if x <= p]
  R = [x for x in data[:-1] if x > p]

  L = quick(L)
  R = quick(R)

  return L + [p] + R

sorted_data = quick(data)
print("Sorted_data: ", sorted_data)