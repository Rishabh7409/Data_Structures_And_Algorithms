# This Is A Program For Doubly Circular Linked List

'''
Topics Covered:
    1. Insertion
    2. Insertion In Beginning
    3.Insertion At Specified Position
    4.Deletion Of First Node
    5.Deletion Of last Node
    6.Deletion Of Specified Node

'''

class createNode:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoublyCircular:
    length=0
    def __init__(self):
        self.head=None

    def insertnode(self,data):
        newnode=createNode(data)
        if self.head==None:
            self.head=newnode
            newnode.next=newnode
        else:
            current=self.head
            while current.next!=self.head:current=current.next
            current.next=newnode
            newnode.prev=current
            newnode.next=self.head

    def displaylist(self):
        self.length=0
        current=self.head
        print("\nThe Doubly Circular Linked List Is :",end=' ')
        while current.next!=self.head:
            print(current.data,end=' -> ')
            current=current.next
            self.length+=1
        print(current.data)
        print("\nThe Length Of the Linked List Is: ",self.length+1)

    def insertbegin(self,data):
        newnode=createNode(data)
        current=self.head
        print(f"\nInserting element {data} in beginning of linked list ")
        while current.next!=self.head:current=current.next
        current.next=newnode
        self.head.prev=newnode
        newnode.next=self.head
        self.head=newnode

    def insertlast(self,data):
        newnode=createNode(data)
        current=self.head
        print(f"\nInserting element{data} in last of linked list")
        while current.next!=self.head:current=current.next
        newnode.next=current.next
        newnode.prev=current
        current.next=newnode

    def insertatposition(self,data,n):
        if n==1:
            DoublyCircular.insertbegin(self,data)
        if n>self.length+2:print("\nCannot Insert...")
        else:
            print(f"\nThe Doubly Circular Linked List After Inserting element {data} at {n} position of linked list\n")
            newnode=createNode(data)
            current=self.head
            while n>2:
                 current=current.next
                 n-=1
            current.next.prev=newnode
            newnode.next=current.next
            newnode.prev=current
            current.next=newnode
            current.prev=newnode

    def deletebegin(self):
        print("\nDeleting the first node..\n")
        current=self.head
        temp=self.head
        while current.next!=self.head:current=current.next
        current.next=temp.next
        temp.next.prev=None
        self.head=temp.next
        temp.next=None

    def deletelast(self):
        print("\nDeleting The Last Node...\n")
        current=self.head
        while current.next.next!=self.head:current=current.next
        current.next.next=current.next.prev=None
        current.next=self.head

    def deletefromposition(self,n):
        print(f"\nDeleting The Node from {n} position")
        current=self.head
        while n>2:
            current=current.next
            n-=1
        temp=current.next
        current.next.next.prev=current
        current.next=current.next.next
        temp.next=temp.prev=None
    
if __name__ == "__main__":
    D=DoublyCircular()
    n=int(input("Enter no. of nodes you want to create for Doubly Circular Linked List..."))
    for i in range(n):
        m=input(f"\nEnter data of {i+1} node : ")
        D.insertnode(m)
    D.displaylist()

    n=input("\nEnter data to insert in beginnning ")
    D.insertbegin(n)
    D.displaylist()
    print("\n")

    n=input("\nEnter data to insert in the last of linked list\n")
    D.insertlast(n)
    D.displaylist()
    print("\n")

    n=int(input("\nEnter the position to insert the node"))
    m=input(f"Enter the data to insert at {n} position")
    D.insertatposition(m,n)
    D.displaylist()
    print("\n")

    # D.deletebegin()
    # D.displaylist()

    # D.deletelast()
    # D.displaylist()

    # n=int(input("Enter the no. of node to delete"))
    # D.deletefromposition(n)
    # D.displaylist()
