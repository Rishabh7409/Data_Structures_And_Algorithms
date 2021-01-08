'''
In This Program We have Used The Concept Of Vertical Order Traversal..
Before Proceeding Further Make Sure That You Know Vertical Order Traversal..

Vertical Order Traversal Is Included in this repository please first go through that algorithm in order to understand this better

In This Method The Concept Of Horizontal Distance(HD) From Root Is Used.. 

HD of root node is 0
Any Node Left To The Node Will Have HD=HD(Node)+1
Any Node Right To The Node Will Have HD=HD(Node)

                      20(0)
                    /        \
                  8(1)       22(0)
                /   \        /    \
            5(2)    3(1)    19(1)   25(0)
                    / \      
                10(2)   14(1)

The Right Diagonal View Of The Tree Will Be :
Diagonal 0 : 20 22 25
Diagonal 1 : 8 3 19 14
Diagonal 2 : 5 10

'''

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


    def Right_diagonal_View(self,node):
        # Base Case 
        # if tree is empty
        if not node:
            return 0

        final_dict={}  #Final Answer Dictionary
        Level_dict={}  #For Storing Level Of Each Ndde
        Q=[node]
        Level_dict[node.data]=0  #Root Level Is 0
        while Q:
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
                if HD not in final_dict:
                    final_dict[HD]=[current.data]
                
                else:
                    final_dict[HD].append(current.data)

                # if current node is having left child
                if current.left:
                    Q.append(current.left)

                    # on going to left HD will increase by 1
                    Level_dict[current.left.data]=HD+1

                if current.right:
                    Q.append(current.right)

                    # on going to right HD remains same
                    Level_dict[current.right.data]=HD
                    
        return final_dict

if __name__=='__main__':
    T=Postorder()
    T.insert(12, T.root)
    T.insert(5, T.root)
    T.insert(19, T.root)
    T.insert(8, T.root)
    T.insert(2, T.root)
    T.insert(89, T.root)
    T.insert(56, T.root)
    x=T.Right_diagonal_View(T.root)
    for i,j in x.items():
        print("Diagonal",i," : ",*j)