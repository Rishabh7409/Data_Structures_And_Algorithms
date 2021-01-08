# In This Program We Will Determine The Height Of A Given Node

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Height_Of_Node:
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
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end='->')
        self.inorder(node.right)

    #This Function returns the addresses of the given node
    # Since We Have node's data only to find its height we must determine its address
    def height(self,node,key):
        if node.data==key:
            
            # if the specified node is matched then get its height
            self.get_height(node)
            return
        if key<node.data:
            self.height(node.left,key)
        else:
            self.height(node.right,key)

    #This Functions Prints the height of the given node
    def get_height(self,node):

        # We Will Calculate the height of a node using level order traversal
        Q=[node]
        height=-1
        while True:
            count=len(Q)
            if not count:
                print("\n\nThe Height Of The Given Node Is",height)
                return
            height+=1
            while count:
                temp=Q.pop(0)
                if temp.left:Q.append(temp.left)
                if temp.right:Q.append(temp.right)
                count-=1

if __name__=='__main__':

    T=Height_Of_Node()
    T.insert(40,T.root)
    T.insert(70, T.root)
    T.insert(30, T.root)
    T.insert(35, T.root)
    T.insert(45, T.root)
    T.insert(80, T.root)
    T.insert(20, T.root)
    T.insert(10, T.root)
    T.insert(15, T.root)

    # T.inorder(T.root)

    # get height of specified node
    T.height(T.root,40)