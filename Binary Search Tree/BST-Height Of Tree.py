class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
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


    def inorder(self,node):
        if node==None:
            return
        self.inorder(node.left)
        print(node.data,end=' -> ')
        self.inorder(node.right)

    #Recursive Method
    def height(self,node):
        if node is None:return 0

        lh=self.height(node.left)
        rh=self.height(node.right)
        if lh>rh:return lh+1
        return rh+1

    #Iterative Method
    #This Method Uses Queue and Level Order Traversal Method
    def height_iter(self,node):
        Q=[]
        Q.append(node)
        height=0
        while True:
            count=len(Q)
            if count==0:
                return height
            height+=1
            while count:
                temp=Q.pop(0)
                if temp.left:Q.append(temp.left)
                if temp.right:Q.append(temp.right)
                count-=1

if __name__=='__main__':

    B=Tree()
    
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

    # print("Inorder Traversal:")
    # B.inorder(B.root)
    print("\nThe Height Of The Tree Using Recursion:",B.height(B.root))
    print("\nThe Height Of The Tree Using Iteration:", B.height_iter(B.root))