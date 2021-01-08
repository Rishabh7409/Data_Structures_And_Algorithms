
'''
                      20
                    /    \
                  8       22
                /   \     / \
               5    3   19   25
                    / \      
                  10   14

Boundary Traversal : 20 8 5 10 14 19 25 22

We break the problem in 4 parts:

Steps:

   1.Traverse The Root Node
   2.Visit The Leftmost Subtree diagonally Until Leaf Node is Encountered..Do not print Leaf Node Of Left Subtree
   3.Visit The Leafnodes and store leaf nodes in a list..print the list in sorted order..
   4.Visit The Rightmost subtree diagonally until Leaf Node Is Encountered..Do not print Leaf Node of Right Subtree
     print the nodes in reverse order i.e. last encountered node must be print first.. '''


class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Binary:
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


    def Boundary_Traversal(self,node):
        print("Boundary Traversal:")
        # starting from root and going in anticlockwise direction
        self.root_data(node)
        
        # left diagonal from root
        self.left_tree(node.left)
        
        # leaf nodes 
        print(*self.leaf_nodes(node),end=' ')

        # right diagonal
        self.right_tree(node.right)

    # Root Node
    def root_data(self,node):
        print(node.data,end=' ')

    # Left Diagonal Traversal From Root Node
    def left_tree(self,node):
        if not node.left:return
        print(node.data,end=' ')
        self.left_tree(node.left)

    # Right Diagonal Traversal From Root Node
    def right_tree(self,node):
        if not node.right:return
        self.right_tree(node.right)
        print(node.data,end=' ')

    # By Doing level Order Traversal We Can get The Leaf nodes of Binary Tree
    def leaf_nodes(self,node):
        Q=[node]
        L=[]
        while True:
            count=len(Q)
            if not Q:return sorted(L)
            while count:
                temp=Q.pop(0)
                if temp.left:Q.append(temp.left)
                if temp.right:Q.append(temp.right)
                if not temp.left and not temp.right:
                    L.append(temp.data)
                count-=1


if __name__=='__main__':

    B=Binary()

    B.insert(56,B.root)
    B.insert(20,B.root)
    B.insert(45,B.root)
    B.insert(67,B.root)
    B.insert(87,B.root)
    B.insert(50,B.root)
    B.insert(223,B.root)
    B.insert(5,B.root)
    B.insert(58,B.root)
    B.insert(22,B.root)

    B.Boundary_Traversal(B.root)