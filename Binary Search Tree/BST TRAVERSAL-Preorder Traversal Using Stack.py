# In this Program we Will Find The Preorder Traversal Of Tree Using Single Stack

class Node:
    def __init__(self,data):

        self.data=data
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,node,data):
        if node is None:
            #if node node is empty
            self.root=Node(data)

        else:
            # if current data is less than node's data then insert in left subtree
            if data<node.data:

                if node.left is None: # if node has no left child 
                    node.left=Node(data)
                else:
                    self.insert(node.left,data) #recursive call to insert element

            # if current data is less than node's data then insert in left subtree
            else:

                if node.right is None: # if node has no right child 
                    node.right=Node(data)
                else:
                    self.insert(node.right,data) #recursive call to insert element

    def iterativePreorder(self,root): 
      
    # Base CAse  
        if root is None: 
            return 
  
    # create an empty stack and push root to it 
        nodeStack = [] 
        nodeStack.append(root) 

        while nodeStack: 
          
        # Pop the top item from stack and print it 
            node = nodeStack.pop() 
            print(node.data,end=' ')
          
        # Push right and left children of the popped node to stack 
            if node.right is not None: 
                nodeStack.append(node.right) 
            if node.left is not None: 
                nodeStack.append(node.left)

B=BinaryTree()
B.insert(B.root,10)
B.insert(B.root,12)
B.insert(B.root,11)
B.insert(B.root,8)
B.insert(B.root,9)
B.insert(B.root,13)


print("\nPreorder Traversal Using Stack : ",end=' ')
B.iterativePreorder(B.root)