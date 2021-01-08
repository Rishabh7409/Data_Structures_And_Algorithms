# Since The Traversals Of Binary Tree And Binary Search Tree Are Similar I Have Just Discussed
#  Preorder, Postorder and Inorder Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Binary_Tree:

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
    
     # Inorder Traversal Of Binary Tree
    def Inorder(self, node):
        # Base case
        if not node: 
            return
        # Left subtree traversal
        self.Inorder(node.left)
        print(node.data, end=' ')

        # right subtree traversal
        self.Inorder(node.right)

    def preorder(self, node):
        # Base case
        if not node: return
        print(node.data, end=' ')
        
        # Left subtree traversal
        self.preorder(node.left)

        # Right subtree traversal
        self.preorder(node.right)

    def postorder(self, node):
        # Base case
        if not node: 
            return

        # Left subtree traversal
        self.preorder(node.left)

        # Right subtree traversal
        self.preorder(node.right)
        print(node.data, end=' ')

if __name__ == '__main__':
    C = Binary_Tree()
    data = int(input("Enter The Root Node Of This Tree"))
    main_root = C.insert(data)
    print("The Preorder Traversal Of The Created Binary Tree Is: ", end=' ')
    C.preorder(main_root)

    print("\n\nThe Postorder Traversal Of The Created Binary Tree Is: ", end=' ')
    C.postorder(main_root)

    print("\n\nThe Inorder Traversal Of The Created Binary Tree Is: ", end=' ')
    C.Inorder(main_root)