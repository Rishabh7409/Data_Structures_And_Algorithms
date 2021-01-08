# This Program Is To Find Childs Of A Given Node

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary:
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


    def find_child(self,data,node):
        # find childs of a given node
        try:
            if node.data==data:
                print("Finding Childs....")
                if node.left:
                    print(f"The Left Child Of {data} Is",node.left.data)
                if node.right:
                    print(f"The Right Child Of {data} Is",node.right.data)

                if not node.left and not node.right:
                    print(f"The Node {data} Does Not Have Any Child")
                return
            elif data<node.data:
                self.find_child(data,node.left)
            else:
                self.find_child(data,node.right)
        except:
            print("Finding Childs....")
            print(f"The Node {data} Is Not In Tree")

if __name__=='__main__':

    B=Binary()
    
    B.insert(34,B.root)
    B.insert(20, B.root)
    B.insert(50, B.root)
    B.insert(25, B.root)
    B.insert(45, B.root)
    B.insert(33, B.root)
    B.insert(32,B.root)
    B.insert(60, B.root)
    B.insert(70, B.root)
    B.insert(10, B.root)
    B.insert(5, B.root)
    B.insert(1, B.root)

    B.find_child(224,B.root)