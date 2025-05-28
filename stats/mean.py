while True:
 data = []
 n = int(input("Enter number of elements: "))
 for i in range(n):
    element = float(input(f"Enter element, {i+1}: "))
    data.append(element)
 def mean(data):
    total=0
    for num in data:
     total=total+num
    return total/len(data)
 print(mean(data))
 repeat = input("enter no if you want to terminate else enter yes: ")
 if repeat == "no":
  break 