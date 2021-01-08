
'''

    DEqueue : Double Ended Queue
    In DEqueue we can insert data from both ends and delete data from both ends..

'''


class createNode:

    def __init__(self,data=None,rear=None):
        self.data=data
        self.rear=None

class DEqueueLinkedlist:

    def __init__(self):
        self.front=None

    def createqueue(self,data):
        node=createNode(data)
        if self.front==None:
            self.front=node
            self.rear=node
        else:
            self.rear.rear=node
            self.rear=node
        
    def insertfront(self,data):
        node=createNode(data)
        print("\nInserting The Element At the front of the Double Ended Queue...\n")
        if self.front==None:self.front=node
        else:
            node.rear=self.front
            self.front=node

    def removefront(self):
        print("Removing The Front Element of the Double Ended Queue...\n")
        if self.front==None:print("UNDERFLOW")
        else:
            temp=self.front.rear
            self.front.rear=None
            self.front=temp

    def insertlast(self,data):
        print("Inserting Element at the Last of Double Ended Queue...\n")
        node=createNode(data)
        if self.front==None:
            self.front=node
            self.rear=node
        else:
            self.rear.rear=node
            self.rear=node

    def removelast(self):
        print("Removing The Last Element of the Double Ended Queue...\n")
        if self.rear==None:print("\nUNDERFLOW")
        else:
            current=self.front
            while current.rear!=self.rear:current=current.rear
            self.rear=current
            current.rear=None

    def displayDEqueue(self):
        print("The Double Ended Queue Is...\n")
        current=self.front
        while current.rear!=None:
            print(current.data)
            current=current.rear
        print(current.data)

if __name__ == "__main__":
    DE=DEqueueLinkedlist()
    for i in range(int(input("Enter the no. of elements of DEqueue..."))):
        DE.createqueue(input("\nEnter the data : "))
    DE.displayDEqueue()

    DE.insertfront(input("\nEnter the data to insert in front...."))
    DE.displayDEqueue()

    DE.insertlast(input("\nEnter the data to insert in last...."))
    DE.displayDEqueue()

    DE.removelast()
    DE.displayDEqueue()

    DE.removefront()
    DE.displayDEqueue()
