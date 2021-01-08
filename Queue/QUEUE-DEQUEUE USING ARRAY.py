# DEqueue using Arrays

import numpy
class Dequeue_Array:
    def __init__(self,n):
        self.n=n
        self.front=-1
        self.rear=-1
        self.Q=numpy.ndarray(shape=self.n,dtype=int)

    def Enque_front(self,data):

        if (self.front==0 and self.rear==self.n-1) or self.rear+1==self.front:
            print("Only",self.n,"Elements Can Be Inserted, Cannot Insert",data)

        elif self.front==-1 and self.rear==-1:
            print("Inserting In Front",data)
            self.front=self.rear=0
            self.Q[self.front]=data

        elif self.front==0:
            print("Inserting In Front", data)
            self.front=self.n-1
            self.Q[self.front]=data
        else:
            print("Inserting In Front", data)
            self.front-=1
            self.Q[self.front]=data

    def Enque_rear(self,data):
        if self.front == -1 and self.rear == -1:
            print("Inserting In Last", data)
            self.front = self.rear = 0
            self.Q[self.rear] = data

        elif (self.front==0 and self.rear==self.n-1) or self.rear+1==self.front:
            print("Only",self.n,"Elements Can Be Inserted Cannot Insert",data)

        elif self.rear==self.n-1:
            print("Inserting In Last", data)
            self.rear=0
            self.Q[self.rear]=data
        else:
            print("Inserting In Last", data)
            self.rear+=1
            self.Q[self.rear]=data

    def delete_front(self):
        if self.front==-1 and self.rear==-1:
            print("DEqueue Is Empty:")

        elif self.front==self.rear:
            print("Deleting Front Element:",self.Q[self.front])
            self.front=self.rear=-1

        elif self.front==self.n-1:
            print("Deleting Front Element:", self.Q[self.front])
            self.front=0
        else:
            print("Deleting Front Element:", self.Q[self.front])
            self.front+=1

    def delete_rear(self):
        if self.front==-1 and self.rear==-1:
            print("DEqueue Is Empty:")

        elif self.front==self.rear:
            print("Deleting rear Element:",self.Q[self.rear])
            self.rear=self.rear=-1

        elif self.rear==0:
            print("Deleting rear Element:", self.Q[self.rear])
            self.rear=self.n-1
        
        else:
            print("Deleting rear Element:", self.Q[self.rear])
            self.rear-=1

    def getfront(self):
        if self.front!=-1 and self.rear!=-1:
            print("Front Element:",self.Q[self.front])
        else:
            print("Queue Is Empty")

    def get_rear(self):
        if  self.front!=-1 and self.rear != -1:
            print("Rear Element:", self.Q[self.rear])
        else:
            print("Queue Is Empty")

    def display_deque(self):
        print("\nThe DEqueue Is:",end=' ')
        i=self.front
        while i!=self.rear:
            print(self.Q[i],end=" ")
            i=(i+1)%self.n
        print(self.Q[i])

if __name__=='__main__':
    n=int(input("How Many Elements In Array??"))
    Q=Dequeue_Array(n)
    for i in range(n):
        Q.Enque_front(int(input("Enter Data")))

    
    Q.display_deque()
    Q.delete_front()
    Q.display_deque()
    Q.delete_rear()
    Q.display_deque()
    Q.Enque_rear(56)
    Q.display_deque()
    Q.Enque_front(90)
    Q.display_deque()
    Q.Enque_rear(45)
    Q.display_deque()
    Q.get_rear()
    Q.getfront()