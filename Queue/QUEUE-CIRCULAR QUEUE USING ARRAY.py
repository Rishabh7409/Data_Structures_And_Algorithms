import numpy
class circular_queue:

    def __init__(self):
        self.n=int(input("No.Of Elements In Array:"))
        self.front=-1
        self.rear=-1
        self.Q=[0]*self.n
        self.Q=numpy.array(self.Q)

    def peek(self):
        if self.n!=0:print("The Front Element Of The Queue Is:",self.Q[self.front])

    def enque(self,data):
        if self.n==0 or (self.rear+1)%self.n==self.front:
            print("Only",self.n,"Elements Can Be Inserted...Cannot Insert",data)
        elif self.front == -1 and self.rear == -1:
            print("Inserting Data",data)
            self.front = self.rear = 0
            self.Q[self.rear] = data

        else:
            print("Inserting Data",data)
            self.rear=(self.rear+1)%self.n
            self.Q[self.rear]=data

    def display(self):
        if self.front!=-1:
            print("The Queue Is:",end=" ")
            i=self.front
            while i!=self.rear:
                print(self.Q[i],end= " ")
                i=(i+1)%self.n
            print(self.Q[i])

    def deque(self):
        if self.front==-1 and self.rear==-1:
            print("Empty Queue")
        elif self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.n

if __name__=='__main__':
    C=circular_queue()
    C.enque(23)
    C.enque(24)
    C.enque(25)
    C.enque(26)
    C.enque(27)
    C.enque(28)
    C.display()
    print("Removing Front Element\n")
    C.deque()
    C.display()
    print("Removing Front Element\n")
    C.deque()
    C.display()
    print("Removing Front Element\n")
    C.deque()
    C.display()
    print("Enquing Some More Elements")
    C.enque(34)
    C.enque(336)
    C.peek()
    C.display()