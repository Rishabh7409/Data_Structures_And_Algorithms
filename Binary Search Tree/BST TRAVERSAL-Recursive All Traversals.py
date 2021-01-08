# In This Program All  The tree Traversals Are Recursively Implemented

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
            #if node node is empty
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

    # Recursive Inorder Traversal 
    def inorderTraversal(self,node):
        # Base Case
        if node==None:
            return
        # Traverse Left Subtree
        self.inorderTraversal(node.left)
        # print current node's data
        print(node.data,end=' -> ')
        # Traverse Right Subtree
        self.inorderTraversal(node.right)



    # Recursive Preorder Traversal 
    def preorderTraversal(self,node):
        # Base Case
        if node==None:
            return
        print(node.data,end=' -> ')
        # Traverse Left Subtree
        self.preorderTraversal(node.left)
        # Traverse Right Subtree
        self.preorderTraversal(node.right)



    # Recursive Postorder Traversal 
    def postorderTraversal(self,node):
        # Base Case
        if node==None:
            return
        # Traverse Left Subtree
        self.postorderTraversal(node.left)
        # Traverse Right Subtree
        self.postorderTraversal(node.right)
        print(node.data,end=' -> ')
            
if __name__ == "__main__":
    B=BinaryTree()
    B.insert(B.root,10)
    B.insert(B.root,12)
    B.insert(B.root,11)
    B.insert(B.root,8)
    B.insert(B.root,9)
    B.insert(B.root,13)

    print("Inorder Traversal:")
    B.inorderTraversal(B.root)

    print("\n\nPreorder Traversal:")
    B.preorderTraversal(B.root)

    print("\n\nPostorder Traversal:")
    B.postorderTraversal(B.root)
