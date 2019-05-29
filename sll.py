class Node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
class SLL:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        temp=Node(data)
        temp.nextt=self.head
        self.head=temp
    def insertatmiddle(self,data,N):
        temp=Node(data)
        previous=self.head
        while previous.data!=N:
            previous=previous.nextt
        temp.nextt=previous.nextt
        previous.nextt=temp
    def insertatend(self,data):
        temp=Node(data)
        previous=self.head
        while(previous.nextt):
            previous=previous.nextt
        previous.nextt=temp
        temp.nextt=None
    def deleteatbeg(self):
        temp=self.head
        
        self.head=self.head.nextt
        temp.nextt=None
    def deleteatmiddle(self,data):
        previous=temp=self.head
        if temp==None:
            print("List is empty")
        else:
            while(temp.data!=data):
                temp=temp.nextt
            previous.nextt=temp.nextt
            temp.nextt=None
    def deleteatend(self):
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
        
obj=SLL()
ch=0
while ch!=8:
    print("LINKED LIST IMPLEMENTATION \n 1.insertion at beginning\n 2.insertion at middle\n 3.insertion at end\n 4.deletion at beginning\n 5.deletion at middle\n 6.deletion at end\n 7.printlist\n 8.exit\n")
    ch=int(input("Enter the choice:"))
    if ch==1:
           data=input("Enter the value of node:")
           obj.insertatbeg(data)
           obj.printlist()
    elif ch==2:
           data=input("Enter the value of node:")
           N=input("Enter the position where the node to be inserted:")
           obj.insertatmiddle(data,N)
           obj.printlist()
           
    elif ch==3:
           data=input("Enter the value of node:")
           obj.insertatend(data)
           obj.printlist()
           
    elif ch==4:
           obj.deleteatbeg()
           obj.printlist()
    elif ch==5:
           data=input("Enter the node to be deleted:")
           obj.deleteatmiddle(data)
           obj.printlist()
    elif ch==6:
           obj.deleteatend()
           obj.printlist()
    elif ch==7:
           obj.printlist()
           
           
