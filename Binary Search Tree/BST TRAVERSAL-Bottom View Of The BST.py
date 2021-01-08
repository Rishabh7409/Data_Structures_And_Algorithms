
'''
In This Program We have Used The Concept Of Vertical Order Traversal..
Before Proceeding Further Make Sure That You Know Vertical Order Traversal..

Vertical Order Traversal Is Included in this repository please first go through that algorithm in order to understand this better


Bottom View Of Tree:
    
    In This Method The Concept Of Horizontal Distance(HD) From Root Is Used..     
    
    The bottom view of a binary tree is the nodes that can be viewed from the bottom of the tree..

                      20(0)
                    /    \
                (-1)8       22(+1)
                /   \      \
           (-2)5      3(0)  25(+2)
                    / \      
               (-1)10    14(+1)

Note : The Value Enclosed in () is HD Of That Node

For the above tree the output should be 5, 10, 3, 14, 25.


HD of root node is 0
Any Node Left To The Node Will Have HD=HD(Node)-1 
Any Node Right To The Node Will Have HD=HD(Node)+1 

'''



# A Tree Node
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class TOP_VIEW:
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


    def Bottom_View(self,node):

        # if tree is not created
        if not node:return 0

        # We use A Queue To Store Nodes
        Q=[node] 
        
        #for storing HD of nodes 
        Level_dict=dict()

        # final answers
        final_dict=dict()

        # HD of root node is 0
        Level_dict[node.data]=0

        while Q:
            # current node
            current=Q.pop(0)

            # get the HD of this node
            HD=Level_dict[current.data]

            # update the value for the current HD
            final_dict[HD]=current.data

            # if current node is having left child
            if current.left:
                Q.append(current.left)

                # on going to left HD decreaes by 1 with respect to its parent
                Level_dict[current.left.data]=HD-1

            if current.right:
                Q.append(current.right)

                # on going to left HD increases by 1 with respect to its parent
                Level_dict[current.right.data]=HD+1
        
        # print in sorted order by HD
        for val in sorted(final_dict.values()):
            print(val,end=' ') 
        

if __name__=='__main__':

    T=TOP_VIEW()
    T.insert(12,T.root)
    T.insert(5, T.root)
    T.insert(19, T.root)
    T.insert(8, T.root)
    T.insert(2, T.root)
    T.insert(89, T.root)
    T.insert(56, T.root)

    T.Bottom_View(T.root)