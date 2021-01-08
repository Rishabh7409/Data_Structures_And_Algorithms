# In This Program We Will Be Creating Binary Tree From Its Preorder And Inorder Traversal

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST_From_Inorder_Preorder:
    def buildTree(self,Inorder,Preorder):
        if len(Inorder)!=len(Preorder) or not Inorder or not Preorder:
            return None
        root=Node(Preorder[0])
        
        # root node
        rootindex=Inorder.index(root.data)

        # recurisve call for left subtree
        root.left=self.buildTree(Inorder[:rootindex],Preorder[1:rootindex+1])

        #recursive call for right subtree
        root.right=self.buildTree(Inorder[rootindex+1:],Preorder[rootindex+1:])

        return root

    def Inorder(self,node):
        if node is None:return
        self.Inorder(node.left)
        print(node.data,end=' ')
        self.Inorder(node.right)

if __name__=='__main__':
    B=BST_From_Inorder_Preorder()
    Preorder=[40,35,30,32,37,39,60,50,55,53,65,63]
    Inorder=sorted(Preorder)
    root=B.buildTree(Inorder,Preorder)
    B.Inorder(root)