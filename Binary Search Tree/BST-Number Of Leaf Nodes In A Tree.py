# In This Program We Will Find The Number Of Leaf Nodes In BST

# We Can Use Any Traversal To Find Leaf Nodes


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

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

    def inorder(self,node):
        if not node:return
        self.inorder(node.left)
        print(node.data,end= ' -> ')
        self.inorder(node.right)

    def number_of_nodes_2(self,node):
        '''Iterative Approach'''
        '''We Can Also Find Out The Number of Leaf Nodes By Using Level order Traversal'''
        if node is None:return 0
        Q=[node]
        leaf=0
        while True:
            count=len(Q)
            if not Q:
                return leaf
            while count:
                temp=Q.pop(0)
                if temp.left is None and temp.right is None:# Because Leaf Node Does not have any child
                    leaf+=1
                if temp.left:Q.append(temp.left)
                if temp.right:Q.append(temp.right)
                count-=1

    def number_of_leaf_nodes(self,node):
        if not node:return 0
    
        if not node.left and not node.right: 
            # since leaf nodes does not have childs
            return 1
        left_val=self.number_of_leaf_nodes(node.left)
        right_val=self.number_of_leaf_nodes(node.right)
        return left_val+right_val

if __name__=='__main__':
    B=Binary()
    B.insert(50,B.root)
    B.insert(30, B.root)
    B.insert(80, B.root)
    B.insert(70, B.root)
    B.insert(28, B.root)
    B.insert(55, B.root)
    B.insert(10, B.root)
    B.insert(69, B.root)
    B.insert(45, B.root)
    B.insert(100, B.root)
    B.insert(12, B.root)
    B.insert(5, B.root)
    B.insert(54, B.root)

    # B.inorder(B.root)

    print("\nThe Number Of Leaf Nodes Using Iteration Are:",B.number_of_nodes_2(B.root))
    print("\nThe Number Of Leaf Nodes Using Recursion Are:", B.number_of_leaf_nodes(B.root))