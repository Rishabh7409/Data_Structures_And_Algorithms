

def Heapify(L,index):

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
        Heapify(L,largest_value_index)  #recursive call for heapifying The heap

if __name__=='__main__':
    
    print("BUILDING HEAP")
    A=[6,8,3,9,2,10,1,35,22] # Any Arbitrary Array
    for i in range(len(A)//2,-1,-1):  # we will not heapify leaf nodes because they are already heapified and leaf nodes starts from len(A)//2 to len(A)
        Heapify(A,i)
        print("Current Heap ",A)

    # Deletion Is Done To Get Sorted Data
    print("DELETION")
    ans=[]
    while A:
        ans.append(A[0])
        A[0]=A[-1]
        A.pop()
        Heapify(A,0)
    
    ans.reverse()
    print(ans)