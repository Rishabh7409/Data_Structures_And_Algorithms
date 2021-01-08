#Visit Jenny Lectures Youtube In Order To understand more better

def Bucket_sort(array):
    val=len(str(max(array))) # length of maximum element of array
    
    for index,value in enumerate(array):
        array[index]=str(value).zfill(val)  #converting length of all numbers equal to size of largest num

    for i in range(val-1,-1,-1):
        L=[[] for i in range(10)]  #buckets for storing numbers

        # traverse the array
        for value in array:
            ind=int(value[i])

            # at the (i)th position in array append the value  
            L[ind].append(value)  

        array.clear()   #every time new values will be stored in sorted order
        for K in L:
            for x in K:
                array.append(x)
    
    output=[]
    for vl in array:
        output.append(int(vl))
    print(output)

if __name__=='__main__':
    L=[5,3,7,888,9,23,54,67,11]
    Bucket_sort(L)
    # Bucket_sort([55,66,77,34,2,3,1,223,344,333,2,22333,4,566,332,11,99,9,8,8,8,7,7])