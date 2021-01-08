# This Program is To Remove Duplicates in a sorted  Circular Linked List

class CircularNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular:
    def __init__(self):
        self.head=None

    def insert(self,node,data):
        newnode=CircularNode(data)
        if node==None:
            self.head=newnode
            newnode.next=self.head
        else:
            current=node
            while current.next!=node:current=current.next
            newnode.next=current.next
            current.next=newnode

    # This function is To Remove Duplicates in a sorted  Circular Linked List
    def removeduplicates(self,node):
        current=node
        while current.next!=self.head:
            # if nodes are same
            if current.data==current.next.data:
                temp=current.next
                current.next=current.next.next
                temp.next=None
            else:
                current=current.next

    def traversal(self,node):
        #USING RECURSION
        if node.next==self.head:
            print(node.data)
            return          
        print(node.data,end=' -> ')
        self.traversal(node.next)

        #USING ITERATION
        '''
        current=node
        while current.next!=node:
            print(current.data,end=' ')  
            current=current.next
        print(current.data)'''
 

if __name__ == "__main__":
    
    C=Circular()

    C.insert(C.head,23)
    C.insert(C.head,23)
    C.insert(C.head,25)
    C.insert(C.head,25)
    C.insert(C.head,25)
    C.insert(C.head,28)
    C.insert(C.head,28)
    
    print("Before Removing Duplicates")
    C.traversal(C.head)

    C.removeduplicates(C.head)
    print("\nAfter Removing Duplicates ")
    C.traversal(C.head)

