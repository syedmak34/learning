while True:
 data = []
 n = int(input("Enter number of elements: "))
 for i in range(n):
    element = float(input(f"Enter element, {i+1}: "))
    data.append(element)
 def mode (data):
  maxcount=(0,0)
  for num in data:
    occurences=data.count(num)
    if occurences > maxcount[0]:
        maxcount= (occurences, num)
  return maxcount[1]
 print(mode(data))
 repeat = input("enter no if you want to terminate else enter yes: ")
 if repeat == "no":
  break