'''MAX HEAP: All The Descendant values of the root are less than the root value'''

'''In MAX Heap, Deletion Is Done From Root Node  i.e From 0th index of array'''

def Deletion_In_Max_Heap(L):
    '''
    Steps:
    
    1. Replace the root or element to be deleted by the last element.
    Delete the last element from the Heap.
    
    2. Since, the last element is now placed at the position of the root node. So, it may not follow the heap property. Therefore, heapify the last node placed at the position of root.


    '''
    L[-1],L[0]=L[0],L[-1]  # step 1
    val=L.pop(-1) #step 1
    Heapify_After_Deletion(L,0) #step 2
    return val

def Heapify_After_Deletion(L,index):

    largest_value_index=index

    n=len(L)
    # left child index
    left_index=2*index+1

    # right child index
    right_index=2*index+2

    # find the maximum of left and right child

    if left_index<n and L[left_index]>L[largest_value_index]:
        largest_value_index=left_index

    if right_index<n and L[right_index]>L[largest_value_index]:
        largest_value_index=right_index

    # if any left or right child is greater than current value then swap them 
    if largest_value_index!=index:
        L[largest_value_index],L[index]=L[index],L[largest_value_index]
        Heapify_After_Deletion(L,largest_value_index)  #recursive call for heapifying The heap


if __name__=='__main__':
    Heap=[60,40,30,5,10,20,23]  # Max Heap 
    ans=[]  # Output list
    
    while Heap:
        ans.append(Deletion_In_Max_Heap(Heap))
        print("Current Heap : ",Heap," \tSorted Output: ",ans)