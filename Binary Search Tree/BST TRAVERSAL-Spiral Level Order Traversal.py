'''

    In Spiral Level Order Traversal Of Tree We First Traverse Even numbered Levels Fron Left To Right and Odd Numbered Levels From Right To Left

                      20            --Level 0
                    /    \
                  8       22        --Level 1
                /   \     / \
               5    3   19   25     --Level 2
                    / \      
                  10   14           --Level 3
        
    The Spiral Level Order Traversal Of The Binary Tree Will Be 20 22 8 5 3 19 25 14 10



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
        S=[]
        Q.append(node)
        while True:
            # This Queue Is Used For Traversing The Even Numbered Levels from left to right
            while Q:
                temp = Q.pop()
                if temp:
                    print(temp.data, end=' ')
                    S.append(temp.left)
                    S.append(temp.right)
            
            # This Queue Is Used For Traversing The Odd Numbered Levels from right to left
            while S:
                temp = S.pop()
                if temp:
                    print(temp.data, end=' ')
                    Q.append(temp.right)
                    Q.append(temp.left)
            if not Q and not S: return

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

    print("\n\nSpiral Level Order Traversal:")
    B.levelorder(B.root)