
'''
ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The idea of shellSort is to allow exchange of far items. In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sublists of every h’th element is sorted.
'''

'''

Visit Jenny Lectures For More information
'''

def Shell_Sort(L):
    n=len(L)
    gap=n//2
    
    while gap>=1:
        for j in range(gap,n):
            i=j-gap
            while i>=0:
                if L[i+gap]>L[i]:
                    break
                else:
                    L[i+gap],L[i]=L[i],L[i+gap]
                i-=gap
        gap//=2
    print(L)

if __name__=='__main__':
    arr=[7,3,4,5,6,1]
    Shell_Sort(arr)
    Shell_Sort([6,5,4,3,5,6,7,8,9,0])
    Shell_Sort([-1,-4,-6,-3,-7,-8])