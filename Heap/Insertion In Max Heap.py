# To continue further you make sure that you are familiar with max heap

''' 
Steps :
1. First increase the heap size by 1, so that it can store the new element.
2. Insert the new element at the end of the Heap.
3. This newly inserted element may distort the properties of Heap for its parents. So, in order to keep the properties of Heap, heapify this newly inserted element following a bottom-up approach.
'''

def Insertion_In_Max_Heap(L,key):
    L.append(key)    # increase size by 1 and append to the end of heap
    i=len(L)-1

    # Heapify The Heap After Inserting the element
    while i>0:
        parent_of_key = (i-1) // 2    #parent of i-th(key) node=(index of i-th node-1)//2

        # since it is max heap 
        # therefore max element should be at the top of heap

        # if newly inserted node's parent is smaller than the newly inserted node then
        if L[parent_of_key]<key:
            # swap them
            L[parent_of_key],L[i]=L[i],L[parent_of_key]
            i=parent_of_key
        else:
            #we have successfull inserted the new element
            break
    return L


if __name__=='__main__':
    L=[]
    print(Insertion_In_Max_Heap(L,23))
    print(Insertion_In_Max_Heap(L, 43))
    print(Insertion_In_Max_Heap(L, 21))
    print(Insertion_In_Max_Heap(L, 56))
    print(Insertion_In_Max_Heap(L, 78))
    print(Insertion_In_Max_Heap(L, 1))
