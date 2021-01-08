'''In Insertion sort the array is divided into two parts one array is sorted and the other array is unsorted
We continuously takes an element from the unsorted array and insert it to the appropriate place in the sorted array
In this sorting the array is sorted from left to right'''

def insertion(L):
    for i in range(1,len(L)):
        temp=L[i]
        j=i-1
        while  j>=0 and L[j]>=temp:
            L[j+1]=L[j]
            j-=1
        L[j+1]=temp
    print(L)

if __name__ == "__main__":
    L = [8, 3, 4, 9, 1, 2, 7, 6, 3, 4, 2, 5, 2, 9, 8, 5, 6, 7, 3, 4, 6, 5, 66, 5, 7, 0, 5, 8, 1, 4, 32, 5, 6, 4, 6, 8,
         5, 8, 3, ]
    L=[6,3,8,9,3,6,4,1,33,2,5,9,0,0,-3,5,2,8]
    insertion(L)