def Binary_Search_First_Occurence(L,key):
    start=0
    find=-1
    end=len(L)-1
    while(start<end):
        mid=(start+end)//2
        if(L[mid]==key):
            # if element is found
            find=mid
            # for the first occurence we have to search in left sub array
            
            end=mid-1
        elif key<L[mid]:
            end=mid-1
        else:
            start=mid+1
    return find if find!=-1 else find

if __name__=='__main__':
    L=[1,2,5,5,5,5,5,6,7]
    a=Binary_Search_First_Occurence(L,5)
    if a==-1:
        print("Not Found")
    else:
        print("First Occurence At Index:",a)