
'''

Diameter Of Binary Tree: 
    The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes

'''


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

    #Recursive Method
    def height(self,node):
        if node is None:return 0

        lh=self.height(node.left)
        rh=self.height(node.right)
        if lh>rh:return lh+1
        return rh+1

    def diameterOfBinaryTree(self,root,diameter) :
        if not root:
            return 0
        
        # left height
        left_diameter=self.diameterOfBinaryTree(root.left,diameter)

        # right height
        right_diameter=self.diameterOfBinaryTree(root.right,diameter)

        # diameter is the sum of tree's left subtree height and right subtree height 

        diameter=max(diameter,1+left_diameter+right_diameter)

        return 1+max(left_diameter,right_diameter)


if __name__=='__main__':
    B=Tree()
    B.insert(40,B.root)
    B.insert(35,B.root)
    B.insert(70, B.root)
    B.insert(65, B.root)
    B.insert(60, B.root)
    B.insert(55, B.root)
    B.insert(50, B.root)
    B.insert(45, B.root)
    B.insert(75, B.root)
    B.insert(74, B.root)
    B.insert(73, B.root)
    B.insert(72, B.root)
    B.insert(71, B.root)
    
    print(B.diameterOfBinaryTree(B.root,-100))