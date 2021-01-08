'''

The Left View Of The Tree Is The Nodes That Are Visible From Left Side Of The Tree

We Can Find The Left View Of Tree By Finding The Left Most Node of each level..

                      20
                    /    \
                  8       22
                /   \     / \
               5    3   19   25
                    / \      
                  10   14
        
    The Left View Of Above Tree Is : 20 8 5 10

'''


class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Left_View_Tree:
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

    
    def Left_View(self,node):

        if not node:
            return 0
        Q=[node]
        final=list()
        while True:
            P=[]
            count=len(Q) 
            if not count:
                return final
            while count:
                temp=Q.pop(0)
                P.append(temp.data)
                if temp.left:Q.append(temp.left)
                if temp.right:Q.append(temp.right)
                count-=1
            final.append(P[0]) # insert starting node of the current level

                
if __name__=='__main__':
    T=Left_View_Tree()
    T.insert(50,T.root)
    T.insert(40, T.root)
    T.insert(55, T.root)
    T.insert(60, T.root)
    T.insert(61, T.root)
    T.insert(35, T.root)
    T.insert(42, T.root)
    T.insert(41, T.root)
    T.insert(46, T.root)
    T.insert(45, T.root)
    T.insert(48, T.root)
    T.insert(42, T.root)
    
    D=T.Left_View(T.root)
    if D:
        print("\n\nLeft View Of This Binary Tree Is:",*D)
    else:
        print("Tree Not Created")