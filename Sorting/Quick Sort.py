'''Quick Sort: The Main Idea behind this alogorithm is that an element is selected from the provided array and one element called pivot element is selected from the list and based on this element the sorting is performed.
All the Elements left to this pivot element are less than pivot element and to the right of the pivot element the element are greater than pivot element.
This Is  Divide and conquer technique in which array is subdivided into subarray and the solution is applied to them and the output is then combined to get the desired result
This algorithm is based on recursion..'''

'''In This Algorithm We Will Be Using The First Element Of The List As Pivot Element'''

def Partition(L,lb,ub):
    pivot=L[lb] #Selection of pivot element
    i=lb #Avoiding the index of pivot element
    j=ub
    while i<j:
        while i<=j and L[i]<=pivot:#Finding The index of the element which is greater than the pivot element
            i+=1
        while i<=j and L[j]>pivot:#Finding The index of the element which is smaller than the pivot element
            j-=1
        if i<j:     #if index of start and end element crosses each other
            L[i],L[j]=L[j],L[i] #Swapping These Elements

    L[lb],L[j]=L[j],L[lb]   #Putting pivot element at its appropriate place
    return j #returning index before the index of pivot element

def Quick_Sort(L,lb,ub):
    if lb<ub:
        loc=Partition(L,lb,ub)
        #Recursive Calls for the divided arrays
        Quick_Sort(L,lb,loc-1)
        Quick_Sort(L,loc+1,ub)
    return L

if __name__=='__main__':

        L = [1,2,3,4,5,6,7,8,9]
        L=[8,7,6,5,4,3,2,1]
        print(Quick_Sort(L, 0, len(L) - 1))
        