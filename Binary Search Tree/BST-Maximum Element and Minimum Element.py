# In This program We Will Find The Maximum and Minimum Element Of BST

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
        if node is None:return
        self.inorder(node.left)
        print(node.data,end=' -> ')
        self.inorder(node.right)

    # the rightmost element of the BST Is MAximum element 
    def maximum(self,node):
        if node.right is None:
            return node.data
        return self.maximum(node.right)
    # the leftmost element of BST Is Minimum element
    def minimum(self,node):
        if node.left is None:
            return node.data
        return self.minimum(node.left)

if __name__=='__main__':
    T=Tree()
    T.insert(50,T.root)
    T.insert(30,T.root)
    T.insert(60,T.root)
    T.insert(55,T.root)
    T.insert(40,T.root)
    T.insert(45,T.root)
    T.insert(37,T.root)
    T.insert(58,T.root)
    T.inorder(T.root)

    max_val=T.maximum(T.root)
    print("\n\nMaximum Element Of The Tree Is:",max_val)
    min_val=T.minimum(T.root)
    print("\n\nMinimum Element Of The Tree Is:",min_val)
