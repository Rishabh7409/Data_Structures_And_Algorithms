'''USING LEVEL ORDER TRAVERSAL'''

'''The Inorder traversal of a BST and the mirror of BST must be reversed to each other..if it is then we have succe
    -ssfully converted the BST into its mirror tree..
    As soon as we are getting a node we will swap its left and right child to get the mirror tree of the BST
    '''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Mirror_View:
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


    # Function To convert the Binary Search Tree To its Mirror Form
    def convertToMirror(self,node):
        # Using Level Order Traversal
        Q=[]
        Q.append(node)
        while Q!=[]:
            temp=Q.pop(0)
            if temp.left:Q.append(temp.left)
            if temp.right:Q.append(temp.right)
            '''As soon as we are getting a node we will swap its left and right child to get the mirror view of the tree'''
            temp.left, temp.right = temp.right, temp.left  #swapping left and right childs

if __name__=='__main__':

    # Creating Object of Mirror_View Class
    B=Mirror_View()  

    # Inserting Data

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

    # function call to convert to mirror form
    B.convertToMirror(B.root)


    