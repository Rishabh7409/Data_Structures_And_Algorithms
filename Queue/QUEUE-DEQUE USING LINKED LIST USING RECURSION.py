# DEqueue : Double Ended Queue

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class DEQUEUE:
    def __init__(self):
        self.head=None
        self.end=None

    def Insert_End(self,data,node):
        if self.head is None:
            self.head=Node(data)
            self.end=Node(data)
        elif node.next is None:
            node.next=Node(data)
            node.end=Node(data)
        else:
            self.Insert_End(data,node.next)

    def display(self,node):
        if not node:return
        print(node.data,end=' ')
        self.display(node.next)

    def Insert_Begin(self,data):
        temp=self.head
        self.head=Node(data)
        self.head.next=temp

    def Delete_Begin(self):
        temp=self.head.next
        self.head.next=None
        self.head=temp

    def Delete_Last(self):
        node=self.head
        while node.next.next!=None:
            node=node.next
        node.next=None

if __name__=='__main__':
    D=DEQUEUE()
    D.Insert_End(34,D.head)
    D.Insert_End(35, D.head)
    D.Insert_End(36, D.head)
    D.Insert_End(37, D.head)
    D.Insert_End(38, D.head)
    D.display(D.head)
    D.Insert_Begin(89)
    print("\nInsert Begin:",end=' ')
    D.display(D.head)
    print("\nDelete Begin:",end=' ')
    D.Delete_Begin()
    D.display(D.head)
    print("\nDelete Last:",end=' ')
    D.Delete_Last()
    D.display(D.head)