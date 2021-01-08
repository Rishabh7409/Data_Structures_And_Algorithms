# This Program is For Deleting A Linked List Completely


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,node,data):
        if self.head==None:
            self.head=Node(data)
        elif node.next!=None:
            self.insert(node.next,data)
        elif node.next==None:
            node.next=Node(data)
            return

    def traverse(self,node):
        if node==None:
            print("\n\nNo Nodes Left")
            return
        print(node.data,end=' ')
        self.traverse(node.next)

    def deletelist(self,node):
        if node==None:
            return
        else:
            temp=node
            node=node.next
            temp.next=None
            self.deletelist(node)
        self.head=None

if __name__ == "__main__":
    L=linkedlist()
    L.insert(L.head,12)
    L.insert(L.head,13)
    L.insert(L.head,14)
    L.insert(L.head,15)
    L.insert(L.head,16)

    L.traverse(L.head)
    print()
    print("\nDeleting Linked List")
    L.deletelist(L.head)
    L.traverse(L.head)
