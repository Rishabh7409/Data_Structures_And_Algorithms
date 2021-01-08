'''
 This Is A Program For Doubly Linked List
 Topics Covered:
    1. Insertion Using Recursion
    2. Traversal In reverse order
    3. Reversing The Linked List

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinked:
    def __init__(self):
        self.head=None

    def insert(self,node,data):
        if self.head==None:self.head=Node(data)
        elif node.next==None:
            temp=Node(data)
            temp.prev=node
            node.next=temp
            return
        else:self.insert(node.next,data)

    def traverse(self,node):
        if node==None:return
        print(node.data,end=' -> ')
        self.traverse(node.next)

    # Linked List Traversal In reverse Order
    def reversetraverse(self,node):
        if node==None:return
        self.reversetraverse(node.next)
        print(node.data,end=' -> ')

    # Reversing The Actual Linked List
    def reverselinkedlist(self,node):
        if node.next==None:
            node.next,node.prev=node.prev,node.next
            self.head=node
            return
        node.next,node.prev=node.prev,node.next
        self.reverselinkedlist(node.prev)

if __name__ == "__main__":
                
    D=DoubleLinked()
    for i in range(int(input("Enter no. of nodes of linked list.."))):
        D.insert(D.head,input("\nEnter data of {} node".format(i+1)))

    print("\nForward Traversal:")
    D.traverse(D.head)

    print("\n\nTraversal In Reverse Order:")
    D.reversetraverse(D.head)


    print("\n\nReversing The Linked List:")
    D.reverselinkedlist(D.head)
    D.traverse(D.head)

