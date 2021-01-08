'''Bubble Sort:In Bubble Sort Algorithm the idea is to compare the adjacent elements with each other and if required then swap these elements..'''
def Bubble(L):
    for i in range(len(L)-1):
        is_swap=False
        for j in range(len(L)-1-i): #After every iteartion we will be neglecting last element to be comapared                                               because that element will be at its appropriate place
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
                is_swap=True
        if not is_swap:
            break #If no swapping is done it means that the array is sorted
    print(L)

if __name__=='__main__':
    import time
    init=time.time()
    # for i in range(10000):
    Bubble([6,3,8,9,3,6,4,1,33,2,5,9,0,0,-3,5,2,8])
    print(time.time()-init)