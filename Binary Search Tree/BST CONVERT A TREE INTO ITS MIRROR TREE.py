'''USING POSTORDER TRAVERSAL'''

'''The Inorder traversal of a BST and the mirror of BST must be reversed to each other..if it is then we have succe
    -ssfully converted the BST into its mirror tree..
    As soon as we are getting a node we will swap its left and right child to get the mirror tree of the BST
    '''

class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Binary:
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


    def convertToMirror(self,node):
        #Using Postorder Traversal

        if not node:return
        self.convertToMirror(node.left)
        self.convertToMirror(node.right)
        node.left,node.right=node.right,node.left

    def Inorder(self,node):
        if not node:return
        self.Inorder(node.left)
        print(node.data,end=' ')
        self.Inorder(node.right)


if __name__=='__main__':
    B=Binary()

    B.insert(56,B.root)
    B.insert(20,B.root)
    B.insert(45,B.root)
    B.insert(67,B.root)
    B.insert(87,B.root)
    B.insert(50,B.root)
    B.insert(223,B.root)
    B.insert(5,B.root)
    B.insert(58,B.root)
    B.insert(22,B.root)

    B.Inorder(B.root)

    print("\n\nConverting To Its Mirror Tree:\n")

    B.convertToMirror(B.root)

    B.Inorder(B.root)