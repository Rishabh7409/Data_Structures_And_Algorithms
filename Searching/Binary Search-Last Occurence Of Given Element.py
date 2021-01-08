def Binary_Search(L,key):
    start=0
    find=-1
    end=len(L)-1
    while(start<end):
        mid=(start+end)//2
        if(L[mid]==key):
            # if element is found
            find=mid
            # for the last occurence we have to search in right sub array
            start = mid + 1
        elif key<L[mid]:
            end=mid-1
        else:
            start=mid+1
    return find if find!=-1 else find

if __name__=='__main__':
    L=[1,2,5,5,5,5,5,6,7]
    a=Binary_Search(L,5)
    if a==-1:
        print("Not Found")
    else:
        print("Last Occurence At Index:",a)