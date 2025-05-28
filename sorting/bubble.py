while True:
 data = []
 n = int(input("Enter number of elements: "))
 for i in range(n):
    element = int(input(f"Enter element, {i+1}: "))
    data.append(element)
 def buublesort(data):
  n=len(data)
  flag= True
  while flag:
   flag=False
   for i in range (1,n):
    if data [i-1]>data[i]:
     flag=True
     data [i-1],data[i] = data[i],data [i-1]
 buublesort(data)
 print (data)
 repeat = input("enter no if you want to terminate else enter anything: ")
 if repeat == "no":
  break