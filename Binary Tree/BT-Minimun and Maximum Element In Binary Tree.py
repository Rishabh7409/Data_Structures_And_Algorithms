class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Binary_Tree:
    # taking -infinite as maximum value
    max_val=float('-inf')

    # taking infinite as minimum value
    min_val=float('inf')


    # We have find the min and max element using inorder traversal 
    # you can use any traversal technique
    
    def Inorder(self,node):
        if not node:return

        self.Inorder(node.left)

        # if current node's data is less than minimum value then this is the new minimum value
        if node.data<self.min_val:
            self.min_val=node.data

        # if current node's data is greater than maximum value then this is the new maximum value
        elif node.data>self.max_val:
            self.max_val=node.data

        self.Inorder(node.right)

        return self.min_val,self.max_val   # return minimum and maximum value

if __name__=='__main__':

    rootnode=Node(25)

    rootnode.left=Node(2)
    rootnode.left=Node(1)
    rootnode.left.right=Node(34)
    rootnode.left.left=Node(21)
    rootnode.left.left.left=Node(25)
    rootnode.left.left.right=Node(27)
    rootnode.right=Node(56)
    rootnode.right.right=Node(28)
    rootnode.right.left=Node(57)

    B=Binary_Tree()
    L=B.Inorder(rootnode)

    print("Minimun Element:",L[0],"\nMaximum Element:",L[1])