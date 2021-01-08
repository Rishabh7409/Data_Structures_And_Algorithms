def Merge_Sort(L,lb,ub):
    if lb<ub:
        mid=(lb+ub)//2
        Merge_Sort(L,lb,mid)
        Merge_Sort(L,mid+1,ub)
        Merge_List(L,lb,mid,ub)
    return L

def Merge_List(A,lb,mid,ub):
    L=[0]*(lb+ub+1) #Creating Another list with the no. of  elements equal to A
    k=lb
    i=lb
    j=mid+1
    '''This loop will set values in increasing order in new List'''
    while i<=mid and j<=ub:
        if A[i]<=A[j]:
            L[k]=A[i]
            i+=1
            k+=1
        else:
            L[k]=A[j]
            j+=1
            k+=1

    ''' if all the elements from lb to mid+1 are not traversed it means these all will be larger elements'''
    while i<mid+1:
        L[k]=A[i]
        i+=1
        k+=1
    ''' if all the elements from mid+1 to ub are not traversed it means these all will be larger elements'''
    while j<ub+1:
        L[k]=A[j]
        j+=1
        k+=1
    ''' Copying values back to original list'''

    # A[lb:ub+1]=L[lb:ub+1]  #Either Do this or the step mentioned below

    for x in range(lb,ub+1):
        A[x]=L[x]

if __name__=='__main__':
    import time
    # L=[7,6,5,4,3,2,1]
    L=[5,2,6,7,8,3,5,4,7,8,9,0,-8,0,12,32,3,4,5,5,4,7,8,9,0,-8,0,12,32,3,4,5]
    print(Merge_Sort(L,0,len(L)-1))