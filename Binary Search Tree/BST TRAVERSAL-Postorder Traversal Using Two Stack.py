'''

In this program we will we finding the postorder traversal of Tree Using Two Stacks

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Postorder_Traversal:
    def __init__(self):
        self.root=None

    def insert(self,data,node):
        if node is None:
            #if node node is empty
            self.root=Node(data)

        else:
            # if current data is less than node's data then insert in left subtree
            if data<node.data:

                if node.left is None: # if node has no left child 
                    node.left=Node(data)
                else:
                    self.insert(data,node.left) #recursive call to insert element

            # if current data is less than node's data then insert in left subtree
            else:

                if node.right is None: # if node has no right child 
                    node.right=Node(data)
                else:
                    self.insert(data,node.right) #recursive call to insert element

    def postorder_using_stack(self,node):
        # If Tree Is Empty

        if not node:
            return
        else:
            S1=[]
            S2=[]
            while S1 or node:
                if node:
                    S1.append(node)
                    S2.append(node)
                    node=node.right
                else:
                    node=S1.pop()
                    node=node.left
            while S2:
                print(S2.pop().data,end=' -> ')

if __name__=='__main__':

    P=Postorder_Traversal()
    
    P.insert(20,P.root)
    P.insert(10, P.root)
    P.insert(24, P.root)
    P.insert(14, P.root)
    P.insert(23, P.root)
    P.insert(1, P.root)
    P.insert(30, P.root)
    print("\nPostorder Traversal :",end=' ')
    P.postorder_using_stack(P.root)