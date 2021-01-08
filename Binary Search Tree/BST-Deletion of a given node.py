# in This program We Will Be Deleting A Given node From BST


class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class BinaryTree:
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


    #Pre-order traversal of the tree- Root-Left-Right            
    def PreorderTraversal(self,node):
        if node==None:return
        else:
            print(node.data,end=' ')
            self.PreorderTraversal(node.left)
            self.PreorderTraversal(node.right)

    #Inorder Predecessor of the tree i.e. the maximum value in the left subtree of the  tree
    def minval(self,root):
        current=root
        while current.left is not None:
            current=current.left
        return current

    #Inorder Successsor of the tree i.e. the minimum value in the right subtree of the tree
    def maxval(self,root):
        current=root
        while current.right is not None:
            current=current.right
        return current

    #Function for the deleting the node from the tree
    def deletenode(self,root,key):
        if root is None:return  #Base case
        
        elif key<root.data:#checking if key is less than root
            root.left=self.deletenode(root.left,key)
            
        elif key>root.data:#checking if key is greater than root
            root.right=self.deletenode(root.right,key)
            
        else:
            #the node to be deleted is found
            
            #The node to be deleted is having only one child or no child
            if root.left==None:
                temp=root.right
                root=None
                return temp
            elif root.right==None:
                temp=root.left
                root=None
                return temp

            #The node to be deleted is having two childs..
            else:
                #Here we can either of two operations
                #1.Replace the node to be deleted with its inorder successor
                #2.Replace the node to be deleted with its inorder predecessor

                #Method 1:
                temp=self.maxval(root.left)
                root.data=temp.data
                root.left=self.deletenode(root.left,temp.data)

                #Method 2:
                '''temp=self.minval(root.right)
                root.data=temp.data
                root.right=self.deletenode(root.right,temp.data)'''
        return root  #returning root value
    
if __name__ == "__main__":
    B=BinaryTree()
    B.insert(18,B.root)
    B.insert(23,B.root)
    B.insert(32,B.root)
    B.insert(71,B.root)
    B.insert(17,B.root)
    B.insert(21,B.root)
    B.insert(12,B.root)

    print("Inorder Traversal Before Deletion Of Node:")
    B.PreorderTraversal(B.root)

    node_data_to_delete=18

    B.deletenode(B.root,node_data_to_delete)
    print("\n\nInorder Traversal After Deletion Of Node:")
    B.PreorderTraversal(B.root)
