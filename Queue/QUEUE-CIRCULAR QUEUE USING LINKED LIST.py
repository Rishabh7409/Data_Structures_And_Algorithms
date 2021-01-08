class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_Linked:
    def __init__(self):
        self.front=None
        self.rear=None

    def Enque(self,data):
        if not self.front and not self.rear:
            newnode=Node(data)
            self.front=self.rear=newnode
            newnode.next = self.rear
        else:
            newnode=Node(data)
            self.rear.next=newnode
            newnode.next=self.front
            self.rear=newnode

    def display(self):
        if not self.front and not self.rear:
            print("Empty Linked List")
            return
        print("The Queue Is:",end=" ")
        temp=self.front
        while temp.next!=self.front:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data)

    def deque(self):
        print("Removing Front Element Of The Queue")
        if not self.front and not self.rear:
            print("There Is No Linked List")
        elif self.front==self.rear: #if front and rear are pointing to same element
            self.front=self.rear=None
        else:
            self.rear.next=self.front.next
            self.front=self.front.next

    def peek(self):
        if self.front and self.rear:
            print("The Front Element Of Circular Queue Is:",self.front.data)

if __name__=='__main__':
    C=Circular_Linked()
    C.Enque(1)
    C.Enque(2)
    C.Enque(3)
    C.Enque(4)
    C.display()
    C.deque()
    C.display()
    C.peek()