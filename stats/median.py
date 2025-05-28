while True:
 data = []
 n = int(input("Enter number of elements: "))
 for i in range(n):
    element = float(input(f"Enter element, {i+1}: "))
    data.append(element)
 def median(data):

   data.sort()
   N=len(data)

   if N%2==1:
    return data[N//2]


   else:
    a=data[N//2-1]
    b=data[N//2]
    return (a+b)/2
  

 print("Median: ",median(data))
 repeat = input("enter no if you want to terminate else enter yes: ")
 if repeat == "no":
  break