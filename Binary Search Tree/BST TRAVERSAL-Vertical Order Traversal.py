''' We Will Be Using Vertical Order Traversal And Dictionaries Concept for findig out the vertical order traversal
            of the tree...
            We Will Be Having Two Dictionaries One For Storing Final Results  and another for storing arbitrary values
            or levels of all the nodes of the tree...
            We Will be Traversing all the nodes one by one and storing their respective values or levels in Level_Dict..
            We Will then Check that if node of that level is traversed or not..if traversed then we will take out that list
            from node_value_dict and append this node to that list with the given level..
            else we will store the level as key and node as value in the final_result'''

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


    def vertical_Order_Traversal(self,node):
        
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
            if HD not in final_dict:
                final_dict[HD]=[current.data]

            else:
                final_dict[HD].append(current.data)

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
        for key,val in sorted(final_dict.items()):
            print(key," : " ,val) 

if __name__=='__main__':
    P=Postorder()
    P.insert(20,P.root)
    P.insert(10, P.root)
    P.insert(24, P.root)
    P.insert(14, P.root)
    P.insert(23, P.root)
    P.insert(1, P.root)
    P.insert(30, P.root)
    print("\nThe Vertical Order Traversal Of The Tree Is: ")
    P.vertical_Order_Traversal(P.root)
   
    