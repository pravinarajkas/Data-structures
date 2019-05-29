def create_stack():
    stack=[]
    return stack
def push(stack,item):
    stack.append(item)
    print(item,"is pushed to stack")
def pop(stack):
    b=len(stack)
    if b==0:
        return -1
    else:
        return stack.pop()
str=createstack()
ch=0
while ch!=5:
    ch=int(input("Enter the choice:"))
    if ch==1:
        p=int(input("Enter the data:"))
        a=push(str,p)
        print("The stack is:",str)
    elif ch==2:
        a=pop(str)
        print(a)
        print("The stack is:",str)
