def create_queue():
    queue=[]
    return queue
def enqueue(queue,item):
    queue.append(item)
    print(item,"is pushed to queue")
def dequeue(queue):
    b=len(queue)
    if b==0:
        return -1
    else:
        return queue.pop(0)
str=createqueue()
ch=0
while ch!=5:
    ch=int(input("Enter the choice:"))
    if ch==1:
        p=int(input("Enter the data:"))
        a=enqueue(str,p)
        print("The queue is:",str)
    elif ch==2:
        a=dequeue(str)
        print(a)
        print("The queue is:",str)
        
