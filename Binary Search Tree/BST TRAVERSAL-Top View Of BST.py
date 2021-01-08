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

    def Top_View_Order(self,node):
        ''' We Will Be Using Vertical Order Traversal And Dictionaries Concept for findig out the top view of the tree.
            We Will Be Having Two Dictionaries One For Storing Final Results  and another for storing arbitrary values
            or levels of all the nodes of the tree...
            We Will be Traversing all the nodes one by one and storing their respective values or levels in temp_dict..
            We Will then Check that if node of that level is traversed or not..if traversed then we will not do anything
             else we will store the level as key and node as value in the final_result'''
        if not node:return 0
        Q=[node]
        temp_dict=dict()
        final_dict=dict()
        temp_dict[node.data]=0
        while Q:
            temp=list()
            current=Q.pop(0)
            level=temp_dict[current.data]

            if level not in final_dict:
                temp.append(current.data)
                final_dict[level]=temp

            if current.left:
                Q.append(current.left)
                temp_dict[current.left.data]=temp_dict[current.data]-1

            if current.right:
                Q.append(current.right)
                temp_dict[current.right.data]=temp_dict[current.data]+1
        return final_dict

if __name__=='__main__':
    T=TOP_VIEW()
    T.insert(12,T.root)
    T.insert(5, T.root)
    T.insert(19, T.root)
    T.insert(8, T.root)
    T.insert(2, T.root)
    T.insert(89, T.root)
    T.insert(56, T.root)
    x=T.Top_View_Order(T.root)
    print("\nThe Top View Of The Tree Is:",end=' ')
    if x:
        for a in sorted(x.keys()):
            print(*x[a],end=' -> ')
        print()
    else:
        print("Tree Not Created")