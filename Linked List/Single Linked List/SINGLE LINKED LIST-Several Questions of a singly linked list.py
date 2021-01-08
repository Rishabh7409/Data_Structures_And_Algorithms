'''
This Program is For Single Linked List

Topics Covered:
    1. Insertion Using Recursion
    2. Length of linked List Using recursion and Iteration
    3. Search Element Using recursion and iteration
    4. If linked list is palindrome or not using recursion and iteration
    5. remove duplicates from sorted linked list using iteration and recursion
    6. remove Duplicates from unsorted linked list 
    7. Swapping of two nodes by address not by values using iteration and recursion
    8. Swapping all the linked list elemnts by pair
        e.g  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
        output: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 8 -> 7

    9. Swapping First and Last Nodes
    10. Frequecny Of A Node In Linked List

'''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinked:
    s=''
    def __init__(self):
        self.head=None

    # recursive insertion
    def insert(self,node,data):
        if self.head==None:
            self.head=Node(data)
            return
        elif node.next==None:
            node.next=Node(data)
            return
        self.insert(node.next,data)

    # recursive traversal
    def traverse(self,head):
        if head==None:return
        print(head.data,end=' -> ')
        self.traverse(head.next)

    #The length of linked list
    def get_length(self,node):
        a=0
        current=node
        while current!=None:
            current=current.next
            a+=1
        print("\n\nThe length of Linked List is using iterative method:",a)
    
    # length of linked list recursion
    def get_length_Rec(self,node):
        if node==None:return 0
        else:return 1+self.get_length_Rec(node.next)
    
    #Search an element using iteration
    def search_element(self,node,key):
        current=node
        m=0
        while current.data!=key and current.next!=None:
            current=current.next
            m+=1
        print("\nThe value {} is {} node of linked list.".format(key,m+1))

    # search an element using recursion
    def search_element_Rec(self,node,key):
        if node!=None and node.data==key:
            print("\nThe Key {} Found In The Linked List".format(key))
            return
        elif node==None:
            print("\nThe Key {} Is Not Present In Linked List".format(key))
        else:return self.search_element_Rec(node.next,key)

    #If the linked list is palindrome using recursion
    def palindrome(self,node):
        if node==None:
            if self.s==self.s[::-1]:print("\nThe Given Linked List Is Palindrome")
            else:print("\nThe Given Linked List Is Not Palindrome")
            return
        self.s+=str(node.data)
        self.palindrome(node.next)

    # Palindrome linked list using iteration
    def palindrome2(self,node):
        s=''
        current=node
        while current!=None:
            s+=str(current.data)
            current=current.next
        if s==s[::-1]:print("\nThe Given Linked List Is Palindrome")
        else:print("\nThe Given Linked List Is Not Palindrome")
        return

    # Remove Duplicates from sorted list
    def removeduplicates(self,head):
        current=head
        while current.next!=None:
            if current.data==current.next.data:
                temp=current.next
                current.next=temp.next
                temp.next=None
            else:current=current.next

    # remove duplicates from sorted list using recursion
    def removeduplicates2(self,head):
        if head.next==None:return
        elif head.data==head.next.data:
                temp=head.next
                head.next=temp.next
                temp.next=None
                self.removeduplicates2(head)
        else:
            self.removeduplicates(head.next)

    #Remove Duplicates From Unsorted List
    def removeunsorted(self,head):
        node=head
        while node!=None and node.next!=None:
            current=node
            while current.next!=None:
                if node.data==current.next.data:
                    temp2=current.next
                    temp=current.next.next
                    current.next=temp
                    temp2.next=None
                else:current=current.next
            node=node.next

    # Swapping The two Given Nodes
    def swaptwonodes(self,head,k1,k2):
        if k1==k2:return 
        currX=None
        node1=head
        while node1!=None and node1.data!=k1:
            currX=node1
            node1=node1.next
        currY=None
        node2=head
        while node2!=None and node2.data!=k2:
            currY=node2
            node2=node2.next
            
        #Either k1 or k2 is not present
        if node1==None or node2==None:return
        
        #if k1 is not head value
        if currX!=None:currX.next=node2
        else:self.head=node2
        
        #if k2 is not head value
        if currY!=None:currY.next=node1
        else:self.head=node1

        #swapping the next pointers
        temp=node1.next
        node1.next=node2.next
        node2.next=temp

    # Frequecny of A Node Using Iteration
    def countanum(self,head,key):
        s=0
        node=head
        while node!=None:
            if node.data==key:s+=1
            node=node.next
        print("\nThe Key {} appeared {} times in the linked list\n".format(key,s))

    # Frequency of A Node Using recursion
    def countanum2(self,node,key):
        if node==None:
            return 0
        elif node.data==key:
            return 1+self.countanum2(node.next,key)
        else:
            return self.countanum2(node.next,key)

    #This function is for making the last node of list as first node
    def firsttolast(self,head):
        node=head
        while node.next.next!=None:
            node=node.next
        temp=node.next
        node.next=None
        temp.next=head
        self.head=temp
        
        
    #Swap elements of linked list by pair
    def swappair(self,head):
        node=head
        while node!=None and node.next!=None:
            node.data,node.next.data=node.next.data,node.data
            node=node.next.next

    # Swap elemnts using recursion
    def swappair2(self,node):
        if node==None or node.next==None:return
        else:
            node.data,node.next.data=node.next.data,node.data
            return self.swappair2(node.next.next)

if __name__ == "__main__":
               
    C=SingleLinked()
    C.insert(C.head,6)
    C.insert(C.head,2)
    C.insert(C.head,3)
    C.insert(C.head,1)
    C.insert(C.head,5)
    C.insert(C.head,8)
    C.insert(C.head,6)

    print("The Linked List is:\n")
    C.traverse(C.head)

    # C.get_length(C.head)
    # a=C.get_length_Rec(C.head)

    # print("\nThe length of linked list using recursion: ",a)

    # C.search_element(C.head,1)
    # C.search_element_Rec(C.head,6)

    # C.palindrome(C.head)
    # C.palindrome2(C.head)

    # print("\nRemoving Duplicates")
    # print("This method is for sorted list\n")
    # C.removeduplicates2(C.head)
    # C.traverse(C.head)

    # print("\n\nRemoving Duplicates")
    # print("This method is for sorted list\n")
    # C.removeduplicates(C.head)
    # C.traverse(C.head)

    # print("\n\nRemoving Duplicates")
    # print("This method is for unsorted list\n")
    # C.removeunsorted(C.head)
    # C.traverse(C.head)

    # print("\n\nSwapping The Two Nodes")
    # C.swaptwonodes(C.head,1,5)
    # C.traverse(C.head)

    # C.countanum(C.head,1)

    # key=1
    # s=C.countanum2(C.head,key)
    # print("\nThe Key {} appeared {} times in the linked list\n".format(key,s))


    # C.firsttolast(C.head)
    # C.traverse(C.head)

    # print("\n\nSwapping Elements By Pair")
    # C.swappair(C.head)
    # C.traverse(C.head)

    # print("\n\nSwapping Elements Using Recursion")
    # C.swappair2(C.head)
    # C.traverse(C.head)


