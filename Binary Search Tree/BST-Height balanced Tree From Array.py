# Create Height Balanced Tree From An Array

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Tree:
    def sortedArrayToBST(self,nums):
        if len(nums) == 0:
            return None


        mid = (len(nums)) // 2
        # root node
        root = TreeNode(nums[mid])
        
        # left half array for left subtree 
        root.left = self.sortedArrayToBST(nums[:mid])

        # right half array for right subtree
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root

    def Preorder(self,root):
        if not root:return
        print(root.data,end=' ')
        self.Preorder(root.left)
        self.Preorder(root.right)

if __name__=='__main__':
    T=Tree()
    root=T.sortedArrayToBST([2,4,5,7,8,9,10])
    T.Preorder(root)