class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Binary_Tree:

    # insertion In Binary tree
    def insert(self, data):
        root = Node(data)

        # Left child of current node
        x = int(input(f"Enter Left Child Of {data} and 0 For No Left Child: "))
        if x: 
            root.left = self.insert(x)  # recursive call for inserting in left subtree

        # Right Child of current node
        y = int(input(f"Enter Right Child Of {data} and 0 For No Right Child: "))
        if y: 
            root.right = self.insert(y) # recursive call for inserting in right subtree 
        return root

    def Inorder(self,node):
        if not node:return
        self.Inorder(node.left)
        print(node.data, end=' ')
        self.Inorder(node.right)

if __name__=='__main__':

    C=Binary_Tree()
    data=int(input("Enter The Data for Root Node Of This Tree"))

    main_root=C.insert(data)

    print("The Inorder Traversal Of The Created Binary Tree Is:",end=' ')
    C.Inorder(main_root)
