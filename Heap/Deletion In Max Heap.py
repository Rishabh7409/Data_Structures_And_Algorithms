''' 
Deletion In Max heap:

Steps: 
    Since deleting an element at any intermediary position in the heap can be costly, so we can simply replace the element to be deleted by the last element and delete the last element of the Heap.

    1. Replace the root or element to be deleted by the last element.
    Delete the last element from the Heap.
    
    2. Since, the last element is now placed at the position of the root node. So, it may not follow the heap property. Therefore, heapify the last node placed at the position of root.

'''


def Deletion_In_Max_Heap(L):
    
    # step 1
    L[0],L[-1]=L[-1],L[0]
    val=L.pop(-1)

    k=len(L)-1
    i=0
    while i<k:
        # parent node
        key = L[i]

        # assigning left and right child -1
        left=right=-1

        if 2*i+1<len(L):
            # left child index
            left=2*i+1

        if 2*i+2<len(L):
            # right child index
            right=2*i+2

        # if only right child is present
        if left==-1 and right!=-1:
            if L[right]>key:
                L[i], L[right] = L[right], L[i]
                i = right

        # if only left child is present
        elif left!=-1 and right==-1:
            if L[left]>key:
                L[i], L[left] = L[left], L[i]
                i = left

        # otherwise check if max heap property is already satisfying or not

        elif key<max(L[left],L[right]):
            # if not satisfying replace with maximum of left and right child
            if L[left]>L[right]:
                L[i],L[left]=L[left],L[i]
                i=left
            else:
                L[i],L[right]=L[right],L[i]
                i=right
        else:
            # successfully deleted element and heapified the heap
            break

    return val

if __name__=='__main__':
    ans=[]

    # This is a max heap
    max_heap=[50,45,35,33,16,25,34,12,10]

    while max_heap:
        ans.append(Deletion_In_Max_Heap(max_heap))
    
    # Deletion in max heap is done in order to get the values in sorted order 
    print(ans)