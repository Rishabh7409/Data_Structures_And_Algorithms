def Enqueue(Q,data):
    Q.append(data)

def Remove(Q):
    Q.pop(0)

def display(Q):
    print("The Queue Is:",Q)

if __name__=='__main__':
    Q=[]
    n=int(input("Enter Elements Of Queue:"))
    for i in range(n):
        data=input("Enter Data:")
        Enqueue(Q,data)
    display(Q)
    x=int(input("Enter 1 To Delete Last Element Of Queue"))
    if x==1:Remove(Q)
    display(Q)
    x=int(input("Enter 1 To View First Element Of Queue"))
    if x==1:print("First Element Of Queue:",Q[0])

