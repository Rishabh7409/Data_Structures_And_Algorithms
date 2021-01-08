
# Definition for a binary tree node.
class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def Inorder2(node, L):
    if not node: 
        return
    Inorder2(node.left, L)
    L.append(node.data)
    Inorder2(node.right, L)
    return L


if __name__=='__main__':
    # main root node
    root=Node(1)

    # childs of root node

    # In this manner also we can insert nodes to a binary tree
    root.left=Node(2)
    root.left.left=Node(4)
    root.right=Node(3)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.right.left.right=Node(8)
    root.right.right.right=Node(9)
    root.right.right.left=Node(10)
    root.right.right.left.right=Node(11)
    root.right.right.left.right.right=Node(12)

    print(Inorder2(root,[]))
