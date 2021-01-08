# This Is A Program For Doubly Circular Linked List

'''
Topics Covered:
    1. Insertion
    2. Insertion In Beginning
    3. Insertion At Specified Position
    4. Deletion Of First Node
    5. Deletion Of last Node
    6. Deletion Of Specified Node
    7. Reverse of Double Linked List

'''

class LinkedListNode:

    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        
        newnode=LinkedListNode(data)
        if self.head:
            current=self.head
            while current.next:current=current.next
            current.next=newnode
            newnode.prev=current
        else:
            self.head=newnode
            newnode.prev=self.head
            
    def showdouble(self):
        current,self.p=self.head,0
        while current:
            print(current.data,end=' -> ')
            current=current.next
            self.p+=1
        print("\nLength Of Linked List: ",self.p)
    def insertbegin(self,data):
        newnode=LinkedListNode(data)
        print(f"\n\nInserting The Element {data} In Beginning of linked list")
        current=self.head
        current.prev=newnode
        newnode.next=current
        self.head=newnode

    def insertlast(self,data):
        newnode=LinkedListNode(data)
        print(f"\n\nInserting The Element {data} in the last of linked list")
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
        newnode.prev=current

    def insertatposition(self,data,n):
        newnode=LinkedListNode(data)
        print(f"\n\nInserting the element {data} at {n} position")
        m=1
        current=self.head
        while m<n-1:
            current=current.next
            m+=1
        newnode.next=current.next
        newnode.prev=current
        current.next=newnode
        (current.next).prev=newnode

    def deletebegin(self):
        print("\n\nDeleting First Node Of Linked List")
        current=self.head
        current.next.prev=None
        self.head=current.next
    
    def deletelast(self):
        print("\n\nDeleting The Last Node Of Linked List")
        current=self.head
        while current.next.next:
            current=current.next
        current.next.prev=None
        current.next=None

    def delete_from_position(self,n):
        if n==self.p:
            print("\n\nSince the position you have chosen is last elemnet of linked list.\nTherefore...")
            DoubleLinkedList.deletelast(self)
            return
        elif n==1:
            print("\n\nSince The position you have chosen is the beginning of the linked list.Therefore...")
            DoubleLinkedList.deletebegin(self)
            return
        elif n>self.p:
            print("\n\nThe position is out of range of linked list")
            return
        else:
            m,current=1,self.head
            print(f"\n\nDeleting The Element from {n} position")
            while m<n-1:
                    current=current.next
                    m+=1
            temp=current.next
            current.next=temp.next
            temp.next.prev=current
            temp.next=temp.prev=None

    def reverseLinked(self):
        print("\nReversing The Linked List\n")
        current=self.head
        while current.next!=None:
            temp=current.next
            current.next,current.prev=current.prev,current.next
            current=temp
        current.next,current.prev=current.prev,current.next
        self.head=current

if __name__ == "__main__":

    print("*"*10,"DOUBLE LINKED LIST","*"*10)

    D=DoubleLinkedList()
    #Inserting elements to linked list
    D.insert(10)
    D.insert(11)
    D.insert(20)
    D.insert(21)
    D.showdouble()
    
    #Inserting an element at the beginning of linked list
    D.insertbegin(4)
    D.showdouble()
    
    #Inserting an element at last of linked list
    D.insertlast(111)
    D.showdouble()
    
    #Inserting an element at the given position
    D.insertatposition(222,1) #(data,position)
    D.showdouble()
    
    #Deleting the beginning node
    
    #  D.deletebegin()
    # D.showdouble()
    # #Deleting the Last Node
    # D.deletelast()
    # D.showdouble()
    # #Deleting node from the given position
    # D.delete_from_position(1)
    # D.showdouble()
    # #Reversing The Linked List
    # D.reverseLinked()
    # D.showdouble()
