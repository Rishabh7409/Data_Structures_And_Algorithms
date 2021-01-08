'''

The Level Order Traversal of The Tree Can Be Find By Traversing The Tree, Level By Level And From Left To Right

                      20            --Level 0
                    /    \
                  8       22        --Level 1
                /   \     / \
               5    3   19   25     --Level 2
                    / \      
                  10   14           --Level 3
        
    The Level Order Traversal Of Above Tree Is : 20 8 22 5 3 19 25 10 14

'''

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Level_Order:
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


    def levelorder(self,node):
        Q=[]
        Q.append(node) # insert root node
        while Q!=[]:
            temp=Q.pop(0) # pop out front node from queue
            
            if temp.left:Q.append(temp.left) # if node is having left child insert into queue

            if temp.right:Q.append(temp.right) # if node is having right child insert into queue

            print(temp.data,end=' -> ') # print current node's data

if __name__=='__main__':
    B=Level_Order()
    B.insert(40,B.root)
    B.insert(35,B.root)
    B.insert(60,B.root)
    B.insert(30,B.root)
    B.insert(37,B.root)
    B.insert(50,B.root)
    B.insert(65,B.root)
    B.insert(32,B.root)
    B.insert(39,B.root)
    B.insert(55,B.root)
    B.insert(63,B.root)
    B.insert(53,B.root)
    
    print("\n\nLevel Order Traversal:")
    B.levelorder(B.root)