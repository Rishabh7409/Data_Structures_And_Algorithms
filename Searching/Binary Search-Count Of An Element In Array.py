'''The Total Count Of A Number Is A Sorted Array can Be Find Out By Finding Out Its
 Last Occurence And First Occurence In The Array
 Count=index(last occurence)+index(first occurence)-1'''

def First_Occurence(L,key):
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

def Last_Occurence(L,key):
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
    L=[1,2,5,5,5,5,5,5,5,6,7]
    element=1
    print(f"The Total Count Of {element} Is:",Last_Occurence(L,element)-First_Occurence(L,element)+1)