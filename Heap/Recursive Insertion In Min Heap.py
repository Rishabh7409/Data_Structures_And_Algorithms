'''MIN HEAP: All The Descendant Values Are Greater Than The Root Value'''

'''In MIN Heap Insertion Is Done From Rear End Of The Array i.e. element is inserted from last position'''


def Insertion_In_Min_Heap(Heap, key):
    Heap.append(key)
    i = len(Heap) - 1
    Heapify_Min_Heap(Heap, i)
    return Heap


def Heapify_Min_Heap(Heap, i):
    if i > 0:
        parent_index = (i - 1) // 2
        if Heap[parent_index] > Heap[i]:
            Heap[parent_index], Heap[i] = Heap[i], Heap[parent_index]
            Heapify_Min_Heap(Heap, parent_index)


if __name__ == '__main__':
    array=[10,30,40,5,60,20,23]

    Heap_op=[]  # heap to be formed
    for element in array:
        Heap_op=Insertion_In_Min_Heap(Heap_op,element)
        print(Heap_op)
    