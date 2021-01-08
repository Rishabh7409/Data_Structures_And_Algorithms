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

    def Height_Of_Tree(self,node):
        if not node:
            return 0
        
        lh=self.Height_Of_Tree(node.left)
        rh=self.Height_Of_Tree(node.right)
        return lh+1 if lh>rh else rh+1


    def Reverse_Level_Order(self,node):
        height=self.Height_Of_Tree(node)
        for i in range(height,0,-1):
            self.Reverse_Level_Order_Util(node,i)
    
    def Reverse_Level_Order_Util(self,node,height):
        if not node:
            return
        if height==1:
            print(node.data,end=' ')
            return

        self.Reverse_Level_Order_Util(node.left,height-1)
        self.Reverse_Level_Order_Util(node.right,height-1)

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
    
    B.Reverse_Level_Order(B.root)