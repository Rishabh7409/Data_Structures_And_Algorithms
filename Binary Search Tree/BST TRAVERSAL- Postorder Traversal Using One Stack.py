# In This Program We Will Be Doing The Postorder Traversal Of The BST Using Single Stack

# Time Complexity: O(n)  n=number of nodes in BST
# Space Complexity: O(n) n=number of nodes in BST

# Note : We Can Also Have O(1) space complexity if we print the data insetad of storing in list

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Postorder:
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

    def postorder_using_stack(self,node):
        S=[node]
        ans=[]
        #loop while S is not empty
        while S:
            temp=S.pop()
            ans.insert(0,temp.data) #append current data to ans
            
            #append left and right child of the node to stack
            
            if temp.left:
                S.append(temp.left)

            if temp.right:
                S.append(temp.right)
    
        return ans

if __name__=='__main__':

    P=Postorder()
    P.insert(20,P.root)
    P.insert(10, P.root)
    P.insert(24, P.root)
    P.insert(14, P.root)
    P.insert(23, P.root)
    P.insert(1, P.root)
    P.insert(30, P.root)

    print(P.postorder_using_stack(P.root))