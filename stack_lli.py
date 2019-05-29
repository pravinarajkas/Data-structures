class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class Stack:
    def __init__ (self):
        self.head=None
    def push(self,data):
        temp=node(data)
        temp.nextt=self.head
        self.head=temp
    def pop(self):
        temp=self.head
        self.head=self.head.nextt
        temp.next=None
    def peek_or_top(self):
        temp=self.head
        print(temp.data,"is the top element")
    def isempty(self):
        if self.head==None:
            print("Stack is empty")
    def printlist(self):
        temp=self.head
        while temp!=None:
            print(temp.data,"==>",end='')
            temp=temp.nextt
        print("None")
obj=Stack()
ch=0
while ch!=6:
    print("linked list implementation\n 1.push\n 2.pop\n 3.peek_or_top\n 4.isempty\n 5.print\n 6.exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        data= int (input("enter the value of node:"))
        
        obj.push(data)
        obj.printlist()
    elif ch==2:
        obj.pop()
        obj.printlist()
    elif ch==3:
        obj.peek_or_top()
    elif ch==4:
        obj.isempty()
    elif ch==5:
        obj.printlist()
