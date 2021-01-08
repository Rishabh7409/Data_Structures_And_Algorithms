# This Is A Program For Circular Linked List

'''
Topics Covered:
    1. Insertion
    2. Insertion In Beginning
    3.Insertion At Specified Position
    4.Deletion Of First Node
    5.Deletion Of last Node
    6.Deletion Of Specified Node

'''
class circularListNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None

class CircularLinkedList:
    length=0
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode=circularListNode(data)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head
        else:
            current=self.head
            while current.next!=self.head:current=current.next
            current.next=newnode
            newnode.next=self.head

    # Display The Linked List
    def displayList(self):
        self.length=0
        current=self.head

        while current.next!=self.head:
            print(current.data,end=' -> ')
            current=current.next
            self.length+=1

        self.length+=1
        print(current.data)
        print("\nThe Length Of Linked List Is : ",self.length)

    # Insert In Begininning of linked list
    def insert_Begin(self,data):
        print(f"\nThe Linked List After Inserting Element {data} in beginning\n")
        newnode=circularListNode(data)
        if self.head:
            current=self.head
            while current.next!=self.head:current=current.next
            current.next=newnode
            newnode.next=self.head
            self.head=newnode

    # Insert In Last of linked list
    def insert_Last(self,data):
        print(f"\nThe Linked List After Inserting Element {data} in last\n")
        newnode=circularListNode(data)
        if self.head:
            current=self.head
            while current.next!=self.head:current=current.next
            newnode.next=current.next
            current.next=newnode
        else:
            self.head=newnode

    # Insert At Specified Position In linked list
    def insertAtPosition(self,data,n):
        if n>self.length+1 or n==0:
            print("\nPosition Out of length og linked list\n")
            return
        
        # if specified position is first position
        elif n==1:
            CircularLinkedList.insert_Begin(self,data)
            return

        else:
            newnode=circularListNode(data)
            current=self.head
            m=1 # counter for finding position to insert element  
            print(f"\n\nThe Single Linked List After Inserting Element {data} At {n}th Position")
            while m<n-1:
                current=current.next
                m+=1
            newnode.next=current.next
            current.next=newnode
    
    # Delete First Element of LinkedList
    def deleteFirst(self):
        print("\nDeleting First Node.................")
        print("The Linked List After Deleting First Node\n")

        current=self.head
        temp=current.next

        while current.next!=self.head:
            current=current.next
        current.next=temp
        self.head.next=None
        self.head=temp

    # Delete Last Element Of Linked List
    def deleteLast(self):
        print("\nDeleting Last Node..................")
        print("The Linked List after deleting last node\n")

        temp=current=self.head
        while current.next.next!=self.head:
            current=current.next
        current.next=temp

    # Delete at specified position
    def deleteAtPosition(self,n):
        if n==1:CircularLinkedList.deleteFirst(self)
        elif n>self.length:print("\nCannot Delete.......\n")
        else:
            print(f"\nDeleting {n} node........")
            print("The Linked List After Deleting {} node..\n".format(n))
            current=self.head
            while n>2:
                current=current.next
                n-=1
            temp=current.next
            current.next=current.next.next
            temp.next=None
        
if __name__ == "__main__":
         
    S=CircularLinkedList()
    n=int(input("\nEnter the number of nodes of circular linked list...."))
    for i in range(n):
        m=int(input(f"\nEnter the data of {i+1} node"))
        S.insert(m)

    print("\nThe Single Circular Linked List is...\n")
    S.displayList()

    m=int(input("Enter the data to insert at beginning"))
    S.insert_Begin(m)
    S.displayList()

    m=int(input("Enter data to store data in last\n"))
    S.insert_Last(m)
    S.displayList()

    m=int(input("\nEnter The number of node where u want to insert node\n"))
    n=int(input(f"Enter the data to insert at {m} position\n"))
    S.insertAtPosition(n,m)
    S.displayList()

    # S.deleteFirst()
    # S.displayList()

    # S.deleteLast()
    # S.displayList()

    # n=int(input("\nEnter the node to be deleted......."))
    # S.deleteAtPosition(n)
    # S.displayList()
