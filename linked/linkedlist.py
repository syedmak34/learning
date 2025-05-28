class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


a=int(input("enter first num: "))
b=int(input("enter second num: "))
c=int(input("enter third  num: "))
d=int(input("enter fourth num: "))

Node1 = Node(a)
Node2 = Node(b)
Node3 = Node(c)
Node4 = Node(d)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

current = Node1
while current is not None:
    print(current.data, end ="->")
    current = current.next
print("None")