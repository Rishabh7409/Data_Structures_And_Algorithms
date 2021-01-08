'''MAX HEAP: All The Descendant Values Are Lesser Than The Root Value'''

'''In MAX Heap Insertion Is Done From Rear End Of The Array i.e. element is inserted from last position'''
def Insertion_In_Max_Heap(L,key):
    L.append(key)
    i=len(L)-1
    Heapify_After_Insertion(L,i)
    return L
    
def Heapify_After_Insertion(Heap,i):
    # if index is in bounds
    if i>0:
        # find the index of parent node
        parent_index = (i - 1) // 2

        # if parent node is less than current node then swap
        if Heap[parent_index]<Heap[i]:
            Heap[parent_index], Heap[i] = Heap[i], Heap[parent_index]
            Heapify_After_Insertion(Heap,parent_index)

if __name__=='__main__':
    L = [10, 30, 40, 5, 60, 20, 23]
    A = []
    for element in L:
        A = Insertion_In_Max_Heap(A, element)
        print(A)