def Heap_sort(L,index):

    # let smallest value be the current element only
    smallest_value_index=index

    n=len(L)
    left_child_index=2*index+1 # left child index
    right_child_index=2*index+2 #right child index

    # find minimum of left and right child

    if left_child_index<n and L[smallest_value_index]>L[left_child_index]:
        smallest_value_index=left_child_index

    if right_child_index<n and L[smallest_value_index]>L[right_child_index]:
        smallest_value_index=right_child_index

    # if there is an element smaller than current element then
    if smallest_value_index!=index:
        # swap the elements
        L[smallest_value_index],L[index]=L[index],L[smallest_value_index]
        Heap_sort(L,smallest_value_index) # recursive call for heapify

if __name__=='__main__':
    L=[7,5,9,1,3,275,4,2,3,4,5,6]
    for i in range(len(L)//2,-1,-1):
        Heap_sort(L,i)
        print(L)

    sorted=[]
    while L:
        L[0],L[-1]=L[-1],L[0]
        sorted.append(L.pop(-1))
        Heap_sort(L,0)
    print("\n\nSorted Array:",sorted)