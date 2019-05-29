class Node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        temp=Node(data)
        temp.nextt=self.head
        self.head=temp
    def dequeue(self):
        previous=temp=self.head
        while(temp.nextt!=None):
            previous=temp
            temp=temp.nextt
        previous.nextt=None
    def printlist(self):
        temp=self.head
        while (temp!=None):
            print(temp.data,"==>",end='')
            temp=temp.nextt
        print("None") 
obj=Queue()
ch=0
while ch!=4:
    print("QUEUE IMPLEMENTATION USING LINKED LIST\n 1.Enqueue\n 2.Dequeue\n 3.print\n 4.exit\n")
    ch=int(input("Enter the choice:"))
    if ch==1:
           data=input("Enter the value of node:")
           obj.enqueue(data)
           obj.printlist()
    elif ch==2:
           obj.dequeue()
           obj.printlist()
    elif ch==3:
           obj.printlist()
     
