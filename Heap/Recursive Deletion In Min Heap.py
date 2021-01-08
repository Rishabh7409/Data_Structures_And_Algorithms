'''MIN HEAP:All The Descendants of The Root Are Greater Than The Root Value'''

'''In MIN Heap Deletion Is Done From Root Node  i.e From 0th index of array'''

def Deletion_IN_Min_Heap(L):
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
    smallest_value_index=index

    n=len(L)
    # left child index
    left_index=2*index+1

    # right child index
    right_index=2*index+2

    # find the minimum of left and right child

    if left_index<n and L[left_index]<L[smallest_value_index]:
        smallest_value_index=left_index

    if right_index<n and L[right_index]<L[smallest_value_index]:
        smallest_value_index=right_index

    # if any left or right child is less than current value then swap them 
    if smallest_value_index!=index:
        L[smallest_value_index],L[index]=L[index],L[smallest_value_index]
        Heapify_After_Deletion(L,smallest_value_index)  #recursive call for heapifying The heap


if __name__=='__main__':
    Heap=[5,10,20,30,60,40,23]
    ans=[]
    # Min heap deletion is done to get elements sorted order
    while Heap:
        ans.append(Deletion_IN_Min_Heap(Heap))
        print("Current Heap: ",Heap,"\tSorted Output",ans)