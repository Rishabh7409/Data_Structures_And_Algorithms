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
            #if root node is empty
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


    def inOrder_Using_Stack(self,root): 
        # Set current to root of binary tree 
        current = root  
        stack = [] # initialize stack 
      
        while True: 
          
            # Reach the left most Node of the current Node 
            if current is not None: 
                   
                # put current to the stack
                stack.append(current) 
                
                # traverse left subtree
                current = current.left  
  
          
            # BackTrack from the empty subtree and visit the Node 
            # at the top of the stack; however, if the stack is  
            # empty you are done 
            elif(stack): 
                current = stack.pop() 
                print(current.data, end=" ")
          
                #    We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  
  
            else: 
                break

if __name__ == "__main__":
        
    B=BinaryTree()
    B.insert(B.root,10)
    B.insert(B.root,12)
    B.insert(B.root,11)
    B.insert(B.root,8)
    B.insert(B.root,9)
    B.insert(B.root,13)


    print("\nInorder Traversal Using Stack:\n")
    B.inOrder_Using_Stack(B.root)