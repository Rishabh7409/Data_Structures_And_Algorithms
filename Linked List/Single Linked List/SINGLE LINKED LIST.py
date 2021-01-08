# This Is A Program For Single Linked List

'''
Topics Covered:
    1. Insertion
    2. Insertion In Beginning
    3. Insertion At Specified Position
    4. Deletion Of First Node
    5. Deletion Of last Node
    6. Deletion Of Specified Node
    7. Reverse The Linked List

'''


class Nodecreate:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        newnode=Nodecreate(data)
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
        else:
            self.head=newnode
            #newnode.prev=self.head

    def showlinkedlist(self):
        self.p=0
        current=self.head
        while current:
            self.p+=1
            print(current.data,end=' -> ')
            current=current.next
        print("\nLength Of Linked List: ",self.p)


    def insertlast(self,data):
        print(f"\n\nThe Single Linked List After Inserting Element {data} At Last")
        newnode=Nodecreate(data)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
        else:
            self.head=newnode


    def insertbegin(self,data):
        print(f"\n\nThe Single Linked List After Inserting Element {data} At Beginning")
        newnode=Nodecreate(data)
        if self.head:
            current=self.head
            newnode.next=current
            self.head=newnode
        else:self.head=newnode

    def insertatposition(self,data,n):
        if n>self.p or n==0:
            print(f"\nThe position {n} Is out of length of linked list.\n")
            return
        elif n==1:
            singlelinkedlist.insertbegin(self,data)
            return
        elif n==self.p+1:
            singlelinkedlist.insertlast(self,data)
            return
        else:
            newnode,current,m=Nodecreate(data),self.head,1
            print(f"\n\nThe Single Linked List After Inserting Element {data} At {n}th Position")
            while m<n-1:
                current=current.next
                m+=1
            newnode.next=current.next
            current.next=newnode
            
    def deletebegin(self):
        print("\n\nThe Linked List After Deleting First Node")
        current=self.head
        self.head=current.next
        current.next=None

    def deletelast(self):
        print("\n\nThe Linked List After deleting the node at last position") 
        current=self.head
        while (current.next).next:current=current.next
        current.next=None

    def deletefromposition(self,n):
        if n==self.p:
            print("\n\nSince The Position you have chosen is the last node of linked list.\nTherefore...")
            singlelinkedlist.deletelast(self)
            return
        elif n==1:
            print("\n\nSince The position you have chosen is the beginning of the linked list.Therefore...")
            singlelinkedlist.deletebegin(self)
            return
        elif n>self.p:
            print("\n\nThe position is out of range of linked list")
            return
        else:
            print(f"\n\nThe Linked List After deleting {n}th Node")
            m,current = 1,self.head
            while m<n-1:
                current=current.next
                m+=1
            temp=(current.next).next
            (current.next).next=None
            current.next=temp

    def reverseLinked(self):
        current=self.head
        prev=None
        while current!=None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

if __name__=='__main__':
    #Create an object of linked list class
    S=singlelinkedlist()
    #Inserting Nodes to Linked List
    n=int(input("Enter The Number Of nodes of Single linked list..\t"))
    for i in range(n):
        m=int(input(f"Enter The Data of {i+1} node"))
        S.insert(m)
    print("\nThe Single Linked List Is:\n")
    S.showlinkedlist()

    #Inserting At last
    # m=int(input("\nEnter data to be insert at last\n"))
    # S.insertlast(m)
    # S.showlinkedlist()

    # #Inserting At Beginning
    # m=int(input("\nEnter data to be insert in beginning\n"))
    # S.insertbegin(m)
    # S.showlinkedlist()

    # #Inserting at given position
    # m=int(input("\nEnter the number of node where u want to store the data\n"))
    # n=int(input(f"\nEnter data to be insert at {m} position\n"))
    # S.insertatposition(n,m) #(data,position)
    # S.showlinkedlist()

    # #Deleting The first Node
    # S.deletebegin()
    # S.showlinkedlist()

    # #Deleting The Last Node
    # S.deletelast()
    # S.showlinkedlist()

    # #Deletion from the given position
    # m=int(input("\nEnter the number of node u want to delete"))
    # S.deletefromposition(m)
    # S.showlinkedlist()

    # print("\nReverse of the Linked List\n")
    # S.reverseLinked()
    # S.showlinkedlist()


