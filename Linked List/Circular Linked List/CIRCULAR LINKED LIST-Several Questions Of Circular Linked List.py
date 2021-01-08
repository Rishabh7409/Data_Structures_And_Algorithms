
# this Program Contains Some Questions Of Circular Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinked:
    def __init__(self):
        self.head=None

    #Create a new linked list
    def insert(self,head,data):
        node=head
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            newnode.next=self.head
            return
        while node.next!=self.head:
            node=node.next
        node.next=newnode
        newnode.next=self.head

    #Display the linked list   
    def displaycircular(self,head):
        '''current=head
        if head is None:return
        while True:
            print(current.data,end=' -> ')
            current=current.next
            if current==head:break
        '''
        if head==None:return
        print(head.data,end=' -> ')
        head=head.next
        if head==self.head:return
        else:return self.displaycircular(head)

    #Inserting data in sorted order 
    def insertsorted(self,head,key):
        newnode=Node(key)
        if head is None:
            newnode.next=newnode
            self.head=newnode
        else:
            temp=head
            node=head
            while node.data<=key and node.next!=self.head:
                temp=node
                node=node.next
            if node==self.head:
                curr=temp
                while curr.next!=self.head:curr=curr.next
                curr.next=newnode
                newnode.next=temp
                self.head=newnode
            elif node.next==self.head:
                newnode.next=node.next
                node.next=newnode
            else:
                newnode.next=node
                temp.next=newnode

    #delete a given node from the linked list
    def deletenode(self,head,key):
        node=head
        if head.data==key:
            curr=head
            while curr.next!=head:curr=curr.next
            curr.next=self.head.next
            temp=self.head
            self.head=temp.next
            temp.next=None
        else:
            while node.next.data!=key and node.next.next!=self.head:
                node=node.next

            if node.next.data==key and node.next.next!=self.head:
                temp=node.next.next
                node.next.next=None
                node.next=temp

            elif node.next.data==key and node.next.next==self.head:
                node.next.next=None
                node.next=self.head
                
            else:
                print("\nKey Not found...\n")
                
    #Counting the no. of  nodes in the circular linked list
    def count(self,head):
        if head.next==self.head:
            return 1
        return 1+self.count(head.next)

    #Exchanging First and Last Nodes
    def exchange(self,head):
        node=head
        while node.next.next!=head:
            node=node.next

        node.next.next=head.next
        self.head.next=node.next

        node.next=head
        self.head=self.head.next
        
if __name__ == "__main__":
    C=CircularLinked()
    # for i in range(int(input("Enter nodes: "))):
    #     C.insert(C.head,int(input("\nEnter data: ")))
    # print("\nThe Circular Linked List Is:")
    # C.displaycircular(C.head)

    
    print("\n\n")
    for x in range(6):
        C.insertsorted(C.head,int(input("Enter Data to insert In Sorted Order\t")))
    print("\nThe Circular Linked List Is:")
    C.displaycircular(C.head)

    # to delete a node 
    C.deletenode(C.head,int(input("Enter data to delete")))
    C.displaycircular(C.head)

    # print("\n\nThe Number of Nodes Of circular Linked List are:",end='')
    # print(C.count(C.head))

    print("\nExchanging First and Last Nodes")
    C.exchange(C.head)
    C.displaycircular(C.head)
