# This Program Is For Finding The Average of All Levels

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


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

    def averageOfLevels(self, root):
            L = []
            Q = [root]
            while True:
                A = []
                count = len(Q)
                if not count:
                    break
                while count:
                    temp = Q.pop(0)
                    A.append(temp.data)
                    if temp.left: Q.append(temp.left)
                    if temp.right: Q.append(temp.right)
                    count -= 1
                L.append(sum(A) / len(A))
            
            for index,val in enumerate(L):
                print("Level: ",index,"\tAverage: ",val)


if __name__ == "__main__":
    
    B = BinaryTree()
    B.insert(B.root, 10)
    B.insert(B.root, 12)
    B.insert(B.root, 1)
    B.insert(B.root, 8)
    B.insert(B.root, 9)
    B.insert(B.root, 13)

    B.averageOfLevels(B.root)