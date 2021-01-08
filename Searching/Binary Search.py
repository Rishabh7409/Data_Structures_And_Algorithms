'''
Binary Search:

    Binary Search is For Sorted Arrays

     Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

'''


def Binary_Search(L,key):
    start=0
    end=len(L)-1
    while(start<end):
        mid=(start+end)//2
        if(L[mid]==key):
            return mid
        elif key<L[mid]:
            end=mid-1
        else:
            start=mid+1
    return "Not Found"

if __name__=='__main__':
    L=[1,2,5,5,5,5,5,6,7]
    print(Binary_Search(L,0))